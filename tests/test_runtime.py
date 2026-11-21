"""Tests unitaires du runtime d'inférence (AI Engine)."""

from ai.models.local_model_manager import AIModel, LocalModelManager, ModelStatus
from ai.runtime.runtime import AIRuntime, InferenceRequest


def test_run_requires_loaded_model():
    manager = LocalModelManager()
    manager.register(AIModel(id="m-001", name="stm32-context", engine="llama.cpp"))
    runtime = AIRuntime(manager)

    result = runtime.run(InferenceRequest(model_id="m-001", prompt="test prompt"))

    assert result is None


def test_run_with_loaded_model():
    manager = LocalModelManager()
    manager.register(AIModel(id="m-001", name="stm32-context", engine="llama.cpp"))
    manager.load("m-001")
    runtime = AIRuntime(manager)

    result = runtime.run(InferenceRequest(model_id="m-001", prompt="test prompt"))

    assert result is not None
    assert result.model_id == "m-001"
    assert result.prompt == "test prompt"
