from manim import *


class TransitionSlide:
    title: str = "5. LA TRANSIZIONE DIGITALE: GRIDS E SMART METERING"
    voice_id: str = "it-IT-DiegoNeural"

    # Traccia TTS fonetica continua ottimizzata per la dizione di Diego (Stile HOLOS/)
    tts_text: str = (
        "Entriamo nella Sezione cinque, dedicata alla transizione digitale. Come abbiamo anticipato, "
        "la digitalizzazione delle reti è l'architrave strategica di Enel. L'azienda ha stanziato un càpecs "
        "imponente di quarantasette virgola cinque miliardi di euro per l'ammodernamento e la resilienza delle grìds. "
        "Vediamo la vera ràtio finanziaria di questo investimento: ogni euro speso nelle reti espande la "
        "Regulatori Asset Beis, ovvero la ràb, cresciuta infatti del dieci per cento in Italia e in Ibèria. Per l'analista "
        "questo significa una cosa sola: trasformare la spesa iniziale in flussi di cassa certi, regolati e garantiti "
        "dalle autorità. L'obiettivo finale di sistema è creare un isolamento strutturale dalla volatilità dei prezzi di borsa, "
        "ancorando i margini a asset protetti. Il pilastro di questa infrastruttura a contatto con l'utente finale è il "
        "contatore smart di seconda generazione, il due gì. Dal punto di vista ingegneristico, parliamo di dispositivi "
        "con monitoraggio in tempo reale e campionamento dei dati con una granularità di quindici minuti. Questa mole "
        "di dati consente modelli di bùsiness innovativi. Il pruf of concèpt i bòcs, ad esempio, agisce come una banca "
        "digitale del risparmio energetico: valorizza economicamente i chilovattora non consumati, rendendo l'utente un "
        "prošùmer attivo e vincolando la sua fidelizzazione all'ecosistema digitale di Enel. Come si riflette questo sul "
        "bilancio? Per l'analista, un utente ingaggiato e fidelizzato riduce drasticamente il čarn rèit e azzera le morosità, "
        "contraendo la voce del bèd dètt, che storicamente pesa sulle utìliti. Dimostriamo così che la tecnologia ottimizza "
        "capillarmente le metriche finanziarie di basso livello."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Setup Titolo Principale della Slide
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # ==============================================================================
        # FASE 1: INVESTIMENTI NELLE INFRASTRUTTURE DI RETE (GRIDS)
        # ==============================================================================
        sottotitolo_1 = Text(
            "Digitalizzazione delle Reti e Flussi Regolati", font_size=18, color=GRAY_B
        ).next_to(titolo, DOWN, buff=0.2)

        # Blocco Sinistro: Capex Grids
        box_capex = VGroup(
            Text(
                "📊 CAPEX GRIDS: €47,5 MILIARDI",
                font_size=12,
                color=BLUE_B,
                weight=BOLD,
            ),
            Text(
                "Capitale massiccio per la\nresilienza di rete e l'integrazione\ndi fonti rinnovabili intermittenti.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_capex = SurroundingRectangle(
            box_capex,
            color=BLUE_C,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_capex = VGroup(bg_capex, box_capex)

        # Blocco Destro: Sostentamento Margini (RAB)
        box_rab = VGroup(
            Text(
                "📈 SOSTENTAMENTO DEI MARGINI", font_size=12, color=GREEN_B, weight=BOLD
            ),
            Text(
                "Incremento RAB (+10% in Italia).\nTrasformazione del Capex in flussi\ndi cassa regolati e prevedibili.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_rab = SurroundingRectangle(
            box_rab,
            color=GREEN_C,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_rab = VGroup(bg_rab, box_rab)

        layout_grids = (
            VGroup(card_capex, card_rab)
            .arrange(RIGHT, buff=0.8)
            .next_to(sottotitolo_1, DOWN, buff=0.4)
        )

        desc_grids = Text(
            "Obiettivo di Sistema: Isolamento strutturale dalla volatilità dei mercati wholesale energetici.",
            font_size=12,
            color=GRAY_C,
        ).to_edge(DOWN, buff=0.5)

        scene.play(FadeIn(sottotitolo_1), FadeIn(layout_grids), run_time=1.5)
        scene.play(Write(desc_grids), run_time=1.0)

        # Sincronizzazione per coprire la trattazione delle Grids (circa il 42% della durata totale)
        scene.wait(max(1.0, (duration * 0.42) - 4.0))
        scene.play(
            FadeOut(sottotitolo_1),
            FadeOut(layout_grids),
            FadeOut(desc_grids),
            run_time=0.8,
        )

        # ==============================================================================
        # FASE 2: IL CONTATORE 2G E L'ECOSISTEMA E-BOX
        # ==============================================================================
        sottotitolo_2 = Text(
            "Smart Metering 2G: Blueprint Tecnologico", font_size=18, color=PURPLE_A
        ).next_to(titolo, DOWN, buff=0.2)

        # Specifiche e Proof of Concept (Spacer risolto con VMobject nativo)
        specifiche_tech = (
            VGroup(
                Text(
                    "⚙️ SPECIFICHE TECNICHE CONTATORE 2G",
                    font_size=12,
                    color=ORANGE,
                    weight=BOLD,
                ),
                Text(
                    "• Monitoraggio in tempo reale.\n• Campionamento granulare ogni 15 minuti.",
                    font_size=11,
                    color=WHITE,
                ),
                VMobject().set_height(0.1),  # Corretto errore Mypy
                Text(
                    "💡 PROOF OF CONCEPT: E-BOX",
                    font_size=12,
                    color=BLUE_B,
                    weight=BOLD,
                ),
                Text(
                    "• Digital saving bank del risparmio energetico.\n• Valorizzazione economica dei kWh non consumati.\n• Fidelizzazione dell'utente attivo (Prosumer).",
                    font_size=11,
                    color=WHITE,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .scale(0.95)
        )

        # Blocco Analista Finanziario: Impatto su Bad Debt
        box_bad_debt = VGroup(
            Text("🛡️ IMPATTO PER L'ANALISTA", font_size=12, color=RED_A, weight=BOLD),
            Text(
                "Il coinvolgimento digitale dell'utente\nsi traduce direttamente in:\n\n• Contrazione drastica del Bad Debt\n  (crediti deteriorati morosi).\n• Abbattimento del Churn Rate\n  (tasso di perdita dei clienti).",
                font_size=10,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        bg_bad_debt = SurroundingRectangle(
            box_bad_debt,
            color=RED_A,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_bad_debt = VGroup(bg_bad_debt, box_bad_debt).scale(0.95)

        layout_metering = (
            VGroup(specifiche_tech, block_bad_debt)
            .arrange(RIGHT, buff=0.8)
            .next_to(sottotitolo_2, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_2), run_time=0.5)
        scene.play(FadeIn(layout_metering), run_time=1.5)

        # Calcolo dinamico esatto per la chiusura millimetrica della scena con l'audio
        tempo_speso = (
            1.5 + 1.5 + 1.0 + max(1.0, (duration * 0.42) - 4.0) + 0.8 + 0.5 + 1.5
        )
        tempo_rimanente = duration - tempo_speso
        scene.wait(max(1.0, tempo_rimanente))

        # Dissolvenza totale per fine capitolo 5 e passaggio alle conclusioni
        scene.play(
            FadeOut(titolo),
            FadeOut(sottotitolo_2),
            FadeOut(layout_metering),
            run_time=1.0,
        )
