import os
import re
import asyncio
import subprocess
import edge_tts
from core.config import BASE_DIR, AUDIO_RENDER_DIR, prepare_clean_text

def extract_all_notes():
    """Estrae i blocchi \\note{} ordinati dai file sorgente delle sezioni"""
    sections = ["intro", "kpi", "enel", "transition", "evolution", "conclusion"]
    all_notes = []
    for sec in sections:
        path = os.path.join(BASE_DIR, "src", "section", f"{sec}.tex")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            notes = re.findall(r'\\note(?:\[.*?\])?\{(.*?)\}', content, re.DOTALL)
            for n in notes:
                all_notes.append(n.strip())
    return all_notes

async def _synthesize_single_track(idx, note_text, audio_durations, progress, task_id):
    """Esegue la sintesi di un singolo file audio con campionamento condizionale"""
    audio_path = os.path.join(AUDIO_RENDER_DIR, f"track_{idx+1:02d}.mp3")
    clean_content = prepare_clean_text(note_text) if note_text else ""
    
    if clean_content:
        try:
            communicate = edge_tts.Communicate(
                text=clean_content,
                voice='it-IT-DiegoNeural',
                rate='+50%',
                pitch='-10Hz'
            )
            await communicate.save(audio_path)
            
            res = subprocess.run([
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", audio_path
            ], stdout=subprocess.PIPE, text=True, check=True)
            duration = float(res.stdout.strip())
        except Exception:
            duration = 1.0
            subprocess.run([
                "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", str(duration), audio_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        duration = 0.65
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", str(duration), audio_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    audio_durations[idx] = duration
    if progress and task_id is not None:
        progress.advance(task_id, 1)

async def download_all_audio_parallel(slides, notes, progress, task_id):
    """Scarica asincronamente i brani audio mappandoli sulle slide totali"""
    audio_durations = [0.65] * len(slides)
    tasks = [
        _synthesize_single_track(idx, notes[idx] if idx < len(notes) else None, audio_durations, progress, task_id)
        for idx in range(len(slides))
    ]
    await asyncio.gather(*tasks)
    return audio_durations
