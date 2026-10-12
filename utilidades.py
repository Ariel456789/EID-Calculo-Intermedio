"""
utilidades.py - Funciones auxiliares reutilizables por las escenas.

Se separan aquí para no repetir código en cada escena y para poder
explicarlas por separado en la defensa (por ejemplo, cómo se construye
un rectángulo alineado a los ejes con c2p).

Depende de parametros.py (función F, intervalo A-B, estilos).
"""

from manim import *
import parametros as P


# =============================================================================
# Grilla y curva
# =============================================================================

def crear_ejes_y_curva():
    """
    Crea los ejes, sus etiquetas y la curva f(x).
    Retorna: (ax, ax_labels, curva)
    """
    ax = Axes(**P.AXES_CONFIG)
    # Bajamos los ejes ANTES de crear etiquetas y curva, para que todo
    # (etiquetas, curva y los c2p posteriores) quede alineado.
    ax.shift(P.AXES_VERTICAL_SHIFT)
    ax_labels = ax.get_axis_labels(*P.AXES_LABELS)
    curva = ax.plot(P.F, x_range=[P.A, P.B], **P.CURVA_ESTILO)
    return ax, ax_labels, curva


# =============================================================================
# Punto muestra y rectángulos
# =============================================================================

def punto_muestra(x_left, x_right, criterio="midpoint"):
    """
    Devuelve el punto muestra x_i^* del subintervalo [x_left, x_right].

    criterio: "left" (extremo izq.), "right" (extremo der.)
              o "midpoint" (punto medio, por defecto).
    """
    if criterio == "left":
        return x_left
    if criterio == "right":
        return x_right
    return (x_left + x_right) / 2


def crear_rectangulo(ax, x_left, x_right, y_top, estilo=None):
    """
    Construye un rectángulo alineado exactamente a los ejes usando sus
    4 esquinas convertidas con ax.c2p (coordenadas gráfico -> pantalla).
    """
    estilo = estilo or P.RECTANGULO_DESTACADO_ESTILO
    return Polygon(
        ax.c2p(x_left, 0),
        ax.c2p(x_right, 0),
        ax.c2p(x_right, y_top),
        ax.c2p(x_left, y_top),
        **estilo,
    )


def crear_elementos_muestra(ax, i, x_star, y_star):
    """
    Crea los objetos que acompañan a un rectángulo:
    el punto x_i^* (sobre el eje), su etiqueta bajo el eje,
    y la altura f(x_i^*) como una línea verde.

    El texto f(x_i^*)Δx se ubica aparte, DENTRO del rectángulo
    (ver la escena SumaRiemannConstruccion), para no chocar con la curva.
    Retorna un dict con esos mobjects.
    """
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
    """
    Crea un VGroup con los n rectángulos de la suma de Riemann.
    Útil para el refinamiento (n = 4, 8, 16, 32).
    """
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


# =============================================================================
# Cálculo numérico de apoyo
# =============================================================================

def valor_suma_riemann(n, criterio="midpoint"):
    """
    Valor numérico de la suma de Riemann:
        S_n = suma_i f(x_i^*) * Δx
    Sirve de apoyo para mostrar el número en pantalla.
    """
    dx = (P.B - P.A) / n
    total = 0
    for i in range(1, n + 1):
        x_left = P.A + (i - 1) * dx
        x_right = P.A + i * dx
        total += P.F(punto_muestra(x_left, x_right, criterio)) * dx
    return total
