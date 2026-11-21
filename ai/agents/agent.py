"""Interface générique d'un agent spécialisé de l'IA multi-agents."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Agent(ABC):
    """Interface commune des agents spécialisés (AG-xxx)."""

    @abstractmethod
    def name(self) -> str:
        """Identifiant unique de l'agent."""

    @abstractmethod
    def run(self, task: str) -> str:
        """Exécute une tâche et retourne une conclusion."""
