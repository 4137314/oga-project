from typing import Protocol, runtime_checkable
from manim import Scene


@runtime_checkable
class SlideModule(Protocol):
    """Protocollo statico (PEP 544) per la validazione formale delle sezioni d'esame."""

    @property
    def title(self) -> str: ...

    @property
    def tts_text(self) -> str: ...

    @property
    def voice_id(self) -> str: ...

    def render_assets(self, scene: Scene, duration: float) -> None:
        """Contratto vincolante per l'esecuzione della grafica vettoriale del modulo."""
        ...
