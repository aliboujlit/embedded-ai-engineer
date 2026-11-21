"""Gestion de l'ingénierie des tests (plans, exécution, rapports)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class TestCase:
    """Cas de test associé à un projet."""

    project_id: str
    plan_id: str | None = None
    results: list[dict] = field(default_factory=list)
    executed_at: datetime | None = None


class TestingManager:
    """Enregistre et consulte les cas de test et rapports."""

    def __init__(self) -> None:
        self._tests: dict[str, TestCase] = {}

    def create(self, test: TestCase) -> TestCase:
        """Enregistre un cas de test."""
        self._tests[test.project_id] = test
        return test

    def get(self, project_id: str) -> TestCase | None:
        """Récupère le cas de test d'un projet."""
        return self._tests.get(project_id)
