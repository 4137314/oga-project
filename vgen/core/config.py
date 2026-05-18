import os
import re

# Calcolo dei percorsi basato sulla radice oga-project/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD_DIR = os.path.join(BASE_DIR, "build")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Sotto-cartelle di build
VIDEO_RENDER_DIR = os.path.join(BUILD_DIR, "video_render")
AUDIO_RENDER_DIR = os.path.join(BUILD_DIR, "audio_render")
PARTS_DIR = os.path.join(BUILD_DIR, "parts")

def init_workspace():
    """Inizializza l'albero delle cartelle di lavoro"""
    os.makedirs(VIDEO_RENDER_DIR, exist_ok=True)
    os.makedirs(AUDIO_RENDER_DIR, exist_ok=True)
    os.makedirs(PARTS_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def prepare_clean_text(raw_text):
    """Pulisce il testo rimuovendo i tag e i costrutti speciali di LaTeX"""
    if not raw_text:
        return ""
    text = raw_text
    text = re.sub(r'<[^>]*>', '', text)
    text = text.replace(r'\%', ' percento')
    text = text.replace(r'&', ' e ')
    text = text.replace(r'\_', ' ')
    text = re.sub(r'\--+', ' ', text)
    text = re.sub(r'\\•+', ' ', text)
    text = re.sub(r'\\[a-zA-Z]+\*?(\{.*?\})?', '', text)
    text = text.replace('{', '').replace('}', '')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
