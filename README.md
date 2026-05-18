# OGA-PROJECT: Multi-Dimensional Energy Utility Analysis (Enel FY 2025)

An automated, cross-platform academic presentation framework built with LaTeX Beamer (using the Metropolis and Owl themes). This project is fully containerized and automated using **Nix Flakes** and **Direnv**, allowing you to compile slide decks, speaker notes, and even an automated synthetic video presentation with synced Text-to-Speech (TTS) audio.

---

## 🚀 Features & Build Modes

The project can be compiled into three distinct outputs using the included `Makefile`:
1. **Standard Slides:** Clean 16:9 PDF presentation slides ready for delivery.
2. **Speaker Notes Slides:** Ultra-wide 32:9 dual-screen PDF displaying the slides on the left and your speaker notes (`\note{}`) on the right (perfect for `pdfpc`).
3. **Automated Video Presentation:** Generates a `.mp4` video matching every slide and step transition (`\pause`) with a generated Italian synthetic voice reading your speaker notes.

---

## 🛠️ Cross-Platform Prerequisites (Nix Setup)

To ensure perfect compilation without manually installing heavy TeX Live distributions, Python packages, or FFmpeg encoders, this project uses the **Nix package manager**.

### 1. Install Nix

Select the installation command matching your operating system:

* **Linux & macOS (Determinate Systems Installer - Recommended):**
    ```bash
    curl --proto '=https' --tlsv1.2 -sSf -L [https://install.determinate.systems/nix](https://install.determinate.systems/nix) | sh -s -- install
    ```
* **Windows 11 (via WSL2):**
    First, ensure you have WSL2 installed with an Ubuntu distribution (`wsl --install`). Open your WSL Ubuntu terminal and run the Linux command above.

> [!IMPORTANT]
> Restart your terminal application after the Nix installation completes to load the environment variables.

### 2. Enable Experimental Features
Ensure Nix Flakes are enabled. If you used the Determinate Systems installer, this is done automatically. Otherwise, create or append to `~/.config/nix/nix.conf`:
```text
experimental-features = nix-command flakes
