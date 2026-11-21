"""Démo end-to-end : contenu pilote → viewer → progression EAI."""

from desktop.viewer.viewer import EngineeringViewer
from engineering.architecture.architecture import ArchitectureManager
from engineering.architecture.pilot_content import load_pilot_architecture
from engineering.electronics.electronics import ElectronicsManager
from engineering.electronics.pilot_content import load_pilot_design
from engineering.eda.eda import EDAAdministrator
from engineering.eda.pilot_content import load_pilot_eda_design
from engineering.firmware.firmware import FirmwareManager
from engineering.firmware.pilot_content import load_pilot_firmware
from engineering.manufacturing.manufacturing import ManufacturingManager
from engineering.manufacturing.pilot_content import load_pilot_manufacturing
from engineering.mcu.mcu import MCUManager
from engineering.mcu.pilot_content import load_pilot_mcu
from engineering.requirements.requirements import RequirementsManager
from engineering.requirements.pilot_content import load_pilot_requirements
from engineering.simulation.simulation import SimulationManager
from engineering.simulation.pilot_content import load_pilot_simulation
from engineering.testing.testing import TestingManager
from engineering.testing.pilot_content import load_pilot_tests


def main() -> None:
    """Exécute la démo : charge le contenu pilote et affiche la progression."""
    requirements_manager = load_pilot_requirements()
    architecture_manager = ArchitectureManager()
    architecture_manager.create(load_pilot_architecture())
    electronics_manager = load_pilot_design()
    eda_administrator = load_pilot_eda_design()
    mcu_manager = load_pilot_mcu()
    firmware_manager = load_pilot_firmware()
    simulation_manager = SimulationManager()
    simulation_manager.create(load_pilot_simulation())
    testing_manager = TestingManager()
    testing_manager.create(load_pilot_tests())
    manufacturing_manager = load_pilot_manufacturing()

    viewer = EngineeringViewer(
        requirements_manager=requirements_manager,
        architecture_manager=architecture_manager,
        electronics_manager=electronics_manager,
        eda_administrator=eda_administrator,
        mcu_manager=mcu_manager,
        firmware_manager=firmware_manager,
        simulation_manager=simulation_manager,
        testing_manager=testing_manager,
        manufacturing_manager=manufacturing_manager,
    )

    progress = viewer.view("EAI-PILOT")
    print(
        f"Projet {progress.project_id} — "
        f"{len(progress.requirements)} exigence(s), "
        f"{progress.architecture_blocks} bloc(s), "
        f"électronique: {progress.electronics}, "
        f"EDA: {progress.eda}, MCU: {progress.mcu}, "
        f"firmware: {progress.firmware}, simulation: {progress.simulation}, "
        f"tests: {progress.testing}, fabrication: {progress.manufacturing}"
    )


if __name__ == "__main__":
    main()
