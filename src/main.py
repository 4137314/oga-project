import asyncio
from engine.core.builder import run_full_pipeline, load_slides_by_chapters


async def main():
    # Caricamento configurazione
    capitoli = [
        "intro",
        "framework",
        "kpi",
        "enel",
        "transition",
        "evolution",
        "conclusion",
    ]

    slides = load_slides_by_chapters(capitoli)

    # Esecuzione pipeline
    await run_full_pipeline(slides, section_index=0)


if __name__ == "__main__":
    asyncio.run(main())
