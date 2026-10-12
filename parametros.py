"""
parametros.py - Parámetros del proyecto Grupo 4 (EID Cálculo Intermedio 2026).

Aquí están TODOS los valores que debes poder explicar en la defensa:
la función del ejemplo, el intervalo y los números de subintervalos,
además del estilo visual reutilizable.

Tema: Eje 4 - Del símbolo de sumatoria al símbolo de integral.
Pregunta central: ¿Cómo pasamos de una suma con un número finito de
rectángulos a una integral definida?
"""

from manim import *


# =============================================================================
# 1. PARÁMETROS MATEMÁTICOS  (lo que define el ejemplo propio)
# =============================================================================

# Intervalo de integración [a, b]
A = 0
B = 3


def F(x):
    """
    Función del ejemplo propio (distinta a las del apunte):
        f(x) = (1/2)(x - 1)^2 + 1
    Es continua y no negativa en [A, B], por lo que la integral coincide
    con el área geométrica.
    """
    return 0.5 * (x - 1) ** 2 + 1


# Número de subintervalos de la construcción paso a paso
N_INICIAL = 4

# Números de subintervalos para el refinamiento progresivo (prepara el límite n→∞)
REFINAMIENTO_N_LIST = [4, 8, 16, 32]


# =============================================================================
# 2. ESTILO VISUAL  (colores y tamaños, común a todas las escenas)
# =============================================================================

# Configuración de los ejes coordenados
AXES_CONFIG = {
    "x_range": [-0.2, 3.2, 0.5],
    "y_range": [-0.2, 3.5, 0.5],
    "x_length": 6,
    "y_length": 3.5,
    "axis_config": {
        "include_tip": True,
        "tip_shape": StealthTip,
        "stroke_width": 2.5,
    },
}

AXES_LABELS = ("x", "f(x)")

# Desplazamiento vertical de los ejes: los bajamos para reservar una franja
# superior limpia donde van los títulos y las etiquetas (evita superposiciones).
AXES_VERTICAL_SHIFT = DOWN * 0.5

# Margen superior estándar para los títulos
TITULO_BUFF = 0.5

# Curva de la función
CURVA_ESTILO = {"color": BLUE, "stroke_width": 4}

# Rectángulos del refinamiento (muchos, más tenues)
RECTANGULOS_ESTILO = {
    "color": ORANGE,
    "fill_opacity": 0.35,
    "stroke_width": 1.5,
}

# Rectángulo destacado (construcción paso a paso)
RECTANGULO_DESTACADO_ESTILO = {
    "color": ORANGE,
    "fill_opacity": 0.4,
    "stroke_width": 2,
}

# Punto muestra x_i^*
PUNTO_MUESTRA_ESTILO = {"color": YELLOW, "radius": 0.08}

# Líneas verticales de la partición / del punto muestra
LINEAS_MUESTRA_ESTILO = {
    "color": YELLOW,
    "stroke_width": 2,
    "line_func": DashedLine,
}

# Altura f(x_i^*)
ALTURA_ESTILO = {"color": GREEN, "stroke_width": 3}

# Escalas de texto (para mantener proporciones uniformes)
TITULO_ESCALA = 0.85
SUBTITULO_ESCALA = 0.7
TEX_ESCALA = 0.8
MATH_TEX_ESCALA = 0.85
FORMULA_GRANDE_ESCALA = 1.1
MAPEO_ESCALA = 0.8
