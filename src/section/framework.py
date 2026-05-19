from manim import *


class FrameworkSlide:
    title: str = "3. KPI MACROECONOMICI E INDICATORI DI SCENARIO"
    voice_id: str = "it-IT-DiegoNeural"

    # Testo fonetico ottimizzato per la dizione di Diego (Standard HOLOS/)
    tts_text: str = (
        "Entriamo nel vivo dell'analisi quantitativa osservando la mappa dei Màrket Draiver del Gruppo "
        "per l'anno fiscale duemilaventicinque. Questa tabella fotografa un contesto esogeno fortemente "
        "asimmetrico e a due velocità nelle aree geografiche Tier uan. Prima di valutare le singole aree, "
        "faccio comparire un blocco di allerta fondamentale: l'analista deve sempre considerare l'esposizione "
        "al rischio di cambio. Parliamo di ben dodici virgola sette miliardi di euro esposti alle fluttuazioni "
        "effe iks, il che rende il monitoraggio del ci pi ai e dei tassi locali un fattore critico di gestione industriale. "
        "Analizzando le divergenze strategiche, notiamo tre comportamenti distinti. L'Ibèria rappresenta lo scenario "
        "ideale: crescita robusta trainata da un pil al due virgola ottanta per cento e prezzi spot molto competitivi "
        "a sessantacinque virgola cinque euro per megawattora. Al contrario, l'Italia mostra forti criticità: i prezzi spot "
        "rimangono i più alti del paniere, a ben centoquindici virgola tre euro, ma la domanda è stagnante e frenata da una "
        "crescita macroeconomica debole dello zero virgola sessantacinque per cento. Gli Stati Uniti si confermano invece "
        "il mercato di scala con oltre quattromilacinquecento Terawattora di domanda. La sintesi per l'analista è cruciale: "
        "questa diversificazione non è casuale, ma costituisce un èg naturale. Se un mercato nazionale rallenta o subisce "
        "sciòc regolatori, la scala degli altri asset ne stabilizza i flussi complessivi."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Setup Titolo
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # 2. FASE 1: Generazione della Tabella dei KPI (Equivalente al primo Frame LaTeX)
        # Costruzione di una tabella pulita ed elegante ad alta leggibilità
        tabella = (
            Table(
                [
                    ["Italia", "0.65%", "1.63%", "115.3", "311.3"],
                    ["Iberia", "2.80%", "2.69%", "65.5", "320.7"],
                    ["Brasile", "2.28%", "5.02%", "31.9", "754.4"],
                    ["Cile", "2.40%", "4.21%", "53.3", "85.1"],
                    ["USA", "2.20%", "2.72%", "--", "4503.8"],
                ],
                row_labels=[
                    Text(r, font_size=12, weight=BOLD)
                    for r in ["IT", "IB", "BR", "CL", "US"]
                ],
                col_labels=[
                    Text("Area", font_size=12, color=BLUE_B),
                    Text("PIL", font_size=12, color=BLUE_B),
                    Text("CPI", font_size=12, color=BLUE_B),
                    Text("Spot (€/MWh)", font_size=12, color=BLUE_B),
                    Text("Demand (TWh)", font_size=12, color=BLUE_B),
                ],
                include_outer_lines=False,
                line_config={"color": GRAY_D, "stroke_width": 1},
            )
            .scale(0.65)
            .next_to(titolo, DOWN, buff=0.2)
        )

        # Blocco Alert Rischio FX (Cambio)
        alert_box = VGroup(
            Text(
                "⚠️ ALERT: ESPOSIZIONE RISCHIO FX",
                font_size=14,
                color=RED_A,
                weight=BOLD,
            ),
            Text(
                "Esposizione di 12.7 Miliardi di Euro. Monitoraggio CPI e tassi locali critico.",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Sfondo per l'alert box stile Beamer block
        alert_bg = SurroundingRectangle(
            alert_box,
            color=RED_A,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        alert_block = VGroup(alert_bg, alert_box).scale(0.9).to_edge(DOWN, buff=0.4)

        scene.play(FadeIn(tabella), run_time=1.5)
        scene.wait(2.0)
        scene.play(FadeIn(alert_block), run_time=1.0)

        # Pausa per coprire la prima parte della spiegazione del rischio cambio
        scene.wait(max(1.0, (duration * 0.45) - 6.0))

        # Pulisce l'area centrale per la seconda fase
        scene.play(FadeOut(tabella), FadeOut(alert_block), run_time=0.8)

        # 3. FASE 2: Divergenze Strategiche e Hedge Naturale (Secondo Frame LaTeX)
        sottotitolo = Text(
            "Divergenze Strategiche e Protezione Globale", font_size=18, color=PURPLE_A
        ).next_to(titolo, DOWN, buff=0.2)

        # Griglia orizzontale a 3 colonne per Iberia, Italia e USA
        card_iberia = VGroup(
            Text("IBERIA (Scenario Ideale)", font_size=13, color=GREEN_B, weight=BOLD),
            Text(
                "PIL +2.80%\nPrezzi spot competitivi\na 65.5 €/MWh.\nDomanda robusta.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        card_italia = VGroup(
            Text("ITALIA (Criticità)", font_size=13, color=ORANGE, weight=BOLD),
            Text(
                "PIL stagnante (+0.65%)\nPrezzi strutturalmente elevati\na 115.3 €/MWh.\nDomanda debole.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        card_usa = VGroup(
            Text("USA (Scala)", font_size=13, color=BLUE_B, weight=BOLD),
            Text(
                "Mercato di riferimento\nper scala dimensionale:\n4503.8 TWh.\nTarget investimenti.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        confronto_geografie = (
            VGroup(card_iberia, card_italia, card_usa)
            .arrange(RIGHT, buff=0.7)
            .next_to(sottotitolo, DOWN, buff=0.4)
        )

        # Blocco Conclusivo: Hedge Naturale
        hedge_box = VGroup(
            Text("🛡️ HEDGE NATURALE", font_size=14, color=GREEN_A, weight=BOLD),
            Text(
                "La diversificazione geografica globale stabilizza i flussi isolando il Gruppo da shock locali.",
                font_size=12,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        hedge_bg = SurroundingRectangle(
            hedge_box,
            color=GREEN_A,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        hedge_block = VGroup(hedge_bg, hedge_box).scale(0.9).to_edge(DOWN, buff=0.4)

        scene.play(FadeIn(sottotitolo), run_time=0.5)
        scene.play(FadeIn(confronto_geografie), run_time=1.5)
        scene.wait(2.0)
        scene.play(FadeIn(hedge_block), run_time=1.0)

        # Calcolo dinamico del tempo rimanente per chiudere in perfetto sincrono con la traccia audio
        tempo_speso = (
            1.5
            + 1.5
            + 2.0
            + 1.0
            + ((duration * 0.45) - 6.0)
            + 0.8
            + 0.5
            + 1.5
            + 2.0
            + 1.0
        )
        tempo_rimanente = duration - tempo_speso
        scene.wait(max(1.0, tempo_rimanente))

        # Transizione finale svuotamento scena
        scene.play(
            FadeOut(titolo),
            FadeOut(sottotitolo),
            FadeOut(confronto_geografie),
            FadeOut(hedge_block),
            run_time=1.0,
        )
