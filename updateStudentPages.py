from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate
from UpdateStudentDialog import Ui_UpdateStudent_Dialog
from data.student_management import update_student

class StudentUpdatePage(Ui_UpdateStudent_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        # Connecter les boutons aux méthodes
        self.updateStudentBtn.clicked.connect(self.update_student)
        self.update_cancel_btn.clicked.connect(self.cancel_update)

    def load_student_data(self, student_data):
        """Pré-remplit le formulaire avec les données de l'apprenant."""
        self.matricule = student_data['matricule']
        self.update_name_lineEdit.setText(student_data['nom'])
        self.update_name_lineEdit_2.setText(student_data['prenom'])
        self.update_gender_comboBox.setCurrentText(student_data['sexe'])
        self.update_class_comboBox_2.setCurrentText(student_data['option_et_niveau'])
        self.update_dateNaiss_dateEdit.setDate(QDate.fromString(student_data['date_naissance'], 'yyyy-MM-dd'))
        self.update_lieuNaiss_lineEdit.setText(student_data['lieu_naissance'])
        self.update_email_lineEdit.setText(student_data['email'])
        self.update_contact_lineEdit.setText(student_data['contact'])

    def update_student(self):
        """Valide et met à jour les informations de l'apprenant dans la base de données."""
        matricule = self.matricule  # Assurez-vous que le matricule est défini ailleurs

        nom = self.update_name_lineEdit.text()
        prenom = self.update_name_lineEdit_2.text()
        sexe = self.update_gender_comboBox.currentText()
        option_et_niveau = self.update_class_comboBox_2.currentText()
        date_naissance = self.update_dateNaiss_dateEdit.date().toString('yyyy-MM-dd')
        lieu_naissance = self.update_lieuNaiss_lineEdit.text()
        email = self.update_email_lineEdit.text()
        contact = self.update_contact_lineEdit.text()

        if not all([nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        # Mettre à jour les données dans la base de données
        update_student(matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact)

        # Afficher un message de confirmation
        QMessageBox.information(self, "Succès", "Les informations de l'apprenant ont été mises à jour avec succès.")

        # Fermer le dialogue
        self.accept()

    def cancel_update(self):
        """Annule la modification et ferme le formulaire."""
        self.reject()
