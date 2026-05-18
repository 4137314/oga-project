#!/usr/bin/env python3
import os
import sys

# Mappa la directory locale per gli import flat del pacchetto vgen/
VGEN_DIR = os.path.abspath(os.path.dirname(__file__))
if VGEN_DIR not in sys.path:
    sys.path.insert(0, VGEN_DIR)

from core.engine import run_pipeline

if __name__ == "__main__":
    try:
        run_pipeline()
    except KeyboardInterrupt:
        print("\n[!] Esecuzione annullata dall'utente.")
        sys.exit(1)
