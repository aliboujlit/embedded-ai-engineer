"""Gestion de la simulation (simulateurs, modèles, paramètres, résultats)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class SimulationCase:
    """Cas de simulation exécuté dans un simulateur."""

    project_id: str
    simulator: str | None = None
    model: str | None = None
    parameters: dict = field(default_factory=dict)
    results: dict = field(default_factory=dict)
    executed_at: datetime | None = None


class SimulationManager:
    """Enregistre et consulte les cas de simulation."""

    def __init__(self) -> None:
        self._cases: dict[str, SimulationCase] = {}

    def create(self, simulation: SimulationCase) -> SimulationCase:
        """Enregistre un cas de simulation."""
        self._cases[simulation.project_id] = simulation
        return simulation

    def get(self, project_id: str) -> SimulationCase | None:
        """Récupère le cas de simulation d'un projet."""
        return self._cases.get(project_id)
