import os
import subprocess
from core.config import BUILD_DIR, VIDEO_RENDER_DIR, PARTS_DIR, OUTPUT_DIR

def render_sequential_partitions(slides, audio_durations):
    """Unisce in modo lineare i frame PNG e i file audio mp3 estratti"""
    concat_file_path = os.path.join(BUILD_DIR, "concat.txt")
    
    with open(concat_file_path, "w") as f_concat:
        for idx, slide in enumerate(slides):
            audio_path = os.path.join(BUILD_DIR, f"audio_render/track_{idx+1:02d}.mp3")
            slide_path = os.path.join(VIDEO_RENDER_DIR, slide)
            output_part_path = os.path.join(PARTS_DIR, f"part_{idx+1:02d}.mp4")
            
            f_concat.write(f"file 'parts/part_{idx+1:02d}.mp4'\n")
            
            subprocess.run([
                "ffmpeg", "-y", "-loop", "1", "-i", slide_path, "-i", audio_path, 
                "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage", "-crf", "24", "-g", "60", 
                "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-t", str(audio_durations[idx]), 
                "-pix_fmt", "yuv420p", "-vf", "scale=1280:720,format=yuv420p", 
                "-async", "1", "-vsync", "cfr", 
                output_part_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def finalize_packaging_demux():
    """Unisce istantaneamente le sotto-partizioni mp4 tramite stream copy"""
    final_output_file = os.path.join(OUTPUT_DIR, "presentazione_finale.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "concat.txt", 
        "-c", "copy", final_output_file
    ], cwd=BUILD_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
