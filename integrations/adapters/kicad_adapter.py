"""Adaptateur KiCad (PLG-EDA-001) — couche EAI-IR vers KiCad 9+."""

from __future__ import annotations

from typing import Any

from integrations.adapters.base import EngineeringToolAdapter


class KiCadAdapter(EngineeringToolAdapter):
    """Adaptateur KiCad : création de projets, schémas, ERC, PCB, DRC."""

    def get_capabilities(self) -> list[str]:
        return [
            "create_project",
            "create_schematic",
            "run_erc",
            "create_pcb",
            "run_drc",
            "export_bom",
        ]

    def execute(self, operation: str, params: dict[str, Any]) -> dict[str, Any]:
        # TODO : brancher sur l'API KiCad (python).
        return {"operation": operation, "status": "stub", "params": params}
