"""Orchestrateur principal de l'ingénierie électronique assistée par IA (EAI Core)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class TaskStatus(str, Enum):
    """Statuts normalisés d'un livrable / tâche (EAI-STR-001, H.3)."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    GENERATED = "GENERATED"
    BUILD_PASSED = "BUILD_PASSED"
    SIMULATION_PASSED = "SIMULATION_PASSED"
    VERIFIED = "VERIFIED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    REQUIRES_PHYSICAL_TEST = "REQUIRES_PHYSICAL_TEST"


@dataclass
class Task:
    """Une tâche d'ingénierie rattachée à un projet."""

    id: str
    project_id: str
    title: str
    status: TaskStatus = TaskStatus.NOT_STARTED
    assigned_agent: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EngineeringOrchestrator:
    """Orchestre le cycle automatisé : Analyse → Planification → Exécution →
    Vérification → Correction → Consolidation → Livraison."""

    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def create_task(self, task: Task) -> Task:
        """Enregistre une nouvelle tâche dans le registre."""
        self._tasks[task.id] = task
        return task

    def assign(self, task_id: str, agent_id: str) -> Task | None:
        """Affecte un agent à une tâche."""
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.assigned_agent = agent_id
        task.updated_at = datetime.now(timezone.utc)
        return task

    def transition(self, task_id: str, status: TaskStatus) -> Task | None:
        """Déplace une tâche à un nouveau statut."""
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.status = status
        task.updated_at = datetime.now(timezone.utc)
        return task

    def get_task(self, task_id: str) -> Task | None:
        """Récupère une tâche par son identifiant."""
        return self._tasks.get(task_id)
