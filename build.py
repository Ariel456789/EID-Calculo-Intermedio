"""
build.py - Genera el VIDEO COMPLETO del Grupo 4.

Qué hace:
    1. Renderiza, en orden, las 7 escenas del proyecto.
    2. Une los 7 clips en un único archivo de video final.

Uso (desde esta carpeta):
    python build.py                 # calidad media (720p30) -> recomendada
    python build.py --calidad ql    # baja (480p15), rápido para probar
    python build.py --calidad qh    # alta (1080p60)

Salida:
    video_final_grupo4.mp4

Requisitos:
    - Manim Community y sus dependencias (LaTeX/MiKTeX para Tex/MathTex).
    - imageio-ffmpeg  (pip install imageio-ffmpeg) para unir los clips.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

ARCHIVO = "escenas.py"
MODULO = Path(ARCHIVO).stem

# Escenas en el ORDEN del video
ESCENAS = [
    "RegionInicial",
    "ParticionInicial",
    "SumaRiemannConstruccion",
    "RefinamientoProgresivo",
    "TransicionSumaIntegral",
    "LimiteProceso",
    "RespuestaPreguntaCentral",
]

# Carpeta de salida de Manim según la calidad
DIR_CALIDAD = {"ql": "480p15", "qm": "720p30", "qh": "1080p60"}

SALIDA = "video_final_grupo4.mp4"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def asegurar_miktex_en_path():
    """Agrega la carpeta bin de MiKTeX al PATH si no está presente."""
    candidatos = [
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64",
        Path("C:/Program Files/MiKTeX/miktex/bin/x64"),
        Path("C:/Program Files (x86)/MiKTeX/miktex/bin/x64"),
    ]
    for carpeta in candidatos:
        if (carpeta / "dvisvgm.exe").exists() or (carpeta / "latex.exe").exists():
            if str(carpeta) not in os.environ.get("PATH", ""):
                os.environ["PATH"] = str(carpeta) + os.pathsep + os.environ.get("PATH", "")
                print(f"[i] MiKTeX agregado al PATH: {carpeta}")
            return


def renderizar(escena, calidad):
    """Renderiza una escena con Manim."""
    cmd = [
        sys.executable, "-m", "manim",
        f"-{calidad}",
        ARCHIVO, escena,
    ]
    print(f"\n[>] Renderizando {escena} ({calidad}) ...")
    subprocess.run(cmd, check=True)


def ruta_video(escena, calidad):
    """Ruta del mp4 generado por Manim para una escena."""
    return Path("media") / "videos" / MODULO / DIR_CALIDAD[calidad] / f"{escena}.mp4"


def obtener_ffmpeg():
    """Devuelve la ruta de un ejecutable ffmpeg disponible."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return shutil.which("ffmpeg")


def concatenar(videos, salida):
    """Une los clips en un único video (sin re-codificar)."""
    ffmpeg = obtener_ffmpeg()
    if ffmpeg is None:
        raise RuntimeError(
            "No se encontró ffmpeg. Instálalo con:  pip install imageio-ffmpeg"
        )

    lista = Path("_lista_concat.txt")
    with open(lista, "w", encoding="utf-8") as f:
        for v in videos:
            ruta = v.resolve().as_posix().replace("'", "'\\''")
            f.write(f"file '{ruta}'\n")

    cmd = [
        ffmpeg, "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(lista),
        "-c", "copy",
        salida,
    ]
    print(f"\n[>] Uniendo {len(videos)} clips en {salida} ...")
    try:
        subprocess.run(cmd, check=True)
    finally:
        lista.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Genera el video final del Grupo 4.")
    parser.add_argument(
        "--calidad", choices=["ql", "qm", "qh"], default="qm",
        help="Calidad de render: ql=480p15, qm=720p30 (def.), qh=1080p60.",
    )
    parser.add_argument(
        "--solo-render", action="store_true",
        help="Solo renderiza las escenas, sin unir el video final.",
    )
    args = parser.parse_args()

    if not Path(ARCHIVO).exists():
        print(f"[X] No se encontró '{ARCHIVO}'. Ejecuta este script desde su carpeta.")
        sys.exit(1)

    asegurar_miktex_en_path()

    # 1) Renderizar cada escena
    for escena in ESCENAS:
        renderizar(escena, args.calidad)

    clips = [ruta_video(e, args.calidad) for e in ESCENAS]
    faltantes = [str(c) for c in clips if not c.exists()]
    if faltantes:
        print("[X] No se generaron estos clips:")
        for f in faltantes:
            print("   -", f)
        sys.exit(1)

    if args.solo_render:
        print("\n[i] Escenas renderizadas (sin unir).")
        return

    # 2) Unir en el video final
    concatenar(clips, SALIDA)

    print(f"\n[OK] Video final generado: {Path(SALIDA).resolve()}")
    print("     (Agrega aquí tu narración/subtítulos en tu editor de video.)")


if __name__ == "__main__":
    main()
