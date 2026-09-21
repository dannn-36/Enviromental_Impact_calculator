"""Analizador estático de impacto ambiental basado en ANTLR.

Uso:
    from analyzer import analyze
    report = analyze(codigo, "python")
"""
from .core import MODULE_SCOPE, TreeAnalyzer, logical_lines, parse
from .languages import LANGUAGES, LanguageSpec, resolve_language
from .scoring import interpret, language_adjusted, score

__all__ = ["analyze", "LANGUAGES", "resolve_language", "UnsupportedLanguage"]


class UnsupportedLanguage(ValueError):
    pass


def analyze(code: str, language: str) -> dict:
    spec = resolve_language(language)
    if spec is None:
        raise UnsupportedLanguage(language)

    parsed = parse(code, spec)
    tree_analyzer = TreeAnalyzer(spec, parsed)
    tree_analyzer.run()
    tree_analyzer.analyze_call_graph()

    functions = tree_analyzer.functions
    module = tree_analyzer.module
    scopes = functions + [module]

    def total(attr):
        return sum(getattr(s, attr) for s in scopes)

    # La complejidad ciclomática se mide por función; si el archivo no tiene
    # funciones (un script), se usa el código de nivel superior.
    cc_scopes = functions or [module]
    cyclomatic = [s.cyclomatic for s in cc_scopes]
    cyclomatic_avg = sum(cyclomatic) / len(cyclomatic)
    recursive = [f for f in functions if f.recursive]
    worst = max(s.complexity for s in scopes)
    calls = sum(len(s.calls) for s in scopes)

    result = score(
        worst=worst,
        estimated_operations=total("estimated_operations"),
        cyclomatic_avg=cyclomatic_avg,
        cyclomatic_max=max(cyclomatic),
        recursive_functions=len({f.name for f in recursive}),
        allocations=total("allocations"),
        allocations_in_loops=total("allocations_in_loops"),
    )

    return {
        "language": spec.key,
        "language_name": spec.display_name,
        "parsed_with_antlr": True,
        "syntax_ok": not parsed.errors,
        "syntax_errors": parsed.errors,
        "parse_time_ms": parsed.elapsed_ms,
        "prediction_mode": parsed.prediction_mode,
        "metrics": {
            "lines_of_code": logical_lines(parsed.tokens),
            "functions": len(functions),
            "loops": total("loops"),
            "max_loop_depth": max(s.max_loop_depth for s in scopes),
            "branches": total("branches"),
            "cyclomatic_avg": round(cyclomatic_avg, 2),
            "cyclomatic_max": max(cyclomatic),
            "assignments": total("assignments"),
            "operators": total("operators"),
            "calls": calls,
            "allocations": total("allocations"),
            "allocations_in_loops": total("allocations_in_loops"),
            "estimated_operations": total("estimated_operations"),
            "recursive_functions_count": len({f.name for f in recursive}),
            "recursive_functions": sorted({f.name for f in recursive}),
            "estimated_complexity": worst.label(),
        },
        "functions": [
            {
                "name": f.name,
                "line": f.line,
                "end_line": f.end_line,
                "cyclomatic": f.cyclomatic,
                "loops": f.loops,
                "max_loop_depth": f.max_loop_depth,
                "effective_loop_depth": f.effective_loop_depth,
                "calls": len(f.calls),
                "assignments": f.assignments,
                "recursive": f.recursive,
                "recursion_kind": f.recursion_kind,
                "recursion_branching": f.recursion_branching if f.recursive else 0,
                "complexity": f.complexity.label(),
            }
            for f in functions
        ],
        "eco_score": result["score"],
        "eco_score_breakdown": result["penalties"],
        "interpretation": interpret(result["score"]),
        "language_energy_factor": spec.energy_factor,
        "eco_score_language_adjusted": language_adjusted(result["score"], spec.energy_factor),
    }
