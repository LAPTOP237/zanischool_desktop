from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt, QTimer

class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chargement en cours...")
        self.setModal(True)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        
        self.label = QLabel("Veuillez patienter pendant le chargement...")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 0)  # Indeterminate state
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def start_loading(self):
        self.show()

    def stop_loading(self):
        self.accept()
