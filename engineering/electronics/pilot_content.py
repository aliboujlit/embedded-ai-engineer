"""Contenu de la conception électronique du projet pilote."""

from engineering.electronics.electronics import ElectronicsManager, ElectronicDesign


def load_pilot_design() -> ElectronicsManager:
    """Charge la conception électronique du projet pilote."""
    manager = ElectronicsManager()
    manager.create(
        ElectronicDesign(
            project_id="EAI-PILOT",
            schematic_ref="SCH-EAI-PILOT-001",
        )
    )
    return manager
