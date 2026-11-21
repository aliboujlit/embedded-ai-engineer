"""Gestion de l'ingénierie EDA (schéma, ERC, PCB, DRC, BOM)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class EDADesign:
    """Conception EDA (schéma, PCB, vérifications)."""

    project_id: str
    schematic_ref: str | None = None
    pcb_ref: str | None = None
    erc_status: str | None = None
    drc_status: str | None = None
    bom_ref: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EDAAdministrator:
    """Enregistre et consulte les conceptions EDA d'un projet."""

    def __init__(self) -> None:
        self._designs: dict[str, EDADesign] = {}

    def create(self, design: EDADesign) -> EDADesign:
        """Enregistre une conception EDA."""
        self._designs[design.project_id] = design
        return design

    def get(self, project_id: str) -> EDADesign | None:
        """Récupère la conception EDA d'un projet."""
        return self._designs.get(project_id)
