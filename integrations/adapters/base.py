"""Interface commune des adaptateurs d'outils d'ingénierie."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class EngineeringToolAdapter(ABC):
    """Interface normalisée d'un outil externe (KiCad, STM32CubeMX, Renode, ...)."""

    @abstractmethod
    def get_capabilities(self) -> list[str]:
        """Liste les opérations supportées par l'outil."""

    @abstractmethod
    def execute(self, operation: str, params: dict[str, Any]) -> dict[str, Any]:
        """Exécute une opération auprès de l'outil externe."""
