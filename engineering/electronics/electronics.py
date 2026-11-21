"""Gestion de la conception électronique (schéma, calculs, règles)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ElectronicDesign:
    """Conception électronique d'un projet."""

    project_id: str
    schematic_ref: str | None = None
    design_rules: list[str] = field(default_factory=list)
    calculations: list[dict] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ElectronicsManager:
    """Enregistre et consulte les conceptions électroniques."""

    def __init__(self) -> None:
        self._designs: dict[str, ElectronicDesign] = {}

    def create(self, design: ElectronicDesign) -> ElectronicDesign:
        """Enregistre une conception électronique."""
        self._designs[design.project_id] = design
        return design

    def get(self, project_id: str) -> ElectronicDesign | None:
        """Récupère la conception électronique d'un projet."""
        return self._designs.get(project_id)
