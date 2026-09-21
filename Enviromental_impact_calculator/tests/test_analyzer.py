"""Tests del analizador estático sobre los ejemplos de los cinco lenguajes.

Ejecutar desde la carpeta Enviromental_impact_calculator/:
    python -m pytest
"""
from pathlib import Path

import pytest

from analyzer import UnsupportedLanguage, analyze

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

EXAMPLE_FILES = {
    "python": "algoritmos.py",
    "java": "Algoritmos.java",
    "c": "algoritmos.c",
    "go": "algoritmos.go",
    "csharp": "Algoritmos.cs",
}

# Nombre de cada algoritmo en cada lenguaje (siguen las convenciones de cada uno)
NAMES = {
    "fibonacci": {"python": "fibonacci", "java": "fibonacci", "c": "fibonacci", "go": "fibonacci", "csharp": "Fibonacci"},
    "bubble": {"python": "bubble_sort", "java": "bubbleSort", "c": "bubble_sort", "go": "bubbleSort", "csharp": "BubbleSort"},
    "binary": {"python": "binary_search", "java": "binarySearch", "c": "binary_search", "go": "binarySearch", "csharp": "BinarySearch"},
    "total": {"python": "total", "java": "total", "c": "total", "go": "total", "csharp": "Total"},
    "merge_sort": {"python": "merge_sort", "java": "mergeSort", "c": "merge_sort", "go": "mergeSort", "csharp": "MergeSort"},
    "is_even": {"python": "is_even", "java": "isEven", "c": "is_even", "go": "isEven", "csharp": "IsEven"},
}

EXPECTED_COMPLEXITY = {
    "fibonacci": "O(2ⁿ)",
    "bubble": "O(n²)",
    "binary": "O(log n)",
    "total": "O(n)",
    "merge_sort": "O(n log n)",
    "is_even": "O(n)",
}


@pytest.fixture(scope="module", params=list(EXAMPLE_FILES))
def report(request):
    language = request.param
    code = (EXAMPLES / EXAMPLE_FILES[language]).read_text(encoding="utf-8")
    return language, analyze(code, language)


def _function(language, result, algorithm):
    name = NAMES[algorithm][language]
    matches = [f for f in result["functions"] if f["name"] == name]
    assert matches, f"{name} no encontrada en {language}"
    return matches[0]


def test_examples_parse_without_errors(report):
    language, result = report
    assert result["syntax_ok"], result["syntax_errors"]


@pytest.mark.parametrize("algorithm", list(EXPECTED_COMPLEXITY))
def test_complexity_is_consistent_across_languages(report, algorithm):
    language, result = report
    assert _function(language, result, algorithm)["complexity"] == EXPECTED_COMPLEXITY[algorithm]


def test_recursion_detection(report):
    language, result = report
    fib = _function(language, result, "fibonacci")
    assert fib["recursive"] and fib["recursion_kind"] == "directa" and fib["recursion_branching"] == 2
    assert _function(language, result, "binary")["recursion_branching"] == 1
    assert _function(language, result, "is_even")["recursion_kind"] == "mutua"
    assert not _function(language, result, "bubble")["recursive"]
    assert result["metrics"]["recursive_functions_count"] == 5


def test_loops_and_nesting(report):
    language, result = report
    bubble = _function(language, result, "bubble")
    assert bubble["loops"] == 2
    assert bubble["max_loop_depth"] == 2
    assert result["metrics"]["max_loop_depth"] == 2


def test_score_is_bounded_and_explained(report):
    _, result = report
    assert 0 <= result["eco_score"] <= 100
    penalties = result["eco_score_breakdown"]
    assert set(penalties) == {"complejidad", "operaciones", "ciclomatica", "recursion", "memoria"}
    assert result["eco_score"] == pytest.approx(max(0, 100 - sum(penalties.values())), abs=0.02)


def test_language_adjustment_orders_c_first():
    code = {lang: (EXAMPLES / f).read_text(encoding="utf-8") for lang, f in EXAMPLE_FILES.items()}
    c = analyze(code["c"], "c")
    py = analyze(code["python"], "python")
    assert c["eco_score_language_adjusted"] == c["eco_score"]
    assert py["eco_score_language_adjusted"] < py["eco_score"]


@pytest.mark.parametrize("language,code", [
    ("python", "def f(:\n    return 1\n"),
    ("java", "class A { void f() { int x = ; } }"),
    ("c", "int main( { return 0; }"),
    ("go", "package main\nfunc main() {\n"),
    ("csharp", "class A { void F() { int x = ; } }"),
])
def test_syntax_errors_are_reported(language, code):
    result = analyze(code, language)
    assert not result["syntax_ok"]
    assert result["syntax_errors"][0]["line"] >= 1


@pytest.mark.parametrize("language,code", [
    # Strings interpolados de C# (usan CSharpLexerBase)
    ("csharp", 'class A { string F(string n, double x) { return $"Hola {n}, {x:N2} {(x > 1 ? "a" : "b")} {{no}}" + $@"C:\\{n}"; } }'),
    # Canales y method expressions de Go (usan GoParserBase)
    ("go", "package main\n\nimport \"fmt\"\n\ntype T struct{}\n\nfunc (t *T) Get() int { return 1 }\n\n"
           "func w(in <-chan int, out chan<- int) {\n\tfor v := range in {\n\t\tout <- v\n\t}\n}\n\n"
           "func main() {\n\tf := (*T).Get\n\tfmt.Println(f)\n}\n"),
    # Records con varargs y anotaciones con nombre (usan JavaParserBase)
    ("java", '@SuppressWarnings(value = "x") record P(int x, int... ys) { int s() { return x; } }'),
    # Indentación, comprehensions y archivo sin salto de línea final (Python3LexerBase)
    ("python", "class A:\n    def f(self):\n        return [i for i in range(3) if i]\n\n\nx = A().f()"),
])
def test_grammar_base_classes(language, code):
    result = analyze(code, language)
    assert result["syntax_ok"], result["syntax_errors"]


def test_comments_and_strings_are_not_counted():
    code = 'def f():\n    # for i in range(10): while True\n    s = "for while if"\n    return s\n'
    metrics = analyze(code, "python")["metrics"]
    assert metrics["loops"] == 0
    assert metrics["branches"] == 0


def test_empty_code():
    for language in EXAMPLE_FILES:
        result = analyze("", language)
        assert result["eco_score"] == 100


def test_language_aliases():
    assert analyze("int f(){return 0;}", "C")["language"] == "c"
    assert analyze("class A{}", "c#")["language"] == "csharp"
    with pytest.raises(UnsupportedLanguage):
        analyze("x", "cobol")
