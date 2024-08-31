from PySide6.QtWidgets import QMessageBox,QProgressDialog
from PySide6.QtCore import Qt,QTimer
from compteDialog import Ui_CompteDial
from data.compte_management import add_user


class ComptePage(Ui_CompteDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Connecter les boutons à leurs méthodes respectives
        self.saveCompteBtn.clicked.connect(self.create_account)
        self.compte_concel_btn.clicked.connect(self.close)

    def create_account(self):
         # Récupérer les valeurs des champs
        titulaire = self.titulaire_lineEdit.text().strip()
        username = self.name_user_lineEdit.text().strip()
        role = self.role_comboBox.currentText()
        password = self.password_lineEdit.text().strip()
        confirm_password = self.confirm_password_lineEdit.text().strip()

        # Valider les champs
        if not titulaire or not role or  not username or not password or not confirm_password:
            QMessageBox.warning(self, "Champs Manquants", "Veuillez remplir tous les champs obligatoires.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Erreur de Mot de Passe", "Les mots de passe ne correspondent pas.")
            return

        # Afficher le dialogue de progression
        progress_dialog = QProgressDialog("Enregistrement en cours...", None, 0, 0, self)
        progress_dialog.setWindowTitle("Veuillez patienter")
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setAutoClose(False)
        progress_dialog.show()

        # Démarrer un QTimer pour simuler une pause
        QTimer.singleShot(1000, lambda: self.perform_account_creation(progress_dialog, username, password,role,titulaire))

    def perform_account_creation(self, progress_dialog, username, password,role,titulaire):
        # Appel à la fonction pour créer un nouveau compte
        result = add_user(titulaire,username, password,role)
        
        # Fermer le dialogue de progression
        progress_dialog.close()

        # Afficher le résultat
        if result == "Nom d'utilisateur déjà existant.":
            QMessageBox.critical(self, "Erreur", result)
        elif result == "Erreur lors de l'enregistrement du compte.":
            QMessageBox.critical(self, "Erreur", "Une erreur est survenue. Veuillez réessayer. Ou contacter le service client")
        else:
            QMessageBox.information(self, "Succès", "Compte créé avec succès.")
            self.close()

        