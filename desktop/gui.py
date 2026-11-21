"""Interface graphique PyQt6 — QMainWindow avec onglets de visualisation."""

from __future__ import annotations

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTabWidget

from desktop.viewer.viewer import EngineeringViewer, ProjectProgress


class EAIQMainWindow(QMainWindow):
    """Fenêtre principale EAI avec onglets de visualisation par domaine."""

    def __init__(self, project_id: str, viewer: EngineeringViewer) -> None:
        super().__init__()
        self.project_id = project_id
        self.viewer = viewer
        self.setWindowTitle(f"EAI — {project_id}")

        central = QWidget()
        layout = QVBoxLayout(central)
        self.summary_label = QLabel()
        layout.addWidget(self.summary_label)

        self.tabs = QTabWidget()
        self.tab_labels: dict[str, QLabel] = {}
        self.tab_labels["Exigences"] = self._build_tab("Exigences")
        self.tab_labels["Architecture"] = self._build_tab("Architecture")
        self.tab_labels["Électronique"] = self._build_tab("Électronique")
        self.tab_labels["EDA"] = self._build_tab("EDA")
        self.tab_labels["MCU"] = self._build_tab("MCU")
        self.tab_labels["Firmware"] = self._build_tab("Firmware")
        self.tab_labels["Simulation"] = self._build_tab("Simulation")
        self.tab_labels["Tests"] = self._build_tab("Tests")
        self.tab_labels["Fabrication"] = self._build_tab("Fabrication")

        layout.addWidget(self.tabs)
        self.setCentralWidget(central)
        self.refresh()

    def _build_tab(self, key: str) -> QLabel:
        label = QLabel(f"[stub] Vue {key} pour le projet {self.project_id}")
        return label

    def refresh(self) -> None:
        """Rafraîchit les vues à partir du viewer."""
        progress: ProjectProgress = self.viewer.view(self.project_id)
        self.summary_label.setText(
            f"Projet {progress.project_id} — {len(progress.requirements)} exigence(s), "
            f"{progress.architecture_blocks} bloc(s) architectural(aux)."
        )

        self.tab_labels["Exigences"].setText(
            f"Exigences : {', '.join(progress.requirements) if progress.requirements else 'Aucune'}"
        )
        self.tab_labels["Architecture"].setText(f"Blocs architecturaux : {progress.architecture_blocks}")
        self.tab_labels["Électronique"].setText(f"Conception électronique : {progress.electronics}")
        self.tab_labels["EDA"].setText(f"Conception EDA : {progress.eda}")
        self.tab_labels["MCU"].setText(f"Configuration MCU : {progress.mcu}")
        self.tab_labels["Firmware"].setText(f"Firmware : {progress.firmware}")
        self.tab_labels["Simulation"].setText(f"Simulation : {progress.simulation}")
        self.tab_labels["Tests"].setText(f"Tests : {progress.testing}")
        self.tab_labels["Fabrication"].setText(f"Fabrication : {progress.manufacturing}")


def run_app(project_id: str, viewer: EngineeringViewer | None = None) -> int:
    """Point d'entrée applicatif EAI Desktop."""
    app = QApplication([])
    window = EAIQMainWindow(project_id=project_id, viewer=viewer or EngineeringViewer())
    window.show()
    return app.exec()
