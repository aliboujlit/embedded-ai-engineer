"""Fondation de l'application Desktop EAI (EAI Desktop / PyQt6)."""

from __future__ import annotations

from desktop.viewer.viewer import EngineeringViewer, ProjectProgress


class MainWindow:
    """Fenêtre principale de l'application EAI Desktop.

    Affiche la progression d'un projet : exigences, architecture, électronique,
    EDA, MCU, firmware, simulation, tests, fabrication.
    """

    def __init__(self, project_id: str, viewer: EngineeringViewer) -> None:
        self.project_id = project_id
        self.viewer = viewer
        self.progress: ProjectProgress | None = None

    def load(self) -> ProjectProgress:
        """Charge et assemble la vue de progression du projet."""
        self.progress = self.viewer.view(self.project_id)
        return self.progress

    def summary(self) -> str:
        """Retourne un résumé textuel de la progression."""
        progress = self.load()
        return (
            f"Projet {progress.project_id} — "
            f"{len(progress.requirements)} exigence(s), "
            f"{progress.architecture_blocks} bloc(s) architectural(aux), "
            f"électronique: {progress.electronics}, EDA: {progress.eda}, "
            f"MCU: {progress.mcu}, firmware: {progress.firmware}, "
            f"simulation: {progress.simulation}, tests: {progress.testing}, "
            f"fabrication: {progress.manufacturing}"
        )
