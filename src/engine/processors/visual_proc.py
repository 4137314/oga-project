from typing import Any, List, Sequence
from manim import *
from pathlib import Path
import textwrap
from config.slide_template import SlideModule


class ExamPresentationEngine(Scene):
    def construct(self) -> None:
        slides: List[Any] = getattr(self, "slide_modules", [])
        durations: List[float] = getattr(self, "durations", [5.0] * len(slides))

        # HUD Accademico
        titolo_esame = Text(
            "Organizzazione e Gestione Aziendale UniTN", font_size=12, color=GRAY_C
        ).to_edge(UP, buff=0.2)
        linea_strutturale = Line(
            start=LEFT * 7, end=RIGHT * 7, color=BLUE_E, stroke_width=1
        ).next_to(titolo_esame, DOWN, buff=0.1)
        self.add(titolo_esame, linea_strutturale)

        # Rendering sincronizzato con le durate reali
        for i, slide in enumerate(slides):
            slide_duration = durations[i]
            slide.render_assets(self, duration=slide_duration)


def _fmt_time(ms: int) -> str:
    s = ms // 1000
    return f"{s // 3600:02}:{(s % 3600) // 60:02}:{s % 60:02},{ms % 1000:03}"


def generate_srt(
    slides: Sequence[SlideModule], durations: List[float], output_path: Path
) -> Path:
    with open(output_path, "w", encoding="utf-8") as f:
        counter = 1
        current_time = 0.0
        for i, slide in enumerate(slides):
            slide_duration = durations[i]
            lines = textwrap.wrap(slide.tts_text, width=50)
            time_slice = slide_duration / max(1, len(lines))

            for j, line in enumerate(lines):
                start = int(current_time * 1000)
                end = int((current_time + time_slice) * 1000)
                f.write(
                    f"{counter}\n{_fmt_time(start)} --> {_fmt_time(end)}\n{line}\n\n"
                )
                counter += 1
                current_time += time_slice
    return output_path
