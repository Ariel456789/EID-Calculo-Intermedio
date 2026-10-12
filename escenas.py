"""
escenas.py - Las escenas del video del Grupo 4, en orden.

MAPA DEL VIDEO  (sección de la pauta -> escena -> concepto)
--------------------------------------------------------------------
    1. Teoría (planteamiento)     -> RegionInicial
    2. Teoría (partición)         -> ParticionInicial
    3. Ejemplo propio             -> SumaRiemannConstruccion
    4. Refinamiento (CLAVE)       -> RefinamientoProgresivo
    5. Conexión suma -> integral  -> TransicionSumaIntegral
    6. El límite (CLAVE)          -> LimiteProceso
    7. Respuesta + cierre         -> RespuestaPreguntaCentral
    (pendiente) Presentación      -> Presentacion
    (pendiente) Créditos/fuentes  -> Creditos
--------------------------------------------------------------------

Los parámetros matemáticos y de estilo están en parametros.py.
Las funciones auxiliares están en utilidades.py.
"""

from manim import *
import parametros as P
import utilidades as U


# =============================================================================
# SECCIÓN 1 - Teoría: planteamiento del problema
# =============================================================================

class RegionInicial(Scene):
    """
    QUÉ MUESTRA : la región bajo f(x) en [a, b], sombreada.
    CONCEPTO    : el problema del área; por qué conviene aproximar.
    PARÁMETROS  : A, B, F (parametros.py).
    """

    def construct(self):
        titulo = Tex("Del símbolo de sumatoria al símbolo de integral")
        titulo.scale(P.TITULO_ESCALA)
        subtitulo = Tex("Grupo 4 - Eje 4")
        subtitulo.scale(P.SUBTITULO_ESCALA)
        subtitulo.next_to(titulo, DOWN)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo))
        self.wait(1.5)
        self.play(FadeOut(titulo, subtitulo))

        ax, ax_labels, curva = U.crear_ejes_y_curva()

        self.play(Create(ax), Write(ax_labels))
        self.play(Create(curva))
        self.wait(0.5)

        region = ax.get_area(curva, x_range=[P.A, P.B], color=BLUE, opacity=0.15)
        texto_region = Tex("Región bajo la curva en $[a,b]$")
        texto_region.scale(P.TEX_ESCALA)
        texto_region.to_edge(UP)

        self.play(FadeIn(region), Write(texto_region))
        self.wait(2)

        pregunta = Tex(r"¿Cómo aproximamos esta región con rectángulos?")
        pregunta.scale(P.TITULO_ESCALA)
        pregunta.to_edge(DOWN)

        self.play(Write(pregunta))
        self.wait(3)

        self.play(FadeOut(region, texto_region, pregunta, curva, ax, ax_labels))


# =============================================================================
# SECCIÓN 2 - Teoría: partición del intervalo
# =============================================================================

class ParticionInicial(Scene):
    """
    QUÉ MUESTRA : la división de [a, b] en n subintervalos con ancho Δx.
    CONCEPTO    : partición, n, Δx = (b-a)/n, los puntos x_i.
    PARÁMETROS  : A, B, N_INICIAL.
    """

    def construct(self):
        n = P.N_INICIAL
        dx = (P.B - P.A) / n

        ax, ax_labels, curva = U.crear_ejes_y_curva()
        self.add(ax, ax_labels, curva)

        titulo = Tex(r"Partición del intervalo $[a,b]$ en $n$ subintervalos")
        titulo.scale(P.TITULO_ESCALA)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        # Líneas de partición
        particion_lines = VGroup()
        for i in range(n + 1):
            x = P.A + i * dx
            particion_lines.add(
                ax.get_vertical_line(ax.c2p(x, P.F(x)), **P.LINEAS_MUESTRA_ESTILO)
            )

        self.play(Create(particion_lines), run_time=1.5)
        self.wait(0.5)

        # Ancho Δx
        p0 = ax.c2p(P.A, 0)
        p1 = ax.c2p(P.A + dx, 0)
        flecha_dx = DoubleArrow(p0, p1, color=YELLOW, buff=0)
        tex_dx = MathTex(r"\Delta x = \frac{b-a}{n}")
        tex_dx.scale(P.TEX_ESCALA)
        tex_dx.next_to(flecha_dx, UP, buff=0.15)

        self.play(Create(flecha_dx), Write(tex_dx))
        self.wait(2)

        tex_part = MathTex(r"a = x_0 < x_1 < \cdots < x_i < \cdots < x_n = b")
        tex_part.scale(P.TEX_ESCALA)
        tex_part.to_edge(DOWN)
        self.play(Write(tex_part))
        self.wait(3)

        self.play(
            FadeOut(
                titulo, particion_lines, flecha_dx, tex_dx,
                tex_part, curva, ax, ax_labels,
            )
        )


# =============================================================================
# SECCIÓN 3 - Ejemplo propio: construcción de la suma de Riemann
# =============================================================================

class SumaRiemannConstruccion(Scene):
    """
    QUÉ MUESTRA : rectángulo a rectángulo, x_i^*, f(x_i^*) y el aporte f(x_i^*)Δx.
    CONCEPTO    : la suma de Riemann S_n = Σ f(x_i^*) Δx (punto medio).
    PARÁMETROS  : A, B, N_INICIAL, F.
    """

    def construct(self):
        n = P.N_INICIAL
        dx = (P.B - P.A) / n

        ax, ax_labels, curva = U.crear_ejes_y_curva()
        self.add(ax, ax_labels, curva)

        titulo = Tex(r"Suma de Riemann: $\sum_{i=1}^{n} f(x_i^*)\,\Delta x$")
        titulo.scale(P.TITULO_ESCALA)
        titulo.to_edge(UP, buff=P.TITULO_BUFF)
        self.play(Write(titulo))
        self.wait(0.5)

        # Grupo con todo lo que se construye (para desvanecerlo junto al final)
        contenido = VGroup()

        for i in range(1, n + 1):
            x_left = P.A + (i - 1) * dx
            x_right = P.A + i * dx
            x_star = U.punto_muestra(x_left, x_right, "midpoint")
            y_star = P.F(x_star)

            rect = U.crear_rectangulo(ax, x_left, x_right, y_star)
            elems = U.crear_elementos_muestra(ax, i, x_star, y_star)

            # El aporte f(x_i^*)Δx va DENTRO del rectángulo (no encima),
            # así nunca se superpone con la curva.
            term = MathTex(r"f(x_" + str(i) + r"^*)\,\Delta x")
            term.scale(0.5)
            term.move_to(rect.get_center())

            self.play(Create(rect), run_time=0.4)
            self.play(FadeIn(elems["dot"], elems["label_xstar"]), run_time=0.2)
            self.play(Create(elems["h_line"]), run_time=0.2)
            self.play(Write(term), run_time=0.35)
            self.wait(0.15)

            contenido.add(
                rect,
                elems["dot"], elems["label_xstar"], elems["h_line"],
                term,
            )

        self.wait(1.5)

        # Fórmula completa + valor numérico
        valor = U.valor_suma_riemann(n, "midpoint")
        suma_total = MathTex(
            r"S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x \approx "
            + f"{valor:.4f}"
        )
        suma_total.scale(P.MATH_TEX_ESCALA)
        suma_total.to_edge(DOWN, buff=0.4)

        self.play(Write(suma_total))
        self.wait(3)

        self.play(FadeOut(titulo, contenido, ax, ax_labels, curva, suma_total))


# =============================================================================
# SECCIÓN 4 - Refinamiento progresivo (CLAVE)
# =============================================================================

class RefinamientoProgresivo(Scene):
    """
    QUÉ MUESTRA : la misma región con n = 4, 8, 16, 32.
    CONCEPTO    : al aumentar n, Δx -> 0 y la aproximación mejora.
    PARÁMETROS  : A, B, REFINAMIENTO_N_LIST.
    """

    def construct(self):
        ax, ax_labels, curva = U.crear_ejes_y_curva()
        self.add(ax, ax_labels, curva)

        titulo = Tex(r"Refinamiento: $n \uparrow \;\Rightarrow\; \Delta x \downarrow$")
        titulo.scale(P.TEX_ESCALA)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        for n in P.REFINAMIENTO_N_LIST:
            dx = (P.B - P.A) / n
            rects = U.crear_rectangulos_grupo(ax, n, "midpoint", opacity=0.35)

            info = MathTex(
                r"n = " + str(n) + r",\quad \Delta x = \frac{3}{"
                + str(n) + r"} = " + f"{dx:.4f}"
            )
            info.scale(P.TEX_ESCALA)
            info.to_edge(DOWN)

            self.play(FadeIn(rects), Write(info), run_time=1.2)
            self.wait(1.2)
            self.play(FadeOut(rects, info), run_time=0.6)

        concl1 = Tex(r"Al aumentar $n$, los rectángulos se hacen más estrechos")
        concl2 = Tex(r"La aproximación a la región mejora progresivamente")
        concl1.scale(P.TEX_ESCALA)
        concl2.scale(P.TEX_ESCALA)
        concl1.next_to(curva, UP, buff=0.4)
        concl2.next_to(concl1, DOWN, buff=0.15)

        self.play(Write(concl1))
        self.play(Write(concl2))
        self.wait(2.5)

        self.play(FadeOut(titulo, concl1, concl2, curva, ax, ax_labels))


# =============================================================================
# SECCIÓN 5 - Conexión suma -> integral (CLAVE)
# =============================================================================

class TransicionSumaIntegral(Scene):
    r"""
    QUÉ MUESTRA : la transformación de Σ f(x_i^*) Δx en ∫ f(x) dx.
    CONCEPTO    : paso de lo discreto (suma finita) a lo continuo (integral):
                  Σ -> ∫ , f(x_i^*) -> f(x) , Δx -> dx.
    PARÁMETROS  : (simbólico; no usa datos numéricos).
    """

    def construct(self):
        titulo = Tex(r"De la suma finita a la integral definida")
        titulo.scale(P.TITULO_ESCALA)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        # Fórmula por partes (permite resaltar cada símbolo)
        parte_sn = MathTex("S_n =")
        parte_suma = MathTex(r"\sum_{i=1}^{n}")
        parte_f = MathTex(r"f(x_i^*)")
        parte_dx = MathTex(r"\Delta x")
        formula = VGroup(parte_sn, parte_suma, parte_f, parte_dx).arrange(RIGHT, buff=0.12)
        formula.scale(P.FORMULA_GRANDE_ESCALA)
        formula.shift(UP * 0.8)

        self.play(Write(formula))
        self.wait(1.2)

        # Resaltar Σ
        box1 = SurroundingRectangle(parte_suma, color=YELLOW, buff=0.08)
        label1 = Tex(r"$\sum$: suma discreta (finita)")
        label1.scale(P.TEX_ESCALA)
        label1.next_to(box1, UP, buff=0.15).set_color(YELLOW)
        self.play(Create(box1), Write(label1))
        self.wait(1.2)
        self.play(FadeOut(box1, label1))

        # Resaltar f(x_i^*)
        box2 = SurroundingRectangle(parte_f, color=ORANGE, buff=0.08)
        label2 = Tex(r"$f(x_i^*)$: valor representativo del subintervalo")
        label2.scale(P.TEX_ESCALA)
        label2.next_to(box2, UP, buff=0.15).set_color(ORANGE)
        self.play(Create(box2), Write(label2))
        self.wait(1.2)
        self.play(FadeOut(box2, label2))

        # Resaltar Δx
        box3 = SurroundingRectangle(parte_dx, color=GREEN, buff=0.08)
        label3 = Tex(r"$\Delta x$: ancho de cada rectángulo")
        label3.scale(P.TEX_ESCALA)
        label3.next_to(box3, UP, buff=0.15).set_color(GREEN)
        self.play(Create(box3), Write(label3))
        self.wait(1.2)
        self.play(FadeOut(box3, label3))

        # Transformación a la integral
        integral_tex = MathTex(r"\int_{a}^{b} f(x)\,dx")
        integral_tex.scale(P.FORMULA_GRANDE_ESCALA)
        self.play(ReplacementTransform(formula, integral_tex))
        self.wait(1.5)

        # Mapeo de símbolos (responde la pregunta central)
        mapeo = Tex(
            r"$\sum_{i=1}^{n} \;\longmapsto\; \int_{a}^{b}$, \quad "
            r"$f(x_i^*) \;\longmapsto\; f(x)$, \quad "
            r"$\Delta x \;\longmapsto\; dx$"
        )
        mapeo.scale(P.MAPEO_ESCALA)
        mapeo.next_to(integral_tex, DOWN, buff=0.9)
        self.play(Write(mapeo))
        self.wait(3)

        self.play(FadeOut(titulo, integral_tex, mapeo))


# =============================================================================
# SECCIÓN 6 - El límite como proceso (CLAVE)
# =============================================================================

class LimiteProceso(Scene):
    """
    QUÉ MUESTRA : la definición integral = lim(n→∞) Σ f(x_i^*)Δx.
    CONCEPTO    : n→∞ es un proceso, no un valor que se sustituya; Δx→0.
    PARÁMETROS  : (simbólico; no usa datos numéricos).
    """

    def construct(self):
        titulo = Tex(r"El papel del límite: $n \to +\infty$, \quad $\Delta x \to 0$")
        titulo.scale(P.TITULO_ESCALA)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        limite_tex = MathTex(
            r"\int_{a}^{b} f(x)\,dx = \lim_{n\to\infty}"
            r"\left(\sum_{i=1}^{n} f(x_i^*)\,\Delta x\right)"
        )
        limite_tex.scale(P.MATH_TEX_ESCALA)
        self.play(Write(limite_tex))
        self.wait(2)

        idea1 = Tex(r"$n \to \infty$ describe un \textbf{proceso}, no un valor que se sustituye")
        idea2 = Tex(r"$\Delta x = \frac{b-a}{n} \to 0$ cuando la partición se hace más fina")
        idea3 = Tex(r"El error disminuye a medida que refinamos la partición")
        for idea in (idea1, idea2, idea3):
            idea.scale(P.TEX_ESCALA)

        idea1.next_to(limite_tex, DOWN, buff=0.6)
        idea2.next_to(idea1, DOWN, buff=0.25)
        idea3.next_to(idea2, DOWN, buff=0.25)

        self.play(Write(idea1))
        self.wait(1.8)
        self.play(Write(idea2))
        self.wait(1.8)
        self.play(Write(idea3))
        self.wait(2.5)

        self.play(FadeOut(titulo, limite_tex, idea1, idea2, idea3))


# =============================================================================
# SECCIÓN 7 - Respuesta explícita a la pregunta central
# =============================================================================

class RespuestaPreguntaCentral(Scene):
    """
    QUÉ MUESTRA : la respuesta en 5 pasos y la conclusión final.
    CONCEPTO    : conexión suma finita -> límite -> integral definida.
    PARÁMETROS  : (simbólico; no usa datos numéricos).
    """

    def construct(self):
        pregunta = Tex(
            r"Pregunta central: ¿cómo pasamos de una suma con un número \\ "
            r"finito de rectángulos a una integral definida?"
        )
        pregunta.scale(P.TEX_ESCALA)
        pregunta.to_edge(UP)
        self.play(Write(pregunta))
        self.wait(1.2)

        pasos = [
            r"1. Partimos de una suma de Riemann finita: $S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x$",
            r"2. Refinamos la partición: aumentamos $n$ indefinidamente",
            r"3. Entonces $\Delta x \to 0$ y los rectángulos se ajustan mejor a la curva",
            r"4. Tomamos el límite: $\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^*)\,\Delta x$",
            r"5. Ese límite define la integral definida: $\int_{a}^{b} f(x)\,dx$",
        ]
        pasos_mobs = VGroup(*[Tex(p) for p in pasos])
        pasos_mobs.scale(0.72)
        pasos_mobs.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        pasos_mobs.next_to(pregunta, DOWN, buff=0.5)

        for mob in pasos_mobs:
            self.play(Write(mob), run_time=0.8)
            self.wait(0.6)

        concl = Tex(
            r"Así pasamos del \textbf{discreto} (suma finita) al "
            r"\textbf{continuo} (integral definida)."
        )
        concl.scale(P.TITULO_ESCALA)
        concl.to_edge(DOWN, buff=0.5)
        self.play(Write(concl))
        self.wait(3)

        self.play(FadeOut(pregunta, pasos_mobs, concl))
