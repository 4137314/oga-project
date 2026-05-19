from manim import *


class ConclusionSlide:
    title: str = "7. CONCLUSIONI: SINTESI METODOLOGICA PER L'ANALISTA"
    voice_id: str = "it-IT-DiegoNeural"

    # Traccia TTS fonetica continua ottimizzata per la dizione istituzionale di Diego (Stile HOLOS/)
    tts_text: str = (
        "Arriviamo alla sintesi metodologica di questa trattazione. Il caso Enel ci offre una lezione fondamentale: "
        "valutare una moderna utìliti guardando solo l'ebitdà o i flussi finanziari tradizionali è un errore. "
        "Quell'ebitdà da ventidue virgola nove miliardi è solido solo perché poggia su un'estesa base infrastrutturale "
        "regolata e digitalizzata. Per esportare questo modello di analisi su altri plèier del mercato, propongo tre "
        "direttrici tecniche replicabili. La prima è la Visibilità Regolatoria: analizzare quanto il uàcc sia protetto "
        "dalle variazioni dei tassi di interesse in base alle espansioni della ràb. La seconda è il comòditi insulèišon rèit, "
        "ovvero quantificare con precisione quanta parte del margine complessivo sia del tutto immune dalle oscillazioni di borsa "
        "rispetto alle vecchie logiche mèrčant. La terza è la monetizzazione dei servizi digitali vàs, misurando l'impatto di smart "
        "mìter due gì e bèss sulla riduzione dei costi operativi e del credito deteriorato, il bèd dètt. In conclusione, la "
        "trasformazione industriale analizzata indica che la sopravvivenza e la profittabilità del settore risiedono nella "
        "capacità di coniugare un ferreo rigore finanziario con la centralità strategica del dato ingegneristico e tecnologico. "
        "Vi ringrazio per l'attenzione e sono a disposizione per qualsiasi domanda o approfondimento."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Setup Titolo Conclusivo
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # Assunto iniziale di framework
        assunto = Text(
            "La valutazione delle Utility moderne deve trascendere il dato finanziario isolato:\n"
            "la stabilità dell'EBITDA (€22,9bn) è vincolata alla digitalizzazione dell'Asset Base.",
            font_size=12,
            color=GRAY_C,
        ).next_to(titolo, DOWN, buff=0.3)
        scene.play(FadeIn(assunto), run_time=1.0)

        # ==============================================================================
        # TRE DIRETTRICI TECNICHE DI VALUTAZIONE (Enumera il blocco Beamer)
        # ==============================================================================
        card_1 = VGroup(
            Text("1. VISIBILITÀ REGOLATORIA", font_size=12, color=BLUE_B, weight=BOLD),
            Text(
                "Impatto dei quadri normativi nazionali sul WACC in relazione alla crescita della RAB.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        card_2 = VGroup(
            Text(
                "2. COMMODITY INSULATION RATE",
                font_size=12,
                color=PURPLE_B,
                weight=BOLD,
            ),
            Text(
                "Quota di margine protetta da asset regolati rispetto alla generazione esposta al rischio merchant.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        card_3 = VGroup(
            Text(
                "3. MONETIZZAZIONE DEI DIGITAL VAS",
                font_size=12,
                color=GREEN_B,
                weight=BOLD,
            ),
            Text(
                "Impatto delle tecnologie smart (2G, BESS) sulla contrazione del rischio commerciale (Bad Debt).",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        direttrici_group = (
            VGroup(card_1, card_2, card_3)
            .arrange(DOWN, buff=0.35, aligned_edge=LEFT)
            .next_to(assunto, DOWN, buff=0.4)
        )

        # Mostra le tre direttrici in sequenza controllata
        for card in direttrici_group:
            scene.play(FadeIn(card, shift=RIGHT * 0.2), run_time=0.8)
            scene.wait(1.5)

        # ==============================================================================
        # BLOCCO CONCLUSIVO & RINGRAZIAMENTI
        # ==============================================================================
        box_conclusione = VGroup(
            Text("🎯 STRATEGIA UNIFICATA", font_size=12, color=GOLD, weight=BOLD),
            Text(
                "Il futuro del settore risiede nella capacità di coniugare il rigore finanziario alla centralità del dato tecnologico.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_conc = SurroundingRectangle(
            box_conclusione,
            color=GOLD,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_conclusione = (
            VGroup(bg_conc, box_conclusione).scale(0.95).to_edge(DOWN, buff=0.4)
        )

        scene.play(FadeIn(block_conclusione), run_time=1.0)

        # Calcolo millimetrico della timeline per chiudere simultaneamente con l'ultima parola dell'audio
        tempo_speso = 1.5 + 1.0 + (3 * 0.8) + (3 * 1.5) + 1.0
        tempo_rimanente = duration - tempo_speso
        scene.wait(max(1.0, tempo_rimanente))

        # Dissolvenza finale totale della presentazione (Fade to Black)
        scene.play(
            FadeOut(titolo),
            FadeOut(assunto),
            FadeOut(direttrici_group),
            FadeOut(block_conclusione),
            run_time=1.5,
        )
