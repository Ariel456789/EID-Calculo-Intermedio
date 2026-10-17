"""Escenas del EID Grupo 4 (Manim Community).

Storyboard: guion_storyboard_EID_G04_v2.tex. El video base no incluye audio:
las pausas están previstas para sincronizar narración propia al editar el MP4.

Concepto central: la integral definida es el LIMITE de sumas de Riemann;
no se obtiene sustituyendo símbolos de manera individual.
"""

from manim import *
import parametros as P
import utilidades as U

# Texto visible intencionalmente breve: la explicación completa será oral.
TEXTO = "DejaVu Sans"
COLOR_BASE = WHITE
AZUL = BLUE_C
NARANJA = ORANGE
VERDE = GREEN_C
DORADO = YELLOW


def texto(cadena, tam=29, color=COLOR_BASE):
    obj = Text(cadena, font=TEXTO, font_size=tam, color=color)
    if obj.width > 12.4:
        obj.scale_to_fit_width(12.4)
    return obj


def encabezado(cadena):
    obj = texto(cadena, tam=31)
    obj.to_edge(UP, buff=0.34)
    return obj


def matematica(cadena, escala=0.9):
    obj = MathTex(cadena).scale(escala)
    if obj.width > 12.4:
        obj.scale_to_fit_width(12.4)
    return obj


def pie(obj):
    obj.to_edge(DOWN, buff=0.37)
    return obj


def plano(funcion=True, lado_izquierdo=True):
    """Ejes con escala consistente; se reserva espacio para fórmulas a la derecha."""
    ax = Axes(**P.AXES_CONFIG)
    ax.shift(LEFT * (2.35 if lado_izquierdo else 0) + DOWN * 0.4)
    etiquetas = ax.get_axis_labels(x_label="x", y_label="f(x)")
    curva = ax.plot(P.F, x_range=[P.A, P.B], **P.CURVA_ESTILO) if funcion else VGroup()
    return ax, etiquetas, curva


def estado_limpio(escena, tiempo=0.55):
    if escena.mobjects:
        escena.play(FadeOut(*escena.mobjects), run_time=tiempo)


def indicador_rectangulo(ax, izq, der, altura, color=NARANJA, opacidad=0.38):
    return Polygon(
        ax.c2p(izq, 0), ax.c2p(der, 0), ax.c2p(der, altura), ax.c2p(izq, altura),
        stroke_color=color, stroke_width=1.3, fill_color=color,
        fill_opacity=opacidad,
    )


def pausa(escena, segundos):
    """Espacio de locución; modificable globalmente en parametros.py."""
    escena.wait(segundos * P.FACTOR_PAUSAS)


# ---------------------------------------------------------
# 1. Presentación obligatoria (confirmar integrantes antes del render final)
# ---------------------------------------------------------
class Presentacion(Scene):
    def construct(self):
        self.play(Write(texto("Cálculo Intermedio · EID · Grupo 4", 32).shift(UP * 2.8)), run_time=1.5)
        tema = texto("Del símbolo de sumatoria\nal símbolo de integral", 43, AZUL)
        self.play(FadeIn(tema, shift=UP * 0.25), run_time=1.1)
        pregunta = texto("¿Cómo pasamos de una suma con un número finito\nde rectángulos a una integral definida?", 25)
        pregunta.next_to(tema, DOWN, buff=0.65)
        self.play(Write(pregunta), run_time=1.4)
        integrantes = texto(P.TEXTO_INTEGRANTES, 20, GRAY_B)
        integrantes.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(integrantes), run_time=0.8)
        pausa(self, 5.5)
        estado_limpio(self)


# ---------------------------------------------------------
# 2. Motivación: un automóvil a rapidez constante
# ---------------------------------------------------------
class AutoVelocidadConstante(Scene):
    def construct(self):
        self.add(encabezado("Una rapidez constante: un área fácil de calcular"))
        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 8, 2], x_length=7, y_length=3.7,
            axis_config={"include_tip": True, "stroke_width": 2},
        ).shift(LEFT * 2.35 + DOWN * 0.28)
        etiquetas = VGroup(
            matematica(r"t\ (\mathrm{s})", 0.7).next_to(ax.x_axis, RIGHT, buff=0.15),
            matematica(r"v\ (\mathrm{m/s})", 0.65).next_to(ax.y_axis, UP, buff=0.1),
        )
        rect = indicador_rectangulo(ax, 0, 5, 6, color=AZUL, opacidad=0.32)
        linea = Line(ax.c2p(0, 6), ax.c2p(5, 6), color=VERDE, stroke_width=4)
        self.play(Create(ax), FadeIn(etiquetas), run_time=1.8)
        self.play(Create(linea), run_time=1.3)
        self.play(FadeIn(rect), run_time=1.2)
        info = VGroup(
            matematica(r"v=6\ \mathrm{m/s}", 0.85),
            matematica(r"\Delta t=5\ \mathrm{s}", 0.85),
            matematica(r"d=v\,\Delta t", 0.92),
            matematica(r"d=30\ \mathrm{m}", 1.05).set_color(DORADO),
        ).arrange(DOWN, buff=0.38).move_to(RIGHT * 3.8 + DOWN * 0.06)
        for elemento in info:
            self.play(Write(elemento), run_time=0.8)
            pausa(self, 1.3)
        self.play(Write(pie(texto("Área del rectángulo = distancia recorrida", 25))), run_time=1.1)
        pausa(self, 4.0)
        estado_limpio(self)


# ---------------------------------------------------------
# 3. Motivación: ¿qué ocurre si la rapidez varía?
# ---------------------------------------------------------
class AutoVelocidadVariable(Scene):
    def construct(self):
        self.add(encabezado("¿Y si la rapidez cambia durante el recorrido?"))
        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 12, 2], x_length=7.4, y_length=3.8,
            axis_config={"include_tip": True, "stroke_width": 2},
        ).shift(DOWN * 0.38)
        curva = ax.plot(lambda t: 2 + 0.35 * t * t, x_range=[0, 5], color=VERDE, stroke_width=4)
        relleno = ax.get_area(curva, x_range=[0, 5], color=AZUL, opacity=0.24)
        txt = texto("La rapidez ya no es una única altura", 25)
        pie(txt)
        self.play(Create(ax), run_time=1.5)
        self.play(Create(curva), run_time=1.9)
        self.play(FadeIn(relleno), Write(txt), run_time=1.5)
        pausa(self, 3.5)
        self.play(FadeOut(txt))
        # Cuatro rectángulos ilustrativos: sin convertir el automóvil en otro ejemplo principal.
        rects = VGroup()
        for i in range(4):
            x0, x1 = i * 1.25, (i + 1) * 1.25
            tm = (x0 + x1) / 2
            rects.add(indicador_rectangulo(ax, x0, x1, 2 + 0.35 * tm * tm, NARANJA, 0.26))
        self.play(LaggedStart(*[FadeIn(r) for r in rects], lag_ratio=0.15), run_time=2.0)
        self.play(Write(pie(texto("Aproximar por intervalos y sumar aportes", 26, DORADO))), run_time=1.1)
        pausa(self, 4.5)
        estado_limpio(self)


# ---------------------------------------------------------
# 4. Se establece el ejemplo matemático principal.
# ---------------------------------------------------------
class RegionInicial(Scene):
    def construct(self):
        self.add(encabezado("Nuestro ejemplo: una región bajo una curva"))
        ax, etiquetas, curva = plano(lado_izquierdo=True)
        relleno = ax.get_area(curva, x_range=[P.A, P.B], color=AZUL, opacity=0.3)
        guia_a = DashedLine(ax.c2p(P.A, 0), ax.c2p(P.A, P.F(P.A)), color=GRAY_B)
        guia_b = DashedLine(ax.c2p(P.B, 0), ax.c2p(P.B, P.F(P.B)), color=GRAY_B)
        self.play(Create(ax), FadeIn(etiquetas), run_time=1.1)
        self.play(Create(curva), FadeIn(relleno), Create(guia_a), Create(guia_b), run_time=2.1)
        derecha = VGroup(
            matematica(r"f(x)=\frac12(x-1)^2+1", 0.92),
            matematica(r"[a,b]=[0,3]", 0.92),
            texto("Continua y positiva", 24, VERDE),
        ).arrange(DOWN, buff=0.6).move_to(RIGHT * 3.6 + UP * 0.05)
        self.play(LaggedStart(*[Write(e) for e in derecha], lag_ratio=0.2), run_time=3.2)
        self.play(Write(pie(texto("Buscamos el área exacta, empezando por aproximaciones", 24))), run_time=1.0)
        pausa(self, 5.8)
        estado_limpio(self)


# ---------------------------------------------------------
# 5. Partición, ancho de cada subintervalo y punto muestra
# ---------------------------------------------------------
class ParticionInicial(Scene):
    def construct(self):
        self.add(encabezado("Dividimos el intervalo en cuatro partes"))
        ax, etiquetas, curva = plano(lado_izquierdo=True)
        self.add(ax, etiquetas, curva)
        dx = (P.B-P.A)/P.N_INICIAL
        divisiones = VGroup()
        for i in range(P.N_INICIAL + 1):
            xi = P.A + i*dx
            divisiones.add(DashedLine(ax.c2p(xi, 0), ax.c2p(xi, P.F(xi)), color=GRAY_B))
        self.play(Create(divisiones), run_time=2.0)
        p1, p2 = ax.c2p(P.A, -0.1), ax.c2p(P.A + dx, -0.1)
        marcador = DoubleArrow(p1, p2, buff=0, color=DORADO, stroke_width=3, tip_length=0.15)
        self.play(Create(marcador), run_time=1)
        lateral = VGroup(
            matematica(r"n=4", 0.94),
            matematica(r"\Delta x=\frac{b-a}{n}", 0.98),
            matematica(r"\Delta x=\frac{3-0}{4}=\frac34", 0.93).set_color(DORADO),
        ).arrange(DOWN, buff=0.58).move_to(RIGHT * 3.6)
        for e in lateral:
            self.play(Write(e), run_time=0.9)
            pausa(self, 1.2)
        self.play(Write(pie(texto("Cada rectángulo tendrá base Δx", 24))), run_time=1.0)
        pausa(self, 5)
        estado_limpio(self)


# ---------------------------------------------------------
# 6. Suma S4 con puntos medios: parte que no debe quedarse como opcional
# ---------------------------------------------------------
class SumaRiemannConstruccion(Scene):
    def construct(self):
        self.add(encabezado("Elegimos puntos medios y construimos la suma"))
        ax, etiquetas, curva = plano(lado_izquierdo=True)
        self.add(ax, etiquetas, curva)
        n = P.N_INICIAL
        dx = (P.B - P.A) / n

        # ETAPA 1: puntos muestra y rectángulos (sin fórmulas que se superpongan).
        formula_m = matematica(r"x_i^*=\left(i-\frac12\right)\Delta x", 0.84)
        formula_m.move_to(RIGHT * 3.52 + UP * 1.55)
        self.play(Write(formula_m), run_time=1.6)

        puntos = matematica(r"\frac38,\ \frac98,\ \frac{15}8,\ \frac{21}8", 0.82)
        puntos.move_to(RIGHT * 3.52 + UP * 0.45)
        self.play(Write(puntos), run_time=1.4)

        for i in range(1, n + 1):
            x_left, x_right = P.A + (i - 1) * dx, P.A + i * dx
            xstar = U.punto_muestra(x_left, x_right)
            rect = indicador_rectangulo(ax, x_left, x_right, P.F(xstar))
            marcador = Dot(ax.c2p(xstar, P.F(xstar)), color=DORADO, radius=0.065)
            self.play(FadeIn(rect), FadeIn(marcador), run_time=0.95)
            pausa(self, 1.2)

        aporte = matematica(r"A_i=f(x_i^*)\,\Delta x", 0.92)
        aporte.move_to(RIGHT * 3.52 + DOWN * 0.95)
        self.play(Write(aporte), run_time=1.2)
        pausa(self, 2.5)

        # ETAPA 2: limpiar la columna antes de desarrollar S_4.
        self.play(FadeOut(formula_m), FadeOut(puntos), FadeOut(aporte), run_time=0.65)
        sum_line1 = matematica(
            r"S_4=\frac34\left[f\left(\frac38\right)+f\left(\frac98\right)\right.",
            0.78,
        )
        sum_line2 = matematica(
            r"\left.\qquad+f\left(\frac{15}8\right)+f\left(\frac{21}8\right)\right]",
            0.78,
        )
        desarrollo = VGroup(sum_line1, sum_line2).arrange(DOWN, buff=0.30)
        if desarrollo.width > 5.65:
            desarrollo.scale_to_fit_width(5.65)
        # Centro de la columna derecha; la separación es relativa al objeto completo.
        desarrollo.move_to(RIGHT * 3.55 + UP * 0.37)
        self.play(Write(desarrollo), run_time=3.4)
        pausa(self, 4.5)

        # ETAPA 3: al calcular el resultado ya no se conserva la expresión larga.
        resultado = matematica(r"S_4=\frac{567}{128}\approx4{,}4297", 1.05).set_color(DORADO)
        resultado.move_to(RIGHT * 3.55 + DOWN * 0.35)
        self.play(FadeOut(desarrollo), FadeIn(resultado), run_time=1.2)
        pausa(self, 5.8)
        estado_limpio(self)


# ---------------------------------------------------------
# 7. Mismo intervalo, n crece, tabla de valores numéricos
# ---------------------------------------------------------
class RefinamientoProgresivo(Scene):
    def construct(self):
        self.add(encabezado("Refinar: aumentar n y disminuir Δx"))
        ax, etiquetas, curva = plano(lado_izquierdo=True)
        self.add(ax, etiquetas, curva)
        dato_ancho = matematica(r"\Delta x=\frac{3}{n}", 1.0)
        dato_ancho.move_to(RIGHT * 3.5 + UP * 1.7)
        self.add(dato_ancho)
        valor_anterior = None
        rects_anteriores = None
        for n in P.REFINAMIENTO_N_LIST:
            rects = U.crear_rectangulos_grupo(ax, n, criterio="midpoint", opacity=0.28)
            valor = U.valor_suma_riemann(n, "midpoint")
            ficha = VGroup(
                matematica(r"n="+str(n), 0.95),
                matematica(r"\Delta x=\frac{3}{"+str(n)+r"}", 0.82),
                matematica(r"S_{"+str(n)+r"}\approx"+f"{valor:.5f}", 0.9),
            ).arrange(DOWN, buff=0.35).move_to(RIGHT * 3.52 + DOWN * 0.38)
            if rects_anteriores is None:
                self.play(FadeIn(rects), FadeIn(ficha), run_time=1.3)
            else:
                self.play(ReplacementTransform(rects_anteriores, rects),
                          ReplacementTransform(valor_anterior, ficha), run_time=1.8)
            pausa(self, 5.2)
            rects_anteriores, valor_anterior = rects, ficha
        self.play(Write(pie(texto("Las sumas se acercan a 4,5", 28, DORADO))), run_time=1)
        pausa(self, 4.2)
        estado_limpio(self)


# ---------------------------------------------------------
# 8. Algebra esencial del ejemplo: usar identidades sin saturar pantalla
# ---------------------------------------------------------
class CalculoGeneral(Scene):
    def construct(self):
        self.add(encabezado("De cuatro rectángulos a cualquier n"))

        # PASO 1. La regla del punto medio, para cualquier n.
        subtitulo = texto("La misma regla de puntos medios sirve para cualquier n", 24)
        subtitulo.move_to(UP * 2.20)
        self.play(Write(subtitulo), run_time=1.2)
        general = matematica(r"x_i^*=\left(i-\frac12\right)\frac3n", 1.16)
        general.move_to(DOWN * 0.10)
        self.play(Write(general), run_time=1.7)
        pausa(self, 3.7)

        # PASO 2. Suma general. Reemplaza el paso anterior, no lo apila.
        summ = matematica(r"S_n=\sum_{i=1}^{n}f(x_i^*)\frac3n", 1.17)
        summ.move_to(DOWN * 0.10)
        self.play(ReplacementTransform(general, summ), run_time=1.7)
        pausa(self, 4.2)

        # PASO 3. Identidades en su propia pantalla. Sin sumatoria grande encima.
        subtitulo2 = texto("Aplicamos dos identidades de sumatorias", 25)
        subtitulo2.move_to(UP * 2.20)
        self.play(FadeOut(summ), ReplacementTransform(subtitulo, subtitulo2), run_time=0.85)
        identidad1 = matematica(r"\sum_{i=1}^{n}i=\frac{n(n+1)}2", 1.00)
        identidad2 = matematica(r"\sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}6", 0.98)
        identidad1.move_to(UP * 0.70)
        identidad2.move_to(DOWN * 0.88)
        self.play(Write(identidad1), run_time=1.9)
        self.play(Write(identidad2), run_time=2.0)
        pausa(self, 3.0)

        # PASO 4. Resultado intermedio útil para comprender el desarrollo en LaTeX.
        subtitulo3 = texto("Aplicadas a los puntos medios, obtenemos", 24)
        subtitulo3.move_to(UP * 2.20)
        intermedia = matematica(r"\sum_{i=1}^{n}\left(i-\frac12\right)^2=\frac{4n^3-n}{12}", 1.00)
        intermedia.move_to(DOWN * 0.05)
        self.play(FadeOut(identidad1), FadeOut(identidad2),
                  ReplacementTransform(subtitulo2, subtitulo3), run_time=0.9)
        self.play(Write(intermedia), run_time=1.8)
        pausa(self, 2.6)

        # PASO 5. Resultado general, una sola expresión bien centrada.
        resultado = matematica(r"S_n=\frac92-\frac{9}{8n^2}", 1.35).set_color(DORADO)
        resultado.move_to(DOWN * 0.10)
        self.play(FadeOut(intermedia), FadeOut(subtitulo3), FadeIn(resultado), run_time=1.9)
        pausa(self, 5.6)
        estado_limpio(self)


# ---------------------------------------------------------
# 9. Límite calculado: no se sustituye n por infinito
# ---------------------------------------------------------
class LimiteProceso(Scene):
    def construct(self):
        self.add(encabezado("El límite de las sumas"))
        fila1 = matematica(r"n\to\infty\qquad \Delta x=\frac3n\to 0", 0.98)
        fila1.shift(UP * 1.75)
        self.play(Write(fila1), run_time=1.8)
        pausa(self, 2.0)
        fila2 = matematica(r"\lim_{n\to\infty}S_n=\lim_{n\to\infty}\left(\frac92-\frac{9}{8n^2}\right)", 1.0)
        self.play(Write(fila2), run_time=2.2)
        pausa(self, 5.0)
        fila3 = matematica(r"\frac{9}{8n^2}\to0\qquad\Longrightarrow\qquad\lim_{n\to\infty}S_n=\frac92", 0.93)
        fila3.next_to(fila2, DOWN, buff=0.75)
        self.play(Write(fila3), run_time=1.9)
        pausa(self, 5.2)
        self.play(Write(pie(texto("El límite es el valor exacto al que convergen las sumas", 23, DORADO))), run_time=1)
        pausa(self, 4.1)
        estado_limpio(self)


# ---------------------------------------------------------
# 10. Relación real suma–límite–integral (corrige el reemplazo anterior)
# ---------------------------------------------------------
class TransicionSumaIntegral(Scene):
    def construct(self):
        self.add(encabezado("De la suma finita a la integral definida"))
        suma = matematica(r"S_n=\sum_{i=1}^{n}f(x_i^*)\,\Delta x", 1.18)
        suma.shift(UP * 1.58)
        self.play(Write(suma), run_time=2.4)
        pausa(self, 3)
        flecha = matematica(r"\xrightarrow{\ \ n\to\infty\ \ }", 1.0).set_color(DORADO)
        flecha.next_to(suma, DOWN, buff=0.52)
        self.play(Write(flecha), run_time=1.4)
        pausa(self, 2.4)
        igualdad = matematica(r"\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\,\Delta x", 1.05)
        igualdad.next_to(flecha, DOWN, buff=0.48)
        self.play(Write(igualdad), run_time=2.6)
        pausa(self, 6.0)
        aviso = pie(texto("El límite conecta las expresiones; no reemplazamos símbolos aislados", 21, GRAY_B))
        self.play(Write(aviso), run_time=1.5)
        pausa(self, 3.0)
        estado_limpio(self)


# ---------------------------------------------------------
# 11. Respuesta de forma explícita a la pregunta central
# ---------------------------------------------------------
class RespuestaPreguntaCentral(Scene):
    def construct(self):
        self.add(encabezado("¿Cómo llegamos a la integral definida?"))
        secuencia = [
            texto("1. Construimos rectángulos", 28),
            texto("2. Sumamos sus aportes", 28),
            texto("3. Refinamos la partición", 28),
            texto("4. Tomamos el límite", 28, DORADO),
        ]
        grupo = VGroup(*secuencia).arrange(DOWN, buff=0.37, aligned_edge=LEFT)
        grupo.move_to(UP * 0.38)
        for l in grupo:
            self.play(FadeIn(l, shift=RIGHT * 0.15), run_time=0.8)
            pausa(self, 1.2)
        conclusion = matematica(r"\int_0^3\left[\frac12(x-1)^2+1\right]dx=\frac92=4{,}5", 0.95)
        pie(conclusion)
        self.play(Write(conclusion), run_time=2.4)
        pausa(self, 7.0)
        estado_limpio(self)


# ---------------------------------------------------------
# 12. Créditos legibles: fuentes deben figurar en el video según la pauta
# ---------------------------------------------------------
class Creditos(Scene):
    def construct(self):
        self.play(Write(texto("Fuentes y recursos", 39).shift(UP * 2.65)), run_time=1.2)
        referencias = VGroup(
            texto("Apunte de Cálculo Intermedio: Introducción a la integral", 21),
            texto("Stewart · Cálculo de una variable: Conceptos y contextos (4.ª ed.)", 21),
            texto("Larson, Hostetler y Edwards · Cálculo y geometría analítica (vol. 1)", 21),
            texto("Manim Community · docs.manim.community", 21),
            texto("Motivación audiovisual: BlueDot (YouTube, 2023)", 21),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to(DOWN * 0.1)
        for r in referencias:
            self.play(FadeIn(r), run_time=0.55)
        pie_txt = texto("Equipo Grupo 4 · Cálculo Intermedio", 23, AZUL)
        pie(pie_txt)
        self.play(Write(pie_txt), run_time=0.7)
        pausa(self, 7.0)
        estado_limpio(self)
