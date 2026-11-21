"""Contenu de l'architecture du projet pilote (blocs fonctionnels et techniques)."""

from engineering.architecture.architecture import Architecture, ArchitectureBlock


def load_pilot_architecture() -> Architecture:
    """Charge l'architecture fonctionnelle et technique du projet pilote."""
    architecture = Architecture(project_id="EAI-PILOT", decision_id="DEC-001")
    architecture.blocks.append(ArchitectureBlock(id="B-01", name="Acquisition capteurs", kind="fonctionnel"))
    architecture.blocks.append(ArchitectureBlock(id="B-02", name="Gestion moteur BLDC", kind="fonctionnel"))
    architecture.blocks.append(ArchitectureBlock(id="B-03", name="Gestion alimentation", kind="technique"))
    return architecture
