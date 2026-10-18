"""Parámetros y estilo visual del EID Grupo 4 (Cálculo Intermedio)."""

from manim import *
import os

A = 0
B = 3


def F(x):
    return 0.5 * (x - 1) ** 2 + 1


N_INICIAL = 4
REFINAMIENTO_N_LIST = [4, 8, 16, 32]

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

AXES_VERTICAL_SHIFT = DOWN * 0.5

TITULO_BUFF = 0.5

CURVA_ESTILO = {"color": BLUE, "stroke_width": 4}

RECTANGULOS_ESTILO = {
    "color": ORANGE,
    "fill_opacity": 0.35,
    "stroke_width": 1.5,
}

RECTANGULO_DESTACADO_ESTILO = {
    "color": ORANGE,
    "fill_opacity": 0.4,
    "stroke_width": 2,
}

PUNTO_MUESTRA_ESTILO = {"color": YELLOW, "radius": 0.08}

LINEAS_MUESTRA_ESTILO = {
    "color": YELLOW,
    "stroke_width": 2,
    "line_func": DashedLine,
}

ALTURA_ESTILO = {"color": GREEN, "stroke_width": 3}

TITULO_ESCALA = 0.85
SUBTITULO_ESCALA = 0.7
TEX_ESCALA = 0.8
MATH_TEX_ESCALA = 0.85
FORMULA_GRANDE_ESCALA = 1.1
MAPEO_ESCALA = 0.8

FACTOR_PAUSAS = float(os.getenv("EID_FACTOR_PAUSAS", "1.0"))

TEXTO_INTEGRANTES = "Gustavo Martínez · Ariel Díaz"
