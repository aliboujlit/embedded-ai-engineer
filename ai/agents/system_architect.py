"""Agent d'architecture système — System Architect (AG-003)."""

from __future__ import annotations

from ai.agents.agent import Agent


class SystemArchitectAgent(Agent):
    """Agent chargé de l'architecture globale (AG-003)."""

    def name(self) -> str:
        return "AG-003"

    def run(self, task: str) -> str:
        # Décomposition du besoin en architecture système.
        # TODO : brancher sur le runtime IA local via le Master Engineer.
        return f"[stub] Architecture générée pour la tâche : {task}"
