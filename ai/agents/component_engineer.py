"""Agent de sélection et qualification des composants — Component Engineer (AG-005)."""

from __future__ import annotations

from ai.agents.agent import Agent


class ComponentEngineerAgent(Agent):
    """Agent chargé de la sélection et qualification des composants (AG-005)."""

    def name(self) -> str:
        return "AG-005"

    def run(self, task: str) -> str:
        # Sélection justifiée des composants et alternatives.
        # TODO : brancher sur le runtime IA local via le Master Engineer.
        return f"[stub] Sélection de composants pour la tâche : {task}"
