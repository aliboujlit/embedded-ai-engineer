"""Application Desktop complète EAI — point d'entrée de l'interface graphique."""

from __future__ import annotations

from desktop.main_window import MainWindow
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


class EngineeringViewerFactory:
    """Fabrique le viewer prêt à l'emploi avec le contenu du projet pilote."""

    @staticmethod
    def create() -> EngineeringViewer:
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

        return EngineeringViewer(
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


class EAIDesktopApp:
    """Application Desktop EAI : fenêtre principale + viewer d'ingénierie."""

    def __init__(self, project_id: str, viewer: EngineeringViewer | None = None) -> None:
        self.project_id = project_id
        self.viewer = viewer or EngineeringViewerFactory.create()
        self.window: MainWindow | None = None

    def run(self) -> MainWindow:
        """Crée et retourne la fenêtre principale chargée sur le projet."""
        self.window = MainWindow(project_id=self.project_id, viewer=self.viewer)
        return self.window
