import os
import re
import sys
import asyncio
import subprocess

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from core.config import init_workspace, VIDEO_RENDER_DIR
from audio.tts import extract_all_notes, download_all_audio_parallel
from video.muxer import render_sequential_partitions, finalize_packaging_demux

console = Console()

def run_pipeline():
    console.print("\n[bold back_blue]  HOLOS/ AUDIO-VIDEO ENGINE  [/bold back_blue]\n")
    
    init_workspace()
    
    with console.status("[bold cyan]Extracting[/bold cyan] LaTeX note blocks...", spinner="dots"):
        notes = extract_all_notes()
    console.print("[bold green]✓ Extracted[/bold green] note blocks from LaTeX source.")
    
    with console.status("[bold cyan]Generating[/bold cyan] 150 DPI clean slide frames (pdftoppm)...", spinner="dots"):
        subprocess.run(["pdftoppm", "-png", "-r", "150", "output/presentazione_pulita.pdf", os.path.join(VIDEO_RENDER_DIR, "slide")])
    
    slides = sorted(
        [f for f in os.listdir(VIDEO_RENDER_DIR) if f.startswith("slide") and f.endswith(".png")],
        key=lambda x: [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)]
    )
    console.print(f"[bold green]✓ Rendered[/bold green] {len(slides)} subframes from template.")
    
    if len(slides) == 0:
        console.print("[bold red][!] ERRORE CRITICO: pdftoppm vuoto![/bold red]")
        sys.exit(1)
        
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(bar_width=30), TaskProgressColumn(), console=console) as progress:
        task_audio = progress.add_task("[cyan]Downloading[/cyan] Native API tracks (1.5x speed)", total=len(slides))
        audio_durations = asyncio.run(download_all_audio_parallel(slides, notes, progress, task_audio))
    console.print("[bold green]✓ Synced[/bold green] Edge-TTS voice generation completed.")

    total_duration = sum(audio_durations)
    minutes = int(total_duration // 60)
    seconds = total_duration % 60
    console.print(f"[bold dim]➔ Analysis:[/bold dim] Total speech timeline computed at [bold]{minutes}m {seconds:.2f}s[/bold] ({total_duration:.2f} seconds).")
    
    if total_duration > 300.0:
        console.print(f"\n[bold red]✖ COMPILATION BLOCKER:[/bold red] La timeline complessiva ({minutes}m {seconds:.2f}s) supera il limite di 300.0s.")
        sys.exit(1)
    else:
        console.print("[bold green]✓ Approved[/bold green] Timeline complies with the 5-minute strict budget constraint.")

    with console.status("[bold cyan]Multiplexing[/bold cyan] Frames and high-fidelity audio tracks...", spinner="bouncingBar"):
        render_sequential_partitions(slides, audio_durations)
    console.print("[bold green]✓ Rendered[/bold green] All sequential partitions generated.")

    with console.status("[bold yellow]Packaging[/bold yellow] Stream copy demux concatenation...", spinner="arc"):
        finalize_packaging_demux()
        
    console.print(f"\n[bold green]✓ Finished[/bold green] Targets compiled in [underline]output/presentazione_finale.mp4[/underline]\n")
