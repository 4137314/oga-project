# ==============================================================================
# Justfile - Automazione della presentazione d'esame OGA (Standard 2026)
# ==============================================================================

# Comando principale: esegue formattazione, linter, controllo tipi e renderizza
default: format lint type-check run

# Verifica che l'ambiente Nix e i pacchetti PEP 621 siano attivi
[private]
env-check:
    @python3 -c "import manim, edge_tts; print('✓ Ambiente di sviluppo validato.')"

# Sincronizza lo stile del codice usando Ruff
format:
    @echo "Formattazione del codice in corso..."
    ruff format src/

# Analisi statica per correggere bug al volo ed eliminare import inutilizzati
lint:
    @echo "Analisi statica (Linter) in corso con filtri Manim..."
    ruff check src/ --fix --ignore E501,F403,F405
# Valida che tutte le slide in src/section/ rispettino il Protocollo statico
type-check:
    @echo "Controllo statico dei tipi (Mypy)..."
    MYPYPATH=src mypy --ignore-missing-imports --explicit-package-bases src/

# Compila l'audio TTS ed esegue il motore grafico vettoriale di Manim
run: env-check
    @echo "Avvio della pipeline audio/video (Manim + Edge-TTS)..."
    python3 src/main.py

# justfile
clean:
    @echo "Pulizia profonda del workspace tramite settings..."
    python3 -c "from src.config.settings import settings; import shutil; \
    shutil.rmtree(settings.BUILD_DIR, ignore_errors=True); \
    shutil.rmtree(settings.OUTPUT_DIR, ignore_errors=True); \
    import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]"
    @echo "Workspace pulito."
