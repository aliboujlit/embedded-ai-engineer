"""Viewer d'ingénierie : agrège l'état des livrables d'un projet."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ProjectProgress:
    """Vue d'ensemble de progression d'un projet EAI."""

    project_id: str
    requirements: list = field(default_factory=list)
    architecture_blocks: int = 0
    electronics: dict = field(default_factory=dict)
    eda: dict = field(default_factory=dict)
    mcu: dict = field(default_factory=dict)
    firmware: dict = field(default_factory=dict)
    simulation: dict = field(default_factory=dict)
    testing: dict = field(default_factory=dict)
    manufacturing: dict = field(default_factory=dict)
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EngineeringViewer:
    """Assemble la vue de progression d'un projet à partir des modules d'ingénierie."""

    def __init__(
        self,
        requirements_manager=None,
        architecture_manager=None,
        electronics_manager=None,
        eda_administrator=None,
        mcu_manager=None,
        firmware_manager=None,
        simulation_manager=None,
        testing_manager=None,
        manufacturing_manager=None,
    ) -> None:
        self.managers = {
            "requirements": requirements_manager,
            "architecture": architecture_manager,
            "electronics": electronics_manager,
            "eda": eda_administrator,
            "mcu": mcu_manager,
            "firmware": firmware_manager,
            "simulation": simulation_manager,
            "testing": testing_manager,
            "manufacturing": manufacturing_manager,
        }

    def view(self, project_id: str) -> ProjectProgress:
        """Construit la vue de progression d'un projet."""
        progress = ProjectProgress(project_id=project_id)
        requirements = self.managers["requirements"]
        if requirements is not None:
            progress.requirements = [r.id for r in requirements.list()]
        architecture = self.managers["architecture"]
        if architecture is not None:
            progress.architecture_blocks = len(architecture.get(project_id).blocks) if architecture.get(project_id) else 0
        progress.electronics = {"design": self.managers["electronics"].get(project_id) is not None} if self.managers["electronics"] else {}
        progress.eda = {"design": self.managers["eda"].get(project_id) is not None} if self.managers["eda"] else {}
        progress.mcu = {"config": self.managers["mcu"].get(project_id) is not None} if self.managers["mcu"] else {}
        progress.firmware = {"project": self.managers["firmware"].get(project_id) is not None} if self.managers["firmware"] else {}
        progress.simulation = {"case": self.managers["simulation"].get(project_id) is not None} if self.managers["simulation"] else {}
        progress.testing = {"case": self.managers["testing"].get(project_id) is not None} if self.managers["testing"] else {}
        progress.manufacturing = {"package": self.managers["manufacturing"].get(project_id) is not None} if self.managers["manufacturing"] else {}
        return progress
