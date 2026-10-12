# Grupo 4 - Del símbolo de sumatoria al símbolo de integral

Proyecto de la Evaluación Integrada de Desempeño (EID) de **Cálculo Intermedio (MAT1188)**.
Consiste en una serie de animaciones hechas con **Manim Community** que explican cómo se
pasa de una suma de Riemann finita a la integral definida.

## Datos del proyecto

- **Asignatura:** Cálculo Intermedio (MAT1188)
- **Curso:** Ingeniería Civil Informática - Segundo año
- **Grupo:** 4
- **Eje / Tema:** Eje 4 - De una suma finita a la integral definida
- **Pregunta central:** ¿Cómo pasamos de una suma con un número finito de rectángulos a una integral definida?

## Integrantes

| Integrante | Rol principal | Cuenta GitHub |
|---|---|---|
| Gustavo Martínez | Matemática y explicación | _(completar)_ |
| Ariel Díaz | Visualización y código | _(completar)_ |
| Luciana Lagos | Revisión e integración | _(completar)_ |

## Ejemplo propio

- **Función:** f(x) = (1/2)(x - 1)^2 + 1
- **Intervalo:** [a, b] = [0, 3]
- **Punto muestra:** punto medio, x_i* = (x_{i-1} + x_i)/2
- **Refinamiento mostrado:** n = 4, 8, 16, 32

## Estructura del repositorio

```
.
├── parametros.py    # Función, intervalo, n y estilos (lo que se explica en la defensa)
├── utilidades.py    # Funciones auxiliares reutilizables (ejes, rectángulos, punto muestra)
├── escenas.py       # Las escenas del video, en orden
├── build.py         # Renderiza todas las escenas y une el video final
├── requirements.txt # Dependencias
└── README.md
```

## Requisitos

- **Python:** 3.12
- **Manim Community:** 0.22.0
- **LaTeX (MiKTeX):** necesario para renderizar `Tex` y `MathTex`.
- **imageio-ffmpeg:** para unir los clips en un solo video.

## Instalación

```bash
python -m pip install -r requirements.txt
```

También debe estar instalado **MiKTeX** (para las fórmulas). En Windows:
https://miktex.org/download

## Cómo ejecutar

Renderizar **una** escena:

```bash
python -m manim -pqm escenas.py RegionInicial
```

Generar el **video completo** (renderiza las 7 escenas y las une):

```bash
python build.py            # calidad media (720p30) - recomendada
python build.py --calidad ql   # baja (pruebas)
python build.py --calidad qh   # alta (1080p60)
```

Salida: `video_final_grupo4.mp4`

## Escenas (orden del video)

| # | Escena | Contenido |
|---|---|---|
| 1 | `RegionInicial` | Planteamiento: la región bajo la curva |
| 2 | `ParticionInicial` | Partición, Δx y los puntos x_i |
| 3 | `SumaRiemannConstruccion` | Construcción de la suma de Riemann |
| 4 | `RefinamientoProgresivo` | n = 4, 8, 16, 32: Δx → 0 |
| 5 | `TransicionSumaIntegral` | De Σ a ∫ (suma → integral) |
| 6 | `LimiteProceso` | El límite n → ∞ como proceso |
| 7 | `RespuestaPreguntaCentral` | Respuesta explícita y cierre |

_(Pendiente por agregar: Presentación y Créditos.)_

## Fuentes

- Apunte base: _Introducción a la integral_ (MAT1188 - Cálculo Intermedio).
- Manim Community Documentation: https://docs.manim.community/
- _(agregar al menos 2 fuentes matemáticas complementarias con autor, título, año y enlace)_

## Declaración de uso de IA

_(Completar: herramienta, finalidad, partes apoyadas y cómo se verificaron. Si no se usó, declararlo.)_

## Ficha de entrega

- **SHA del commit entregado:** _(completar al momento de entregar)_
- **Video:** `video_final_grupo4.mp4` (4 a 6 minutos, con narración).
