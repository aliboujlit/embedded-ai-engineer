"""Runtime d'exécution de l'intelligence artificielle locale (inférence)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from ai.models.local_model_manager import AIModel, LocalModelManager, ModelStatus


@dataclass
class InferenceRequest:
    """Requête d'inférence adressée à un modèle local."""

    model_id: str
    prompt: str
    max_tokens: int = 512


@dataclass
class InferenceResult:
    """Résultat d'une inférence locale."""

    model_id: str
    prompt: str
    response: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class AIRuntime:
    """Exécute des inférences via un modèle IA local chargé."""

    def __init__(self, model_manager: LocalModelManager) -> None:
        self.model_manager = model_manager

    def run(self, request: InferenceRequest) -> InferenceResult | None:
        """Exécute une inférence locale (stub — branché sur llama.cpp / LM Studio)."""
        model: AIModel | None = self.model_manager.get(request.model_id)
        if model is None or model.status is not ModelStatus.LOADED:
            return None
        # TODO : appel réel vers le moteur de runtime (llama.cpp / LM Studio).
        response = f"[stub] Inférence via {model.engine} pour le modèle {model.name}"
        return InferenceResult(
            model_id=model.id,
            prompt=request.prompt,
            response=response,
        )
