"""Gestion de l'architecture technique (diagrammes, interfaces, budgets)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ArchitectureBlock:
    """Bloc fonctionnel / technique de l'architecture."""

    id: str
    name: str
    kind: str  # fonctionnel | technique
    interfaces: list[str] = field(default_factory=list)


@dataclass
class Architecture:
    """Architecture technique d'un projet."""

    project_id: str
    blocks: list[ArchitectureBlock] = field(default_factory=list)
    decision_id: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ArchitectureManager:
    """Enregistre l'architecture fonctionnelle et technique d'un projet."""

    def __init__(self) -> None:
        self._architectures: dict[str, Architecture] = {}

    def create(self, architecture: Architecture) -> Architecture:
        """Enregistre une architecture."""
        self._architectures[architecture.project_id] = architecture
        return architecture

    def get(self, project_id: str) -> Architecture | None:
        """Récupère l'architecture d'un projet."""
        return self._architectures.get(project_id)

    def add_block(self, project_id: str, block: ArchitectureBlock) -> bool:
        """Ajoute un bloc à l'architecture du projet."""
        architecture = self._architectures.get(project_id)
        if architecture is None:
            return False
        architecture.blocks.append(block)
        return True
