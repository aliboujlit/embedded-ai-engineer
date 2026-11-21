"""Gestion des modèles d'intelligence artificielle locaux (llama.cpp / LM Studio)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class ModelStatus(str, Enum):
    """Statut d'un modèle IA local."""

    NOT_REGISTERED = "NOT_REGISTERED"
    AVAILABLE = "AVAILABLE"
    LOADED = "LOADED"
    ERROR = "ERROR"


@dataclass
class AIModel:
    """Modèle IA local applicable à une tâche d'ingénierie."""

    id: str
    name: str
    engine: str  # "llama.cpp" | "LM Studio"
    context_size: int = 0
    status: ModelStatus = ModelStatus.NOT_REGISTERED


class LocalModelManager:
    """Registre les modèles locaux et gère leur cycle de vie (chargement)."""

    def __init__(self) -> None:
        self._models: dict[str, AIModel] = {}

    def register(self, model: AIModel) -> AIModel:
        """Enregistre un modèle local dans le gestionnaire."""
        self._models[model.id] = model
        return model

    def get(self, model_id: str) -> AIModel | None:
        """Récupère un modèle par son identifiant."""
        return self._models.get(model_id)

    def list(self) -> list[AIModel]:
        """Liste les modèles enregistrés."""
        return list(self._models.values())

    def load(self, model_id: str) -> AIModel | None:
        """Charge un modèle local (simulation du chargement runtime)."""
        model = self._models.get(model_id)
        if model is None:
            return None
        model.status = ModelStatus.LOADED
        return model
