"""Tests d'intégration du viewer avec le contenu du projet pilote."""

from desktop.viewer.viewer import EngineeringViewer
from engineering.architecture.architecture import ArchitectureManager
from engineering.architecture.pilot_content import load_pilot_architecture
from engineering.requirements.pilot_content import load_pilot_requirements


def test_viewer_with_pilot_content():
    requirements_manager = load_pilot_requirements()
    architecture_manager = ArchitectureManager()
    architecture_manager.create(load_pilot_architecture())

    viewer = EngineeringViewer(
        requirements_manager=requirements_manager,
        architecture_manager=architecture_manager,
    )
    progress = viewer.view("EAI-PILOT")

    assert progress.project_id == "EAI-PILOT"
    assert len(progress.requirements) > 0
    assert progress.architecture_blocks > 0
