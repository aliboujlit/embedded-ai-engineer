"""Contenu de la configuration MCU du projet pilote."""

from engineering.mcu.mcu import MCUManager, MCUConfiguration


def load_pilot_mcu() -> MCUManager:
    """Charge la configuration MCU du projet pilote."""
    manager = MCUManager()
    manager.create(
        MCUConfiguration(
            project_id="EAI-PILOT",
            family="STM32",
            chip="STM32G474",
            toolchain="STM32CubeIDE",
            status="SELECTED",
        )
    )
    return manager
