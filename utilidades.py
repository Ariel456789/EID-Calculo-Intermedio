"""Funciones auxiliares reutilizables por las escenas."""

from manim import *
import parametros as P


def crear_ejes_y_curva():
    ax = Axes(**P.AXES_CONFIG)
    ax.shift(P.AXES_VERTICAL_SHIFT)
    ax_labels = ax.get_axis_labels(*P.AXES_LABELS)
    curva = ax.plot(P.F, x_range=[P.A, P.B], **P.CURVA_ESTILO)
    return ax, ax_labels, curva


def punto_muestra(x_left, x_right, criterio="midpoint"):
    if criterio == "left":
        return x_left
    if criterio == "right":
        return x_right
    return (x_left + x_right) / 2


def crear_rectangulo(ax, x_left, x_right, y_top, estilo=None):
    estilo = estilo or P.RECTANGULO_DESTACADO_ESTILO
    return Polygon(
        ax.c2p(x_left, 0),
        ax.c2p(x_right, 0),
        ax.c2p(x_right, y_top),
        ax.c2p(x_left, y_top),
        **estilo,
    )


def crear_elementos_muestra(ax, i, x_star, y_star):
    dot_xstar = Dot(ax.c2p(x_star, 0), **P.PUNTO_MUESTRA_ESTILO)

    label_xstar = MathTex(r"x_" + str(i) + r"^*")
    label_xstar.scale(0.65)
    label_xstar.next_to(dot_xstar, DOWN, buff=0.06)

    h_line = Line(ax.c2p(x_star, 0), ax.c2p(x_star, y_star), **P.ALTURA_ESTILO)

    return {
        "dot": dot_xstar,
        "label_xstar": label_xstar,
        "h_line": h_line,
    }


def crear_rectangulos_grupo(ax, n, criterio="midpoint", opacity=None):
    rects = VGroup()
    dx = (P.B - P.A) / n

    estilo_rect = P.RECTANGULOS_ESTILO.copy()
    if opacity is not None:
        estilo_rect["fill_opacity"] = opacity

    for i in range(1, n + 1):
        x_left = P.A + (i - 1) * dx
        x_right = P.A + i * dx
        x_star = punto_muestra(x_left, x_right, criterio)
        y_star = P.F(x_star)
        rects.add(crear_rectangulo(ax, x_left, x_right, y_star, estilo_rect))

    return rects


def valor_suma_riemann(n, criterio="midpoint"):
    dx = (P.B - P.A) / n
    total = 0
    for i in range(1, n + 1):
        x_left = P.A + (i - 1) * dx
        x_right = P.A + i * dx
        total += P.F(punto_muestra(x_left, x_right, criterio)) * dx
    return total
