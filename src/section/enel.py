from manim import *


class EnelSlide:
    title: str = "4. CASO STUDIO: ENEL S.P.A. FY 2025"
    voice_id: str = "it-IT-DiegoNeural"

    # Traccia TTS fonetica continua ottimizzata per la dizione fluida di Diego (Stile HOLOS/)
    tts_text: str = (
        "Passiamo ora all'analisi del caso di studio verticale su Enel. Per comprendere come l'azienda gestisca "
        "la complessità macroeconomica appena vista, dobbiamo scendere al livello dell'infrastruttura tecnologica proprietaria. "
        "Il bènchmark che corrobora questa sezione si basa sulla release pì pì èsse èsse fìrmuor, tracciata con l'hasc "
        "di riferimento Include cinque ci sei due due bi sei. Questa architettura software, documentata rigorosamente tramite dòcsigen, "
        "costituisce il nucleo di orchestrazione per l'acquisizione dei flussi di telemetria dai nodi di rete in tempo reale, "
        "garantendo l'integrità del dato alla base delle decisioni di bùsiness. Sul piano industriale, la capacità installata "
        "globale è di quasi ottantasette Gigauatt. Come vedete a sinistra, il cuore delle rinnovabili è guidato dall'idroelettrico, "
        "seguito da eolico e solare. Sottolineo alla commissione l'importance dei tremilaquattrocentoquarantuno Megauatt di sistemi "
        "di accumulo bèss a batteria: sono lo strumento critico per stabilizzare le fluttuazioni intrinseche del solare e dell'eolico. "
        "Questo bilanciamento permette l'accelerazione del blocco di allerta a destra: il crollo del carbone a soli quattromilaseicentoventisette "
        "Megauatt indica il feis aut quasi definitivo della generazione termica tradizionale mèrčant sul mercato europeo. "
        "Questa capacità produttiva segue logiche di specializzazione geografica mirate nelle aree Tier uan. In Italia, Enel mantiene "
        "la sua roccaforte idroelettrica con circa tredici Gigauatt di asset storici ammortizzati, che garantiscono flessibilità "
        "e margini elevati nel mercato dei servizi di dispacciamento. Negli Stati Uniti, invece, il Gruppo ha concentrato oltre la "
        "metà del suo asset eolico globale con la tecnologia uìnd attiva, capitalizzando sui regimi di incentivazione locali e sulle "
        "grandi economie di scala territoriali. Concludiamo il focus industriale esaminando la logica feilsèif dei sistemi di stòreg "
        "periferici. Per garantire che i dati di telemetria vengano registrati sul file lòg ci èsse vu senza perdite, l'architettura "
        "implementa un isolamento inarduar e software. Grazie alla gestione dual mòd tramite fat effe èsse e a un sèifri lòc arduar, "
        "il sistema previene in modo deterministico la corruzione del fàilsistem, impedendo la scrittura concorrente quando un òst "
        "esterno accede alla memoria. Questa continuità operativa del dato è il prerequisito fondamentale per la transizione digitale "
        "delle reti che analizzeremo ora."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Inizializzazione Titolo di Sezione Fisso
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # ==============================================================================
        # FRAME 1: CONFIGURAZIONE FIRMWARE TARGET (ppse-firmware)
        # ==============================================================================
        sottotitolo_1 = Text(
            "Architettura e Orchestrazione Controllo Firmware",
            font_size=18,
            color=GRAY_B,
        ).next_to(titolo, DOWN, buff=0.2)

        box_firmware = VGroup(
            Text(
                "⚙️ CONFIGURAZIONE DI RELEASE (FY 2025)",
                font_size=13,
                color=BLUE_B,
                weight=BOLD,
            ),
            Text("• Target di Sistema: ppse-firmware", font_size=12, color=WHITE),
            Text("• Release di Riferimento: Hash 5c622b6", font_size=12, color=WHITE),
            Text(
                "• Data Climax di Monitoraggio: 14 Maggio 2026",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bg_fw = SurroundingRectangle(
            box_firmware,
            color=BLUE_C,
            buff=0.25,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_fw = VGroup(bg_fw, box_firmware).scale(0.95).shift(UP * 0.2)

        desc_fw = Text(
            "Integrazione documentale automatica tramite Doxygen 1.16.1.\nGarantisce la piena tracciabilità dei flussi di telemetria in tempo reale.",
            font_size=12,
            color=GRAY_C,
        ).next_to(block_fw, DOWN, buff=0.4)

        scene.play(FadeIn(sottotitolo_1), FadeIn(block_fw), run_time=1.5)
        scene.play(Write(desc_fw), run_time=1.5)

        # Attesa per coprire la spiegazione dell'infrastruttura firmware (circa il 22% della durata totale)
        scene.wait(max(1.0, (duration * 0.22) - 4.5))
        scene.play(
            FadeOut(sottotitolo_1), FadeOut(block_fw), FadeOut(desc_fw), run_time=0.8
        )

        # ==============================================================================
        # FRAME 2: QUANTITATIVA MIX PRODUTTIVO (86.986 MW)
        # ==============================================================================
        sottotitolo_2 = Text(
            "Capacità Installata di Gruppo: 86.986 MW", font_size=18, color=PURPLE_A
        ).next_to(titolo, DOWN, buff=0.2)

        col_capacita = VGroup(
            Text(
                "🟢 CAPACITÀ RINNOVABILE CORE", font_size=12, color=GREEN_B, weight=BOLD
            ),
            Text(
                "• Idroelettrico: 28.320 MW\n• Eolico: 16.184 MW\n• Solare: 13.059 MW",
                font_size=11,
                color=WHITE,
            ),
            VMobject().set_height(0.1),  # Risolto l'errore Mypy 'Spacer' non definito
            Text("🔵 TECNOLOGIE DI SUPPORTO", font_size=12, color=BLUE_B, weight=BOLD),
            Text(
                "• Sistemi BESS (Batterie): 3.441 MW\n• CCGT (Ciclo Combinato): 12.420 MW\n• Nucleare: 3.328 MW",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        col_alert_carbone = VGroup(
            Text("⚠️ ALERT: PHASE-OUT FOSSILI", font_size=12, color=RED_A, weight=BOLD),
            Text(
                "La capacità residua a Carbone\nscende drasticamente a 4.627 MW.\n\nDeclino irreversibile della\ngenerazione termica tradizionale\nmerchant sul mercato europeo.",
                font_size=10,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        bg_carbone = SurroundingRectangle(
            col_alert_carbone,
            color=RED_A,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_carbone = VGroup(bg_carbone, col_alert_carbone).scale(0.95)

        layout_mix = (
            VGroup(col_capacita, block_carbone)
            .arrange(RIGHT, buff=1.2)
            .next_to(sottotitolo_2, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_2), run_time=0.5)
        scene.play(FadeIn(col_capacita), run_time=1.5)
        scene.play(FadeIn(block_carbone), run_time=1.0)

        # Attesa per spiegazione mix produttivo e BESS
        scene.wait(max(1.0, (duration * 0.23) - 3.0))
        scene.play(FadeOut(sottotitolo_2), FadeOut(layout_mix), run_time=0.8)

        # ==============================================================================
        # FRAME 3: ALLOCAZIONE DI CAPITALE GEOGRAFICA
        # ==============================================================================
        sottotitolo_3 = Text(
            "Specializzazione Geografica Asset Tier 1", font_size=18, color=GREEN_A
        ).next_to(titolo, DOWN, buff=0.2)

        block_it = VGroup(
            Text(
                "🇮🇹 ROCCAFORTE EUROPA (ITALIA)", font_size=12, color=BLUE_A, weight=BOLD
            ),
            Text(
                "• Concentrazione di 12.994 MW idro.\n• Asset storici ammortizzati.\n• Fornitura di flessibilità essenziale\n  per i servizi di dispacciamento.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_it = SurroundingRectangle(
            block_it,
            color=BLUE_B,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_it = VGroup(bg_it, block_it)

        block_us = VGroup(
            Text("🇺🇸 HUB DI CRESCITA (USA)", font_size=12, color=ORANGE, weight=BOLD),
            Text(
                "• Oltre il 50% del potenziale eolico.\n• 6.218 MW di tecnologia Wind attiva.\n• Sfruttamento strategico degli schemi\n  regolatori e incentivi locali.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_us = SurroundingRectangle(
            block_us,
            color=ORANGE,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_us = VGroup(bg_us, block_us)

        layout_geo = (
            VGroup(card_it, card_us)
            .arrange(RIGHT, buff=0.8)
            .next_to(sottotitolo_3, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_3), FadeIn(layout_geo), run_time=1.5)

        # Attesa per geografie
        scene.wait(max(1.0, (duration * 0.22) - 1.5))
        scene.play(FadeOut(sottotitolo_3), FadeOut(layout_geo), run_time=0.8)

        # ==============================================================================
        # FRAME 4: LOGICA FAILSAFE STORAGE (FatFS Connection Lock)
        # ==============================================================================
        sottotitolo_4 = Text(
            "Infrastrutture e Logica Failsafe di Storage", font_size=18, color=RED_A
        ).next_to(titolo, DOWN, buff=0.2)

        box_failsafe = VGroup(
            Text(
                "🛡️ MECCANISMI DI PROTEZIONE DEL FILESYSTEM",
                font_size=13,
                color=GREEN_B,
                weight=BOLD,
            ),
            Text(
                "• Dual-Mode Access: Gestione trasparente via libreria FatFS su Flash interna.",
                font_size=12,
                color=WHITE,
            ),
            Text(
                "• Safety Lock: Rilevamento automatico dello stato della connessione hardware USB.",
                font_size=12,
                color=WHITE,
            ),
            Text(
                "• Prevenzione Corruzione: Blocco automatico della scrittura concorrente\n  sul file telemetry_log.csv se il PC occupa il Mass Storage.",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        bg_fs = SurroundingRectangle(
            box_failsafe,
            color=GREEN_A,
            buff=0.25,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_fs = (
            VGroup(bg_fs, box_failsafe)
            .scale(0.95)
            .next_to(sottotitolo_4, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_4), FadeIn(block_fs), run_time=1.5)

        # Sincronizzazione finale calcolata dinamicamente per chiudere insieme alla traccia audio
        tempo_speso = (
            1.5
            + 1.5
            + 1.5
            + max(1.0, (duration * 0.22) - 4.5)
            + 0.8
            + 0.5
            + 1.5
            + 1.0
            + max(1.0, (duration * 0.23) - 3.0)
            + 0.8
            + 1.5
            + max(1.0, (duration * 0.22) - 1.5)
            + 0.8
            + 1.5
        )
        tempo_rimanente = duration - tempo_speso
        scene.wait(max(1.0, tempo_rimanente))

        # Dissolvenza totale per fine capitolo 4
        scene.play(
            FadeOut(titolo), FadeOut(sottotitolo_4), FadeOut(block_fs), run_time=1.0
        )
