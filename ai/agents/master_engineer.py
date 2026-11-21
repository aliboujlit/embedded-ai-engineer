"""Agent de direction et coordination — Master Engineer (AG-001)."""

from __future__ import annotations

from dataclasses import dataclass

from ai.models.local_model_manager import AIModel, LocalModelManager, ModelStatus
from ai.runtime.runtime import AIRuntime, InferenceRequest


@dataclass
class AgentTask:
    """Tâche traitée par un agent spécialisé."""

    task_id: str
    prompt: str
    model_id: str


class MasterEngineerAgent:
    """Agent de direction et coordination du projet (AG-001).

    Il orchestre l'analyse, la planification et la décomposition du besoin
    en tâches d'ingénierie, via le runtime IA local.
    """

    def __init__(self, runtime: AIRuntime, model_manager: LocalModelManager) -> None:
        self.runtime = runtime
        self.model_manager = model_manager

    def run(self, task: AgentTask) -> str | None:
        """Exécute la tâche via le runtime local et retourne la conclusion."""
        model: AIModel | None = self.model_manager.get(task.model_id)
        if model is None or model.status is not ModelStatus.LOADED:
            return None
        result = self.runtime.run(
            InferenceRequest(
                model_id=task.model_id,
                prompt=task.prompt,
                max_tokens=1024,
            )
        )
        return result.response if result is not None else None
