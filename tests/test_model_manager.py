"""Tests unitaires du gestionnaire de modèles locaux (AI Engine)."""

from ai.models.local_model_manager import AIModel, LocalModelManager, ModelStatus


def test_register_and_load():
    manager = LocalModelManager()
    manager.register(AIModel(id="m-001", name="stm32-context", engine="llama.cpp"))

    assert manager.get("m-001") is not None
    assert len(manager.list()) == 1

    loaded = manager.load("m-001")
    assert loaded is not None
    assert loaded.status == ModelStatus.LOADED


def test_get_missing_model():
    manager = LocalModelManager()
    assert manager.get("unknown-model") is None
