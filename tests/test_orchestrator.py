"""Tests unitaires du cycle de vie des tâches (EAI Core / Orchestrator)."""

from core.orchestrator.orchestrator import EngineeringOrchestrator, Task, TaskStatus


def test_create_task():
    orchestrator = EngineeringOrchestrator()
    task = orchestrator.create_task(Task(id="T-001", project_id="P-001", title="Analyse du besoin"))

    stored = orchestrator.get_task("T-001")

    assert stored is not None
    assert stored.id == "T-001"
    assert stored.project_id == "P-001"
    assert task.title == "Analyse du besoin"


def test_assign_and_transition_lifecycle():
    orchestrator = EngineeringOrchestrator()
    task = orchestrator.create_task(Task(id="T-002", project_id="P-001", title="Concevoir le schéma"))

    orchestrator.assign("T-002", "AG-004")
    assigned = orchestrator.get_task("T-002")
    assert assigned is not None
    assert assigned.assigned_agent == "AG-004"

    orchestrator.transition("T-002", TaskStatus.BUILD_PASSED)
    transitioned = orchestrator.get_task("T-002")
    assert transitioned is not None
    assert transitioned.status == TaskStatus.BUILD_PASSED


def test_get_task_not_found():
    orchestrator = EngineeringOrchestrator()
    assert orchestrator.get_task("T-INEXISTANT") is None
