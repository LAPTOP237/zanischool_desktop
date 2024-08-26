from PySide6.QtWidgets import QMessageBox
from StudentPayeDialog import Ui_Dialog
from PySide6.QtCore import QDate
from data.student_management import save_payement_to_db;

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

    
    def validate_and_save(self):
        if self.validate_fields():
            self.save_payement()
        else:
            self.show_error_message()

    def validate_fields(self):
        # Vérifie que les champs obligatoires sont remplis
        matricule = self.paye_matricule_lineEdit.text()
        raison = self.paye_raison_lineEdit.text()
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
        raison = self.paye_raison_lineEdit.text()
        montant = self.paye_amount_doubleSpinBox.text()
        date = self.paye_date_dateEdit.date().toString('yyyy-MM-dd')
        annee = self.paye_annee_comboBox.currentText()

        # Appeler la fonction pour sauvegarder les données dans la base de données
        save_payement_to_db(matricule, raison, montant, date, annee)
        # Fermer la boîte de dialogue après l'enregistrement
        self.accept()
