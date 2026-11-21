"""Contenu de la simulation du projet pilote."""

from engineering.simulation.simulation import SimulationCase


def load_pilot_simulation() -> SimulationCase:
    """Charge le cas de simulation du projet pilote."""
    return SimulationCase(
        project_id="EAI-PILOT",
        simulator="Renode",
        model="STM32G474",
        parameters={"clock_hz": 64000000},
        results={},
        executed_at=None,
    )
