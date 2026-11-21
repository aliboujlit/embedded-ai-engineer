"""Gestion de l'ingénierie MCU (choix, configuration, SDK)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class MCUConfiguration:
    """Configuration d'un microcontrôleur dans le cadre d'un projet."""

    project_id: str
    family: str | None = None
    chip: str | None = None
    toolchain: str | None = None
    status: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class MCUManager:
    """Enregistre et consulte les configurations MCU par projet."""

    def __init__(self) -> None:
        self._configs: dict[str, MCUConfiguration] = {}

    def create(self, config: MCUConfiguration) -> MCUConfiguration:
        """Enregistre une configuration MCU."""
        self._configs[config.project_id] = config
        return config

    def get(self, project_id: str) -> MCUConfiguration | None:
        """Récupère la configuration MCU d'un projet."""
        return self._configs.get(project_id)
