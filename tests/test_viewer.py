"""Tests d'intégration du viewer avec le contenu du projet pilote."""

from desktop.viewer.viewer import EngineeringViewer
from engineering.architecture.pilot_content import load_pilot_architecture
from engineering.electronics.pilot_content import load_pilot_design
from engineering.eda.pilot_content import load_pilot_eda_design
from engineering.firmware.pilot_content import load_pilot_firmware
from engineering.manufacturing.pilot_content import load_pilot_manufacturing
from engineering.mcu.pilot_content import load_pilot_mcu
from engineering.requirements.pilot_content import load_pilot_requirements
from engineering.simulation.pilot_content import load_pilot_simulation
from engineering.testing.pilot_content import load_pilot_tests


def test_viewer_with_pilot_content():
    viewer = EngineeringViewer(
        requirements_manager=load_pilot_requirements(),
        architecture_manager=None,
    )
    progress = viewer.view("EAI-PILOT")

    assert progress.project_id == "EAI-PILOT"
    assert len(progress.requirements) > 0
    assert progress.architecture_blocks > 0
