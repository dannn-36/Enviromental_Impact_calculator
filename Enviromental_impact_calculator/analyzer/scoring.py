"""Cálculo de la puntuación ambiental (0-100, más alto = más eficiente).

La puntuación parte de 100 y resta cinco penalizaciones acotadas. Cada una
mide un factor que aumenta el trabajo de la CPU / memoria y, por tanto, la
energía consumida al ejecutar el código:

  complejidad   (máx. 45)  orden de complejidad estimado del peor caso del programa
  operaciones   (máx. 20)  operaciones ejecutadas estimadas (bucles × 10 iteraciones)
  ciclomática   (máx. 15)  complejidad ciclomática media y máxima por función
  recursión     (máx. 10)  funciones recursivas (sobrecoste de pila por llamada)
  memoria       (máx. 10)  reservas de memoria, sobre todo dentro de bucles
"""
import math

from .core import Complexity

COMPLEXITY_PENALTIES = [
    # (complejidad, penalización) ordenado de menor a mayor
    (Complexity(), 0),                       # O(1)
    (Complexity(log=1), 4),                  # O(log n)
    (Complexity(poly=1), 8),                 # O(n)
    (Complexity(poly=1, log=1), 14),         # O(n log n)
    (Complexity(poly=2), 24),                # O(n²)
    (Complexity(poly=2, log=1), 30),         # O(n² log n)
    (Complexity(poly=3), 36),                # O(n³)
]
MAX_POLY_PENALTY = 42      # O(n⁴) o peor
EXPONENTIAL_PENALTY = 45   # O(2ⁿ)


def complexity_penalty(c: Complexity) -> float:
    if c.exponential:
        return EXPONENTIAL_PENALTY
    for reference, penalty in COMPLEXITY_PENALTIES:
        if c <= reference:
            return penalty
    return MAX_POLY_PENALTY


def score(worst: Complexity, estimated_operations: int, cyclomatic_avg: float,
          cyclomatic_max: int, recursive_functions: int, allocations: int,
          allocations_in_loops: int) -> dict:
    penalties = {
        "complejidad": complexity_penalty(worst),
        "operaciones": min(20.0, 5 * math.log10(1 + estimated_operations / 10)),
        "ciclomatica": min(15.0, max(0.0, cyclomatic_avg - 1) * 1.5 + max(0, cyclomatic_max - 10) * 0.5),
        "recursion": min(10.0, 4.0 * recursive_functions),
        "memoria": min(10.0, 0.5 * (allocations - allocations_in_loops) + 2.0 * allocations_in_loops),
    }
    penalties = {k: round(v, 2) for k, v in penalties.items()}
    total = max(0.0, min(100.0, 100 - sum(penalties.values())))
    return {"score": round(total, 2), "penalties": penalties}


def language_adjusted(score_value: float, energy_factor: float) -> float:
    """Ajusta la puntuación con el consumo relativo del lenguaje (C = 1).

    Se usa el logaritmo para que el lenguaje module la nota sin dominarla:
    C ×1.00, Java ×0.97, C# ×0.95, Go ×0.95, Python ×0.81.
    """
    factor = 1 - 0.1 * math.log10(max(1.0, energy_factor))
    return round(score_value * factor, 2)


def interpret(score_value: float) -> str:
    if score_value >= 80:
        return "Excelente eficiencia ambiental 🌿"
    if score_value >= 60:
        return "Buena eficiencia 🍃"
    if score_value >= 40:
        return "Moderada 🌱"
    return "Impacto alto ⚠️"
