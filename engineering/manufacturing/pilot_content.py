"""Contenu du package de fabrication du projet pilote."""

from engineering.manufacturing.manufacturing import ManufacturingManager, ManufacturingPackage


def load_pilot_manufacturing() -> ManufacturingManager:
    """Charge le package de fabrication du projet pilote."""
    manager = ManufacturingManager()
    manager.create(
        ManufacturingPackage(
            project_id="EAI-PILOT",
            gerber_ref="GERBER-EAI-PILOT-001",
            bom_ref="BOM-EAI-PILOT-001",
            pick_and_place_ref="PAP-EAI-PILOT-001",
            assembly_ref="ASM-EAI-PILOT-001",
            status="PENDING",
        )
    )
    return manager
