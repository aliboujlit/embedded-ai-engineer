"""Contenu EDA du projet pilote (schéma, PCB, ERC, DRC, BOM)."""

from engineering.eda.eda import EDAAdministrator, EDADesign


def load_pilot_eda_design() -> EDAAdministrator:
    """Charge la conception EDA du projet pilote."""
    administrator = EDAAdministrator()
    administrator.create(
        EDADesign(
            project_id="EAI-PILOT",
            schematic_ref="SCH-EAI-PILOT-001",
            pcb_ref="PCB-EAI-PILOT-001",
            erc_status="PENDING",
            drc_status="PENDING",
        )
    )
    return administrator
