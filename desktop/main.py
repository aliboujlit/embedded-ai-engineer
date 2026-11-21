"""Point d'entrée de l'application Desktop EAI."""

from __future__ import annotations

from desktop.app import EAIDesktopApp
from desktop.gui import run_app


def main(project_id: str, viewer=None) -> int:
    """Lance l'application EAI Desktop sur un projet."""
    return run_app(project_id, viewer)
