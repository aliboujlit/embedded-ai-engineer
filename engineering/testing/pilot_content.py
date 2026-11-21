"""Contenu des tests du projet pilote."""

from engineering.testing.testing import TestCase


def load_pilot_tests() -> TestCase:
    """Charge le cas de test du projet pilote."""
    return TestCase(
        project_id="EAI-PILOT",
        plan_id="PLAN-EAI-PILOT-001",
        results=[],
        executed_at=None,
    )
