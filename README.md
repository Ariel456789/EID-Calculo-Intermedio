# EID Cálculo Intermedio — Grupo 04

**Tema:** Del símbolo de sumatoria al símbolo de integral  
**Pregunta central:** ¿Cómo pasamos de una suma con un número finito de rectángulos a una integral definida?  
**Asignatura:** MAT1188 — Cálculo Intermedio, Ingeniería Civil Informática  
**Tecnología:** Manim Community (Python)

> **Estado del repositorio:** fuente actualizada para el guion; el video base todavía requiere render, sincronización de voces y revisión final. **No se debe presentar el antiguo `video_final_grupo4.mp4` como el video actualizado.**

## Integrantes y participación

| Integrante | Área principal inicial | GitHub |
|---|---|---|
| Gustavo Martínez | Desarrollo matemático, guion y revisión | gmartinezsenglar |
| Ariel Díaz | Visualización, implementación y renderizado | Ariel456789 |
| Luciana Lagos | Revisión e integración audiovisual (asignación inicial) | **Completar usuario** |

**Importante:** la situación de participación de un integrante debe resolverse con la docente. La pauta establece que los cambios de integrantes requieren autorización y que el grupo no puede expulsar unilateralmente a un compañero. Hasta confirmación formal, no alterar la lista para aparentar un cambio aprobado. Ajustar las voces y la ficha según los integrantes *habilitados* que finalmente confirme la docente.

## Idea matemática y ejemplo

- Motivación: un vehículo con rapidez constante `6 m/s` durante `5 s` recorre `30 m` y ese valor coincide con el área de un rectángulo en la gráfica rapidez-tiempo. La rapidez variable motiva las aproximaciones mediante rectángulos. **Es una motivación, no el ejemplo principal**.
- Ejemplo principal original del equipo: 
  \(f(x)=\tfrac12(x-1)^2+1\), intervalo \([0,3]\), puntos muestra en el **punto medio**.
- \(\Delta x=3/n\), \(x_i^*=(i-\tfrac12)3/n\), \(S_n=\sum_{i=1}^n f(x_i^*)\Delta x\).
- \(S_4=567/128=4,4296875\).
- Refinamientos: \(n=4,8,16,32\).
- Fórmula general verificada: \(S_n=9/2-9/(8n^2)\).
- Resultado: \(\lim_{n\to\infty}S_n=9/2=\int_0^3f(x)\,dx\).

**Precisión conceptual:** la integral no se obtiene reemplazando `Σ → ∫` o `Δx → dx` por separado: se define mediante el **límite de las sumas de Riemann** para esta función continua y particiones uniformes. La función elegida es positiva, por lo que el resultado es área geométrica.

## Requisitos

- Python: **comprobar la versión realmente utilizada** en el PC del equipo (`python --version`). El proyecto original anotaba 3.12, pero el ZIP también contenía caché de Python 3.14, por lo que no se da una versión por confirmada.
- Manim Community (dependencia en `requirements.txt`); anotar la versión obtenida mediante `python -m manim --version`.
- Distribución LaTeX (en Windows puede ser MiKTeX) para `MathTex`.
- FFmpeg (provisto por `imageio-ffmpeg` o instalado en PATH).

```bash
python -m pip install -r requirements.txt
python -m manim --version
```

Documentación oficial: https://docs.manim.community/

## Archivos

```text
EID-Calculo-Intermedio/
├── README.md                  # Datos, fuentes, IA y ejecución
├── escenas.py                 # 12 escenas, sin audio integrado
├── parametros.py              # Función, intervalo, criterios, pausas y nombres
├── utilidades.py              # Ejes, puntos muestra, rectángulos y sumas
├── build.py                   # Renderizado por escena y ensamblaje base
├── requirements.txt           # Dependencias Python
├── GUIA_PARA_ARIEL.md         # Revisión técnica antes de subir
├── PISTA_DE_NARRACION.md      # Asignación de voz y sincronización mañana
└── media/                     # Generado por Manim, no es fuente obligatoria
```

El guion/ storyboard en LaTeX se trabajó por separado; puede incorporarse al repositorio como evidencia matemática cuando su ubicación esté decidida.

## Orden de escenas (video base, sin narración)

| Orden | Clase | Propósito |
|---|---|---|
| 1 | `Presentacion` | Tema, pregunta central e integrantes por confirmar |
| 2 | `AutoVelocidadConstante` | Rapidez constante y área rectangular |
| 3 | `AutoVelocidadVariable` | Problema motivador de rapidez variable |
| 4 | `RegionInicial` | Función y área del ejemplo propio |
| 5 | `ParticionInicial` | Partición, n y ancho \(\Delta x\) |
| 6 | `SumaRiemannConstruccion` | Puntos medios, cuatro rectángulos y \(S_4\) |
| 7 | `RefinamientoProgresivo` | \(n=4,8,16,32\) y valores de las sumas |
| 8 | `CalculoGeneral` | Identidades y fórmula general \(S_n\) |
| 9 | `LimiteProceso` | Evaluación algebraica del límite |
| 10 | `TransicionSumaIntegral` | Relación completa con el símbolo integral |
| 11 | `RespuestaPreguntaCentral` | Respuesta explícita y resultado |
| 12 | `Creditos` | Fuentes básicas legibles |

### Renderizar una sola escena

Desde la carpeta del proyecto:

```bash
python build.py --solo-escena SumaRiemannConstruccion --calidad ql
python build.py --solo-escena TransicionSumaIntegral --calidad ql
```

O con Manim:

```bash
python -m manim -pql escenas.py ParticionInicial
```

### Renderizar y ensamblar video base

```bash
python build.py --calidad ql   # pruebas rápidas a 480p15
python build.py --calidad qm   # base recomendable 720p30
python build.py --calidad qh   # alta, más lenta
```

Por defecto se genera **`video_base_sin_narracion.mp4`**, sin alterar el archivo antiguo `video_final_grupo4.mp4`. Después de sincronizar las voces, exportar el MP4 final con el nombre oficial.

Para ampliar o reducir **solo las esperas**, no la velocidad de los movimientos:

```bash
python build.py --calidad qm --factor-pausas 1.10
python build.py --calidad qm --factor-pausas 0.90
```

También se puede ajustar la duración de clips individuales en el editor audiovisual. El video final debe durar **4 a 6 minutos** incluyendo presentación, cierre y créditos. No usar esperas artificiales prolongadas para suplir contenido matemático.

Para ensamblar clips ya existentes sin renderizar otra vez:

```bash
python build.py --sin-render --calidad qm
```

**Advertencia:** `--sin-render` reutiliza clips que podrían pertenecer a otra versión. Verificarlos antes.

## Narración y audio (pendiente)

- Grabar narración por escenas y guardar originales sin compresión excesiva.
- Cada integrante **habilitado** debe pronunciar una explicación **matemática sustantiva** con su voz, e identificarse por nombre en el video.
- Sincronizar la voz con fórmulas o figuras en pantalla; no es necesario leer todas las expresiones en voz alta.
- Priorizar audio claro, sin música que tape las voces.
- Ver `PISTA_DE_NARRACION.md` para repartir escenas y dejar constancia de tiempos.

## Fuentes matemáticas y recursos

Referencias para el proyecto (verificar que se citen páginas efectivamente consultadas):

1. **Apunte docente:** *Introducción a la integral*, MAT1188 Cálculo Intermedio, 2026, secciones 1–6. PDF de la asignatura.
2. **James Stewart:** *Cálculo de una variable: Conceptos y contextos*, **4.ª edición**, Cengage Learning, **2010**. Secciones 5.1 y 5.2, páginas impresas 332 y 343 (inicio de sección). Ejemplar PDF consultado: `Cálculo de una variable. Conceptos y contextos (James Stewart).pdf` (**agregar URL de procedencia verificable de este ejemplar**).
3. **R. Larson, R. Hostetler y B. Edwards:** *Cálculo y geometría analítica*, **volumen 1, 6.ª edición**, McGraw-Hill. Secciones 4.2 y 4.3, pp. impresas 291–292 y desde 304. (**Año editorial y URL de procedencia del ejemplar: por verificar con su página legal**).
4. **Manim Community:** *Documentation*, https://docs.manim.community/ (institución/proyecto Manim Community; consulta de API de animaciones).
5. **BlueDot:** *Este TEOREMA lo CAMBIO TODO | ¿QUÉ es LA INTEGRAL?*, YouTube, 2023, https://www.youtube.com/watch?v=y6YQSUDTzqE . Recurso audiovisual de **inspiración conceptual** para la motivación del automóvil; gráficos, números y código se elaboraron de forma propia, sin reutilizar material audiovisual.

**Nota:** BlueDot no sustituye ninguna de las dos fuentes matemáticas complementarias obligatorias.

## Declaración de uso de IA (borrador verificable)

Se utilizó **ChatGPT (OpenAI)** como apoyo para aclarar la relación entre suma de Riemann y límite, organizar el desarrollo matemático, proponer redacciones de guion y elaborar/modificar el código Python/Manim y la documentación. **El contenido generado se debe revisar en el PC del equipo**, cotejando fórmulas con el apunte y los libros; la sintaxis de Python se comprobó, pero esta revisión no equivale a haber renderizado Manim. Una vez renderizado, registrar qué escenas y parámetros se verificaron efectivamente.

**Completar antes de enviar:** otras herramientas de IA empleadas por los integrantes, partes específicas generadas/asistidas y métodos reales de verificación.

**Plazo indicado por la pauta adjunta:** domingo 18 de octubre de 2026, 23:59.  
**Defensa:** miércoles 21 de octubre; cualquier integrante seleccionado deberá justificar matemáticas y escenas.
