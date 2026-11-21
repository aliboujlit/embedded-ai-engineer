"""Contenu du projet firmware du projet pilote."""

from engineering.firmware.firmware import FirmwareManager, FirmwareProject


def load_pilot_firmware() -> FirmwareManager:
    """Charge le projet firmware du projet pilote."""
    manager = FirmwareManager()
    manager.create(
        FirmwareProject(
            project_id="EAI-PILOT",
            source_ref="FW-EAI-PILOT-001",
            build_system="CMake",
            toolchain="GCC",
            status="DRAFT",
        )
    )
    return manager
