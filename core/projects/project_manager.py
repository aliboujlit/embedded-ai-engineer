"""Gestion des projets d'ingénierie (Project Manager)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class EngineeringProject:
    """Projet d'ingénierie électronique (de la spec au dossier de réalisation)."""

    id: str
    name: str
    maturity_level: str | None = None  # L0 → L7
    status: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ProjectManager:
    """Enregistre et consulte les projets d'ingénierie."""

    def __init__(self) -> None:
        self._projects: dict[str, EngineeringProject] = {}

    def create(self, project: EngineeringProject) -> EngineeringProject:
        """Enregistre un projet."""
        self._projects[project.id] = project
        return project

    def get(self, project_id: str) -> EngineeringProject | None:
        """Récupère un projet par son identifiant."""
        return self._projects.get(project_id)

    def list(self) -> list[EngineeringProject]:
        """Liste tous les projets."""
        return list(self._projects.values())
