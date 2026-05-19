import os
import importlib
from typing import Sequence, List, Optional
from config.slide_template import SlideModule
from engine.processors.audio_proc import AsyncAudioEngine, mux_audio_video
from engine.processors.visual_proc import ExamPresentationEngine, generate_srt
from config.settings import settings
from manim import config as manim_config


async def run_full_pipeline(
    slides: Sequence[SlideModule], section_index: Optional[int] = None
):
    """
    Esegue la pipeline completa.
    Se section_index è fornito, renderizza solo quella specifica slide/sezione.
    """
    print("⚡ [VGEN ENGINE] Inizializzazione Workspace...")
    settings.init_workspace()

    # Filtro selettivo per debug rapido
    target_slides = [slides[section_index]] if section_index is not None else slides

    # 1. Audio: calcolo durate reali per il set target
    audio_engine = AsyncAudioEngine(settings.AUDIO_TRACK)
    durations = await audio_engine.compile_voice_over(target_slides)
    total_duration = sum(durations)

    # 2. Video: configurazione Manim
    os.environ["VGEN_AUDIO_DURATION"] = str(total_duration)
    manim_config.update(
        {
            "output_file": settings.VIDEO_OUTPUT.name,
            "video_dir": str(settings.VIDEO_OUTPUT.parent),
            "quality": "low_quality",
            "write_to_movie": True,
        }
    )

    # Renderizzazione
    scene = ExamPresentationEngine()
    setattr(scene, "slide_modules", target_slides)
    setattr(scene, "durations", durations)
    scene.render()

    # 3. Mastering: sottotitoli e muxing
    srt_path = generate_srt(target_slides, durations, settings.BUILD_DIR / "subs.srt")

    mux_audio_video(
        video=settings.VIDEO_OUTPUT,
        audio=settings.AUDIO_TRACK,
        srt=srt_path,
        output=settings.OUTPUT_DIR
        / ("project_debug.mp4" if section_index is not None else "project.mp4"),
    )
    print(
        f"✓ Pipeline {'(debug mode)' if section_index is not None else ''} completata."
    )


def load_slides_by_chapters(capitoli: List[str]) -> List[SlideModule]:
    """Carica dinamicamente le classi Slide dai moduli nella cartella section/"""
    timeline = []
    for cap in capitoli:
        mod = importlib.import_module(f"section.{cap}")
        slide_class = getattr(mod, f"{cap.capitalize()}Slide")
        instance = slide_class()
        if isinstance(instance, SlideModule):
            timeline.append(instance)
    return timeline
