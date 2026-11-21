"""Gestion de la préparation à la fabrication (Gerber, BOM, Pick-and-Place, assemblage)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ManufacturingPackage:
    """Package de fabrication d'un projet."""

    project_id: str
    gerber_ref: str | None = None
    bom_ref: str | None = None
    pick_and_place_ref: str | None = None
    assembly_ref: str | None = None
    status: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ManufacturingManager:
    """Enregistre et consulte les packages de fabrication."""

    def __init__(self) -> None:
        self._packages: dict[str, ManufacturingPackage] = {}

    def create(self, package: ManufacturingPackage) -> ManufacturingPackage:
        """Enregistre un package de fabrication."""
        self._packages[package.project_id] = package
        return package

    def get(self, project_id: str) -> ManufacturingPackage | None:
        """Récupère le package de fabrication d'un projet."""
        return self._packages.get(project_id)
