"""Contenu des exigences du projet pilote EAI (carte BLDC STM32G474)."""

from __future__ import annotations

from engineering.requirements.requirements import (
    Requirement,
    RequirementStatus,
    RequirementsManager,
)


def load_pilot_requirements() -> RequirementsManager:
    """Charge les exigences initiales du projet pilote (STM32G474 / BLDC)."""
    manager = RequirementsManager()

    manager.add(
        Requirement(
            id="EAI-PILOT-001",
            text="Le système pilote doit être basé sur un microcontrôleur STM32G474.",
            source="Cahier des charges pilote",
            status=RequirementStatus.CONFIRMED,
        )
    )
    manager.add(
        Requirement(
            id="EAI-PILOT-002",
            text="Le firmware doit implémenter la commande moteur BLDC.",
            source="Cahier des charges pilote",
            status=RequirementStatus.CONFIRMED,
        )
    )
    manager.add(
        Requirement(
            id="EAI-PILOT-003",
            text="Les alimentations du bus doivent être protégées contre les surintensités.",
            source="Cahier des charges pilote",
            status=RequirementStatus.PROPOSED,
        )
    )
    manager.add(
        Requirement(
            id="EAI-PILOT-004",
            text="La carte doit supporter le pilotage d'un moteur BLDC basse tension.",
            source="Cahier des charges pilote",
            status=RequirementStatus.DRAFT,
        )
    )

    return manager
