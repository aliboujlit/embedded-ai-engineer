"""Gestion des exigences techniques et traçabilité (cahier des charges → livrables/tests)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class RequirementStatus(str, Enum):
    """Statut d'une exigence technique."""

    DRAFT = "DRAFT"
    PROPOSED = "PROPOSED"
    CONFIRMED = "CONFIRMED"
    DEPRECATED = "DEPRECATED"


@dataclass
class Requirement:
    """Exigence technique d'un projet."""

    id: str
    text: str
    source: str  # cahier des charges / besoin exprimé
    status: RequirementStatus = RequirementStatus.DRAFT
    traceability: list[str] = field(default_factory=list)  # IDs de livrables/tests


class RequirementsManager:
    """Enregistre les exigences et gère leur traçabilité."""

    def __init__(self) -> None:
        self._requirements: dict[str, Requirement] = {}

    def add(self, requirement: Requirement) -> Requirement:
        """Enregistre une exigence."""
        self._requirements[requirement.id] = requirement
        return requirement

    def get(self, requirement_id: str) -> Requirement | None:
        """Récupère une exigence par son identifiant."""
        return self._requirements.get(requirement_id)

    def list(self, status: RequirementStatus | None = None) -> list[Requirement]:
        """Liste les exigences (option : filtr par statut)."""
        requirements = list(self._requirements.values())
        if status is not None:
            requirements = [r for r in requirements if r.status is status]
        return requirements

    def trace(self, requirement_id: str, target_id: str) -> bool:
        """Ajoute une traceabilité exigence → livrable/test."""
        requirement = self._requirements.get(requirement_id)
        if requirement is None:
            return False
        if target_id not in requirement.traceability:
            requirement.traceability.append(target_id)
        return True
