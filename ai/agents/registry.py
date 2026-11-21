"""Registre des agents spécialisés (EAI-AGT-xxx) et coordination."""

from __future__ import annotations

from ai.agents.agent import Agent


class AgentRegistry:
    """Registre des agents spécialisés et résolveur d'agents."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, agent_id: str, agent: Agent) -> None:
        """Enregistre un agent spécialisé sous son identifiant."""
        self._agents[agent_id] = agent

    def get(self, agent_id: str) -> Agent | None:
        """Récupère un agent par son identifiant."""
        return self._agents.get(agent_id)

    def list(self) -> list[Agent]:
        """Liste tous les agents enregistrés."""
        return list(self._agents.values())
