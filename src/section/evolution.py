from manim import *


class EvolutionSlide:
    title: str = "6. EVOLUZIONE ASSET MIX E CAPACITÀ INSTALLATA"
    voice_id: str = "it-IT-DiegoNeural"

    # Traccia TTS fonetica continua ottimizzata per la dizione di Diego (Stile HOLOS/)
    tts_text: str = (
        "Nella Sezione sei analizziamo l'evoluzione quantitativa del mix di generatione. Su una capacità "
        "globale di quasi ottantasette Gigauatt, l'asset di Enel vede una netta predominanza delle rinnovabili "
        "core, guidate dallo storico idroelettrico e dai progressi di eolico e solare. Spostando l'attenzione "
        "sul secondo punto, sottolineo il ruolo dei tremilaquattrocentoquarantuno Megauatt di stòreg a batterie bèss. "
        "Non sono solo infrastrutture passive: sono il perno fondamentale che abilita il dispacciamento delle "
        "rinnovabili, gestendone l'intermittenza strutturale sulla rete. A destra, il blocco di allerta evidenzia "
        "l'effetto immediato di questo scift: il carbone crolla ad appena quattromilaseicentoventisette Megauatt, "
        "decretando il feis aut quasi definitivo delle vecchie centrali termiche mèrčant sul mercato europeo. "
        "Questa transizione non avviene in modo uniforme, ma segue una precisa specializzazione geografica nelle "
        "aree Tier uan per ottimizzare i ritorni del capitale. Negli Stati Uniti, Enel sfrutta gli schemi regolatori "
        "favorevoli concentrando oltre il cinquanta per cento di tutto il suo asset eolico mondiale, con più di sei "
        "Gigauatt di uìnd in produzione attiva sul territorio. In Italia, al contrario, valorizza la sua storica "
        "flessibilità idrica controllando quasi tredici Gigauatt di idroelettrico: asset interamente ammortizzati "
        "capaci di estrarre margini elevatissimi nel mercato dei servizi di bilanciamento europeo. Questa solidità "
        "industriale ci porta direttamente alle conclusioni metodologiche del nostro studio."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Configurazione Iniziale del Titolo di Sezione
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # ==============================================================================
        # FASE 1: MIX PRODUTTIVO E SISTEMI DI STOCCAGGIO (Primo Frame LaTeX)
        # ==============================================================================
        sottotitolo_1 = Text(
            "Ripartizione Energetica e Storage BESS", font_size=18, color=GRAY_B
        ).next_to(titolo, DOWN, buff=0.2)

        # Colonna Sinistra: Breakdown Capacità Installata (Spacer gestito con oggetti nativi VMobject)
        col_mix = (
            VGroup(
                Text(
                    "📊 RIPARTIZIONE DELL'ASSET MIX (86.986 MW)",
                    font_size=12,
                    color=BLUE_B,
                    weight=BOLD,
                ),
                Text(
                    "• Renewables Core:\n  Idro (28.320 MW) | Eolico (16.184 MW) | Solare (13.059 MW)",
                    font_size=11,
                    color=WHITE,
                ),
                VMobject().set_height(0.12),
                Text(
                    "🔋 STORAGE (BESS) - ABILITATORE CRITICO",
                    font_size=12,
                    color=GREEN_B,
                    weight=BOLD,
                ),
                Text(
                    "• 3.441 MW dedicati alla stabilità e alla\n  gestione dinamica delle intermittenze di rete.",
                    font_size=11,
                    color=WHITE,
                ),
                VMobject().set_height(0.12),
                Text(
                    "⚙️ SUPPORTO E BILANCIAMENTO",
                    font_size=12,
                    color=GRAY_B,
                    weight=BOLD,
                ),
                Text(
                    "• CCGT: 12.420 MW | Nucleare: 3.328 MW", font_size=11, color=WHITE
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            .scale(0.95)
        )

        # Colonna Destra: Alert Box Phase-out Carbone
        box_carbone = VGroup(
            Text("⚠️ PHASE-OUT FOSSILI", font_size=12, color=RED_A, weight=BOLD),
            Text(
                "La capacità residua a Carbone\nscende radicalmente a 4.627 MW.\n\nDeclino irreversibile della\ngenerazione termica tradizionale\nmerchant sul mercato europeo.",
                font_size=10,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        bg_carbone = SurroundingRectangle(
            box_carbone,
            color=RED_A,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        block_carbone = VGroup(bg_carbone, box_carbone).scale(0.95)

        layout_mix = (
            VGroup(col_mix, block_carbone)
            .arrange(RIGHT, buff=0.8)
            .next_to(sottotitolo_1, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_1), run_time=0.5)
        scene.play(FadeIn(col_mix), run_time=1.5)
        scene.play(FadeIn(block_carbone), run_time=1.0)

        # Sincronizzazione dinamica per la prima parte del mix (circa il 45% del video)
        scene.wait(max(1.0, (duration * 0.45) - 4.5))
        scene.play(FadeOut(sottotitolo_1), FadeOut(layout_mix), run_time=0.8)

        # ==============================================================================
        # FASE 2: SPECIALIZZAZIONE GEOGRAFICA TIER 1 (Secondo Frame LaTeX)
        # ==============================================================================
        sottotitolo_2 = Text(
            "Specializzazione Geografica nelle Aree Tier 1",
            font_size=18,
            color=PURPLE_A,
        ).next_to(titolo, DOWN, buff=0.2)

        # Blocco USA
        box_usa = VGroup(
            Text("🇺🇸 USA: SCALABILITÀ EOLICA", font_size=12, color=ORANGE, weight=BOLD),
            Text(
                "• Concentrazione di oltre il 50% della\n  capacità eolica globale del Gruppo.\n• 6.218 MW Wind attivi sul territorio.\n• Sfruttamento di schemi regolatori e\n  regimi di incentivazione favorevoli.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_usa = SurroundingRectangle(
            box_usa,
            color=ORANGE,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_usa = VGroup(bg_usa, box_usa)

        # Blocco Italia
        box_italia = VGroup(
            Text(
                "🇮🇹 ITALIA: FLESSIBILITÀ IDRICA",
                font_size=12,
                color=BLUE_B,
                weight=BOLD,
            ),
            Text(
                "• Roccaforte storica dell'idroelettrico\n  con ben 12.994 MW installati.\n• Asset interamente ammortizzati.\n• Generazione di margini elevati nel\n  mercato dei servizi di bilanciamento.",
                font_size=11,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bg_italia = SurroundingRectangle(
            box_italia,
            color=BLUE_B,
            buff=0.2,
            stroke_width=1,
            fill_color=BLACK,
            fill_opacity=0.8,
        )
        card_italia = VGroup(bg_italia, box_italia)

        layout_geo = (
            VGroup(card_usa, card_italia)
            .arrange(RIGHT, buff=0.8)
            .next_to(sottotitolo_2, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_2), FadeIn(layout_geo), run_time=1.5)

        # Allineamento al millisecondo hardware della timeline per chiudere insieme all'audio
        tempo_speso = (
            1.5 + 0.5 + 1.5 + 1.0 + max(1.0, (duration * 0.45) - 4.5) + 0.8 + 1.5
        )
        tempo_rimanente = duration - tempo_speso
        scene.wait(max(1.0, tempo_rimanente))

        # Svuotamento e dissolvenza di chiusura slide
        scene.play(
            FadeOut(titolo), FadeOut(sottotitolo_2), FadeOut(layout_geo), run_time=1.0
        )
