from PySide6.QtWidgets import QMessageBox, QProgressDialog
from PySide6.QtCore import Qt, QTimer
from data.compte_management import change_password
from updateCompteDialog import Ui_updateCompteDialog

class UpdateComptePage(Ui_updateCompteDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.user_id = user_id
        self.updatePasswordBtn.clicked.connect(self.update_password)
        self.update_pass_concel_btn.clicked.connect(self.close)

    def update_password(self):
        old_password = self.update_old_pass_lineEdit.text()
        new_password = self.update_new_pass_lineEdit.text()
        confirm_password = self.update_confirm_pass_lineEdit.text()

        # Validation des champs
        if not old_password or not new_password or not confirm_password:
            QMessageBox.warning(self, "Erreur", "Tous les champs sont obligatoires.")
            return

        if new_password != confirm_password:
            QMessageBox.warning(self, "Erreur", "Le nouveau mot de passe et la confirmation ne correspondent pas.")
            return

        # Afficher le dialogue de progression
        progress_dialog = QProgressDialog("Enregistrement en cours...", None, 0, 0, self)
        progress_dialog.setWindowTitle("Veuillez patienter")
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setAutoClose(False)
        progress_dialog.show()

        # Démarrer un QTimer pour simuler une pause
        QTimer.singleShot(1000, lambda: self.perform_password_update(progress_dialog, old_password, new_password))

        self.accept()

    def perform_password_update(self, progress_dialog, old_password, new_password):
        # Vérification de l'ancien mot de passe et mise à jour
        result = change_password(self.user_id, old_password, new_password)
        
        # Fermer le dialogue de progression
        progress_dialog.close()

        # Afficher le résultat
        if result == "Mot de passe actuel incorrect.":
            QMessageBox.critical(self, "Erreur", result)
        else:
            QMessageBox.information(self, "Succès", result)
            self.close()
