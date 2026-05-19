import os
import subprocess
import wave
import asyncio
from pathlib import Path
from typing import Sequence, List
import edge_tts
from config.slide_template import SlideModule


class AsyncAudioEngine:
    def __init__(self, output_path: Path):
        self.output_path = output_path
        self.temp_dir = output_path.parent
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    async def compile_voice_over(self, slides: Sequence[SlideModule]) -> List[float]:
        """Sintetizza l'audio e restituisce la durata reale di ogni slide."""
        voice_part = self.output_path
        temp_files = []
        durations: List[float] = []

        # 1. Sintesi segmenti e misurazione
        for i, slide in enumerate(slides):
            temp_s = self.temp_dir / f"s_{i}.wav"
            text = f"<prosody rate='-5%'>{slide.tts_text}</prosody>"
            communicate = edge_tts.Communicate(text, slide.voice_id)
            await communicate.save(str(temp_s))

            # Piccolo ritardo per assicurare il rilascio del file dal sistema operativo
            await asyncio.sleep(0.1)

            # Misura la durata reale usando la libreria standard 'wave'
            try:
                with wave.open(str(temp_s), "rb") as wav_file:
                    frames = wav_file.getnframes()
                    rate = wav_file.getframerate()
                    duration = frames / float(rate)
                    durations.append(duration)
            except Exception as e:
                print(f"⚠️ Errore lettura durata WAV {temp_s}: {e}. Uso fallback 5.0s.")
                durations.append(5.0)

            temp_files.append(temp_s)

        # 2. Concatenazione FFmpeg
        filelist_path = self.temp_dir / "filelist.txt"
        with open(filelist_path, "w") as f:
            for p in temp_files:
                f.write(f"file '{p.absolute()}'\n")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(filelist_path),
                "-ar",
                "48000",
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(voice_part),
            ],
            check=True,
            capture_output=True,
        )

        # 3. Pulizia
        for p in temp_files:
            if p.exists():
                os.remove(p)
        if filelist_path.exists():
            os.remove(filelist_path)

        return durations


def mux_audio_video(video: Path, audio: Path, srt: Path, output: Path):
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-i",
        str(audio),
        "-vf",
        f"subtitles={srt}:force_style='FontSize=20'",
        "-filter_complex",
        "[1:a]aformat=sample_rates=48000:sample_fmts=fltp,loudnorm=I=-16[aout]",
        "-c:v",
        "libx264",
        "-map",
        "0:v:0",
        "-map",
        "[aout]",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-shortest",
        str(output),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
