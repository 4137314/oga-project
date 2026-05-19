from manim import *


class IntroSlide:
    title: str = "1. INQUADRAMENTO STRATEGICO E BENCHMARK FY 2025"
    voice_id: str = "it-IT-DiegoNeural"

    # Sintesi delle note dei due frame LaTeX in un unico flusso TTS continuo
    tts_text: str = (
        "In questa presentazione analizzeremo come il mercato energetico globale stia affrontando una "
        "complessità strutturale senza precedenti. I modelli tradizionali sono obsoleti a causa di tre "
        "driver di disruption: la forte volatilità dei prezzi all'ingrosso, le spinte normative sulla "
        "decarbonizzazione e, soprattutto, la digitalizzazione. Per questo motivo, il progetto propone un "
        "approccio metodologico basato su KPI multidimensionali, capace di unire la stabilità finanziaria "
        "all'evoluzione dell'asset base tecnologico. Assumiamo i dati reali del bilancio dell'anno fiscale "
        "duemilaventicinque di Enel come benchmark di riferimento per testare sul campo questo framework. "
        "Da un lato vedremo come la stabilità dei margini dipenda dall'isolamento dal rischio merchant; "
        "dall'altro, dimostreremo come l'infrastruttura di rete digitale sia il vero motore di "
        "fidelizzazione del cliente. Ricordo che ogni solida valutazione industriale non può prescindere "
        "da una mappatura rigorosa delle variabili macroeconomiche dei mercati in cui l'azienda opera."
    )

    def render_assets(self, scene: Scene, duration: float) -> None:
        # 1. Setup del Titolo (Fix LaTeX string superato con successo)
        titolo = Title(self.title, color=BLUE_A).scale(0.8)
        scene.play(Write(titolo), run_time=1.5)

        # 2. Render del primo blocco: DRIVER DI DISRUPTION (Equivalente al primo Frame LaTeX)
        sottotitolo_1 = Text(
            "Il Nuovo Paradigma Energetico", font_size=20, color=GRAY_B
        ).next_to(titolo, DOWN, buff=0.2)

        # Creazione di una lista testuale per i bullet points del LaTeX
        bullet_points = (
            VGroup(
                Text(
                    "• Volatilità estrema dei prezzi wholesale",
                    font_size=16,
                    color=WHITE,
                ),
                Text(
                    "• Imperativi di decarbonizzazione globali",
                    font_size=16,
                    color=WHITE,
                ),
                Text(
                    "• Evoluzione tecnologica e decentralizzazione",
                    font_size=16,
                    color=WHITE,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(sottotitolo_1, DOWN, buff=0.4)
        )

        scene.play(FadeIn(sottotitolo_1), run_time=0.8)
        scene.play(
            AnimationGroup(*[Write(bp) for bp in bullet_points], lag_ratio=0.3),
            run_time=2.5,
        )
        scene.wait(max(1.0, (duration / 2) - 4.8))

        # Svuota lo schermo centrale lasciando solo il titolo fisso per il secondo frame
        scene.play(FadeOut(sottotitolo_1), FadeOut(bullet_points), run_time=0.8)

        # 3. Render del secondo blocco: COLONNE BENCHMARK ENEL FY 2025 (Equivalente al secondo Frame LaTeX)
        sottotitolo_2 = Text(
            "Benchmark Industriale: Enel FY 2025", font_size=20, color=PURPLE_A
        ).next_to(titolo, DOWN, buff=0.2)

        # Colonna Sinistra: Resilienza Finanziaria
        col_sinistra = VGroup(
            Text("RESILIENZA FINANZIARIA", font_size=15, color=BLUE_B),
            Text(
                "Capacità di stabilizzazione dei\nmargini isolandoli dalle\nfluttuazioni esogene.",
                font_size=13,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # Colonna Destra: Infrastruttura Digitale
        col_destra = VGroup(
            Text("INFRASTRUTTURA DIGITALE", font_size=15, color=GREEN_B),
            Text(
                "Fulcro per abilitare i flussi\nregolati e la fidelizzazione\ndell'utente finale.",
                font_size=13,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # Posizionamento orizzontale a colonne (stile Beamer \\begin{columns})
        colonne = (
            VGroup(col_sinistra, col_destra)
            .arrange(RIGHT, buff=1.5)
            .next_to(sottotitolo_2, DOWN, buff=0.5)
        )

        scene.play(FadeIn(sottotitolo_2), run_time=0.8)
        scene.play(FadeIn(colonne), run_time=1.5)

        # Tempo residuo calcolato dinamicamente sulla traccia audio per questa slide
        tempo_rimanente = duration - (1.5 + 0.8 + 2.5 + 0.8 + 0.8 + 1.5)
        scene.wait(max(1.0, tempo_rimanente))

        # Transizione di chiusura verso la slide successiva
        scene.play(
            FadeOut(titolo), FadeOut(sottotitolo_2), FadeOut(colonne), run_time=1.0
        )
