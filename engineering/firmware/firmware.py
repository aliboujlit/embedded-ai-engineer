"""Gestion de l'ingénierie firmware (sources, build, configuration)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class FirmwareProject:
    """Projet firmware associé à un MCU."""

    project_id: str
    source_ref: str | None = None
    build_system: str | None = None
    toolchain: str | None = None
    status: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class FirmwareManager:
    """Enregistre et consulte les projets firmware."""

    def __init__(self) -> None:
        self._projects: dict[str, FirmwareProject] = {}

    def create(self, project: FirmwareProject) -> FirmwareProject:
        """Enregistre un projet firmware."""
        self._projects[project.project_id] = project
        return project

    def get(self, project_id: str) -> FirmwareProject | None:
        """Récupère un projet firmware."""
        return self._projects.get(project_id)
