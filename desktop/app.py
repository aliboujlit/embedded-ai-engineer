"""Application Desktop complète EAI — point d'entrée de l'interface graphique."""

from __future__ import annotations

from desktop.main_window import MainWindow
from desktop.viewer.viewer import EngineeringViewer


class EAIDesktopApp:
    """Application Desktop EAI : fenêtre principale + viewer d'ingénierie."""

    def __init__(self, project_id: str, viewer: EngineeringViewer | None = None) -> None:
        self.project_id = project_id
        self.viewer = viewer or EngineeringViewer()
        self.window: MainWindow | None = None

    def run(self) -> MainWindow:
        """Crée et retourne la fenêtre principale chargée sur le projet."""
        self.window = MainWindow(project_id=self.project_id, viewer=self.viewer)
        return self.window
