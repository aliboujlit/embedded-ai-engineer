"""Tests d'intégration de bout en bout : EAIDesktopApp → Viewer → Progress."""

from desktop.app import EAIDesktopApp


def test_eai_app_loads_pilot_progress() -> None:
    app = EAIDesktopApp(project_id="EAI-PILOT")
    window = app.run()
    progress = window.load()

    assert progress is not None
    assert progress.project_id == "EAI-PILOT"
    assert len(progress.requirements) > 0
    assert progress.architecture_blocks > 0
