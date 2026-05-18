# Configurazione variabili
MAIN_DIR = src
MAIN_FILE = main
BUILD_DIR = $(shell pwd)/build
OUTPUT_DIR = $(shell pwd)/output

# Colori UI stile Cargo
GREEN  := \033[1;32m
CYAN   := \033[1;36m
RESET  := \033[0m

.PHONY: all clean notes video create_dirs

# 1. MODALITÀ STANDARD (Slide pulite, senza note)
all: create_dirs
	@echo -e "$(CYAN)Compiling$(RESET) clean slides (pdfLaTeX)..."
	@cd $(MAIN_DIR) && pdflatex -interaction=batchmode -output-directory=$(BUILD_DIR) $(MAIN_FILE).tex > /dev/null 2>&1
	@cd $(MAIN_DIR) && pdflatex -interaction=batchmode -output-directory=$(BUILD_DIR) $(MAIN_FILE).tex > /dev/null 2>&1
	@cp $(BUILD_DIR)/$(MAIN_FILE).pdf $(OUTPUT_DIR)/presentazione_pulita.pdf
	@echo -e "$(GREEN) Finished$(RESET) target output/presentazione_pulita.pdf"

# 2. MODALITÀ NOTE (Slide doppie con note per pdfpc)
notes: create_dirs
	@echo -e "$(CYAN)Compiling$(RESET) multi-screen template with presenter notes..."
	@cd $(MAIN_DIR) && pdflatex -interaction=batchmode -output-directory=$(BUILD_DIR) "\def\ShowNotes{1} \input{$(MAIN_FILE).tex}" > /dev/null 2>&1
	@cd $(MAIN_DIR) && pdflatex -interaction=batchmode -output-directory=$(BUILD_DIR) "\def\ShowNotes{1} \input{$(MAIN_FILE).tex}" > /dev/null 2>&1
	@cp $(BUILD_DIR)/$(MAIN_FILE).pdf $(OUTPUT_DIR)/presentazione_con_note.pdf
	@echo -e "$(GREEN) Finished$(RESET) target output/presentazione_con_note.pdf"

# 3. MODALITÀ VIDEO (Automazione TTS tramite script Python)
video: all
	@python3 vgen/vgen.py

create_dirs:
	@mkdir -p build
	@mkdir -p output

clean:
	@echo -e "$(CYAN) Cleaning$(RESET) workspace environments..."
	@rm -rf build output
	@rm -f *.pdfpc concat.txt
	@echo -e "$(GREEN)  Cleaned$(RESET) environment cache."
