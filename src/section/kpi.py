from manim import *


class KpiSlide(Scene):  # <--- Questo nome deve essere identico
    title: str = "KPI OPERATIVI E VALUTAZIONE FINANZIARIA"
    voice_id: str = "it-IT-DiegoNeural"

    # Traccia TTS a zero-difetti fonetici ottimizzata per Diego (Stile HOLOS/)
    tts_text: str = (
        "Entriamo nel vivo della Sezione tre analizzando i Chìi Màrket Draiver che condizionano le performance "
        "operative del gruppo Enel nel corso dell'anno fiscale duemilaventicinque. Come vedete dalla matrice proiettata, "
        "ci muoviamo in scenari caratterizzati da profonde asimmetrie nelle aree Tier uan. Prima di valutare le divergenze "
        "strategiche dei singoli paesi, apro questo alèrt di scenario fondamentale: il bilancio consolidato deve fare i "
        "conti con un'esposizione effe iks significativa di ben dodici virgola sette miliardi di euro. Questo rende l'analisi "
        "dei tassi di ci pi ai e dei tassi di interesse locali una priorità per la nostra intèlligens finanziaria. "
        "Esaminando le asimmetrie di scenario, l'Ibèria si posiziona come il mercato ideale dell'area euro: l'ottimo andamento "
        "del pil si riflette in una crescita della domanda stabile accoppiata a costi spot competitivi a sessantacinque virgola "
        "cinque euro per megawattora. Al polo opposto si colloca l'Italia: la domanda è stagnante per via della debolezza del "
        "contesto macroeconomico dello zero virgola sessantacinque per cento, ma i prezzi spot rimangono i più alti d'Europa "
        "a centoquindici virgola tre euro a causa del mics energetico nazionale. Gli Stati Uniti, con oltre quattromilacinquecento "
        "Terawattora di domanda, ridefiniscono i volumi complessivi dell'attività del gruppo. La logica strategica che la "
        "commissione deve valutare è che la diversificazione di Enel funge da èg naturale: le inefficienze o i rallentamenti "
        "macroeconomici di un singolo paese come l'Italia vengono assorbiti e compensati dalla scala operativa degli altri "
        "asset geografici. Introduciamo ora la performance finanziaria per capire l'impatto di questo bilanciamento sul bilancio consolidato."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # Griglia informativa (Sostituzione Table per compatibilità)
        headers = ["Area", "GDP %", "CPI %", "Spot", "Demand"]
        data = [
            ["IT", "0.65", "1.63", "115.3", "311.3"],
            ["IB", "2.80", "2.69", "65.5", "320.7"],
            ["BR", "2.28", "5.02", "31.9", "754.4"],
            ["CL", "2.40", "4.21", "53.3", "85.1"],
            ["US", "2.20", "2.72", "--", "4503.8"],
        ]

        grid = VGroup()
        for i, row in enumerate([headers] + data):
            row_group = VGroup(
                *[
                    Text(cell, font_size=16, color=WHITE if i > 0 else BLUE_B)
                    for cell in row
                ]
            )
            row_group.arrange(RIGHT, buff=0.6)
            grid.add(row_group)
        grid.arrange(DOWN, buff=0.3).scale(0.8).next_to(titolo, DOWN, buff=0.5)

        alert_box = VGroup(
            Text(
                "⚠️ ALERT: RISCHIO DI CAMBIO (FX EXPOSURE)",
                font_size=13,
                color=RED_A,
                weight=BOLD,
            ),
            Text(
                "Il Gruppo conta €12,7 miliardi esposti. Monitoraggio CPI e tassi locali critico.",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        alert_block = (
            VGroup(
                SurroundingRectangle(
                    alert_box, color=RED_A, buff=0.2, fill_color=BLACK, fill_opacity=0.8
                ),
                alert_box,
            )
            .scale(0.95)
            .to_edge(DOWN, buff=0.4)
        )

        scene.play(FadeIn(grid), run_time=1.5)
        scene.play(FadeIn(alert_block), run_time=1.0)
        scene.wait(max(1.0, (duration * 0.42) - 6.5))
        scene.play(FadeOut(grid), FadeOut(alert_block), run_time=0.8)

        # FASE 2: Divergenze Strategiche
        sottotitolo = Text(
            "Valutazione delle Divergenze Strategiche", font_size=18, color=PURPLE_A
        ).next_to(titolo, DOWN, buff=0.2)

        def create_card(title, body, color):
            return VGroup(
                Text(title, font_size=13, color=color, weight=BOLD),
                Text(body, font_size=11, color=WHITE),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        confronto_geografie = (
            VGroup(
                create_card(
                    "IBERIA",
                    "• Crescita robusta\n• Domanda: 320.7 TWh\n• Prezzi: €65.5/MWh",
                    GREEN_B,
                ),
                create_card(
                    "ITALIA",
                    "• PIL: 0.65%\n• Domanda stagnante\n• Prezzi: €115.3/MWh",
                    ORANGE,
                ),
                create_card(
                    "USA",
                    "• Scala globale\n• Domanda: 4503.8 TWh\n• Hub capitali",
                    BLUE_B,
                ),
            )
            .arrange(RIGHT, buff=0.6)
            .next_to(sottotitolo, DOWN, buff=0.4)
        )

        hedge_box = VGroup(
            Text(
                "🛡️ HEDGE NATURALE DI GRUPPO", font_size=13, color=GREEN_A, weight=BOLD
            ),
            Text(
                "La diversificazione geografica compensa gli shock locali.",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        hedge_block = (
            VGroup(
                SurroundingRectangle(
                    hedge_box,
                    color=GREEN_A,
                    buff=0.2,
                    fill_color=BLACK,
                    fill_opacity=0.8,
                ),
                hedge_box,
            )
            .scale(0.95)
            .to_edge(DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo), FadeIn(confronto_geografie), run_time=1.5)
        scene.play(FadeIn(hedge_block), run_time=1.0)

        tempo_speso = (
            1.5
            + 1.5
            + 2.5
            + 1.0
            + ((duration * 0.42) - 6.5)
            + 0.8
            + 0.5
            + 1.5
            + 2.5
            + 1.0
        )
        scene.wait(max(1.0, duration - tempo_speso))
        scene.play(
            FadeOut(titolo),
            FadeOut(sottotitolo),
            FadeOut(confronto_geografie),
            FadeOut(hedge_block),
            run_time=1.0,
        )
