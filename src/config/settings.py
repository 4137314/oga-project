# src/config/settings.py
from pathlib import Path


class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    BUILD_DIR = BASE_DIR / "build"
    OUTPUT_DIR = BASE_DIR / "output"

    # Percorsi file
    AUDIO_TRACK = BUILD_DIR / "voiceover.wav"
    VIDEO_OUTPUT = BUILD_DIR / "mute.mp4"
    SRT_FILE = BUILD_DIR / "subtitles.srt"
    FINAL_OUTPUT = OUTPUT_DIR / "project.mp4"

    def init_workspace(self):
        self.BUILD_DIR.mkdir(exist_ok=True)
        self.OUTPUT_DIR.mkdir(exist_ok=True)


settings = Settings()
