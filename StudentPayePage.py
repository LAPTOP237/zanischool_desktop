import ctypes
from PySide6.QtWidgets import QMessageBox, QLineEdit, QListView, QVBoxLayout, QWidget, QMenu, QProgressDialog, QPushButton
from PySide6.QtCore import QDate, QStringListModel, Qt, QTimer
import sys

from StudentPayeDialog import Ui_Dialog
from data.student_management import save_payement_to_db, get_students_from_db

class StudentPayePage(Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.paye_date_dateEdit.setDate(QDate.currentDate())
        self.paye_amount_doubleSpinBox.setMinimum(0.0)           # Valeur minimale
        self.paye_amount_doubleSpinBox.setMaximum(1000000000.0) 
        self.paye_amount_doubleSpinBox.setDecimals(3)        # Valeur maximale

        self.savePayementBtn.clicked.connect(self.validate_and_save)
        self.paye_cancel_btn.clicked.connect(self.reject)

        # Création du QListView et du modèle de chaîne
        self.list_view = QListView(self)
        self.list_view.setGeometry(50, 80, 300, 200)
        self.list_view.hide()  # Initialement caché

        self.model = QStringListModel()
        self.list_view.setModel(self.model)

        # Données des étudiants
        self.students = get_students_from_db()

        # Connexion du signal de changement de texte
        self.name_searchlineEdit.textChanged.connect(self.update_list_view)

        # Connexion du signal de sélection d'un élément
        self.list_view.clicked.connect(self.on_item_selected)

        # Créer l'indicateur de chargement
        self.loading_dialog = QProgressDialog("Enregistrement en cours...", None, 0, 0, self)
        self.loading_dialog.setWindowTitle("Veuillez patienter")
        self.loading_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.loading_dialog.setCancelButton(None)
        self.loading_dialog.setAutoClose(False)
        self.loading_dialog.setAutoReset(False)

    def update_list_view(self):
        text = self.name_searchlineEdit.text().lower()
        filtered_students = [
            f"{student['nom']} {student['prenom']}" for student in self.students 
            if text in f"{student['nom']} {student['prenom']}".lower()
        ]
        
        self.model.setStringList(filtered_students)
        self.list_view.setVisible(len(filtered_students) > 0)

    def on_item_selected(self, index):
        student_name = index.data()
        for student in self.students:
            if f"{student['nom']} {student['prenom']}" == student_name:
                self.paye_matricule_lineEdit.setText(student["matricule"])
                self.name_searchlineEdit.setText(f"{student['nom']} {student['prenom']}")
                break
        self.list_view.hide()  # Cacher la liste après la sélection

    
    def validate_and_save(self):
        self.start_loading()  # Démarrer l'indicateur de chargement
        self.savePayementBtn.setEnabled(False)  # Désactiver le bouton d'enregistrement pour éviter les clics multiples
        if self.validate_fields():
            QTimer.singleShot(100, self.save_payement)  # Appeler save_payement après une courte pause
        else:
            self.show_error_message()

    def start_loading(self):
        # Afficher l'indicateur de chargement
        self.loading_dialog.show()

    def stop_loading(self):
        # Masquer l'indicateur de chargement et réactiver le bouton
        self.loading_dialog.hide()
        self.savePayementBtn.setEnabled(True)

    def validate_fields(self):
        # Vérifie que les champs obligatoires sont remplis
        matricule = self.paye_matricule_lineEdit.text()
        raison = self.comboBox.currentText()
        montant = self.paye_amount_doubleSpinBox.text()
        date = self.paye_date_dateEdit.text()
        annee = self.paye_annee_comboBox.currentText()

        if not (matricule and raison and montant and date and annee):
            return False
        return True

    def show_error_message(self):
        # Affiche un message d'erreur si les champs ne sont pas remplis
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Champs manquants")
        msg.setText("Veuillez remplir tous les champs obligatoires.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def save_payement(self):
        # Récupérer les données du formulaire
        matricule = self.paye_matricule_lineEdit.text()
        raison = self.comboBox.currentText()
        montant = self.paye_amount_doubleSpinBox.text()
        date = self.paye_date_dateEdit.date().toString('yyyy-MM-dd')
        annee = self.paye_annee_comboBox.currentText()

        # Appeler la fonction pour sauvegarder les données dans la base de données
        message = save_payement_to_db(matricule, raison, montant, date, annee)
    
        # Afficher un message à l'utilisateur
        ctypes.windll.user32.MessageBoxW(0, message, "Résultat de l'enregistrement", 0x40 | 0x1)

        # Arrêter l'indicateur de chargement
        self.stop_loading()

        # Fermer la boîte de dialogue après l'enregistrement
        self.accept()
