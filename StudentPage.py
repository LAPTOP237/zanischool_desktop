from PySide6.QtWidgets import QMessageBox
from StudentDialog import Ui_StudentDialog
from data.student_management import save_student_to_db, get_all_etudes
from data.database import initialize_db

class StudentPage(Ui_StudentDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.saveStudentBtn.clicked.connect(self.validate_and_save)
        self.cancel_btn.clicked.connect(self.reject)
        initialize_db()  # Initialiser la base de données au lancement
        self.load_combo_box_items() #Pour gerer les items de mon combox de mes classes

    def load_combo_box_items(self):
        etudes = get_all_etudes()
    
        for etude in etudes:
            id_niveau, id_filiere = etude
            item_text = f"{id_filiere} {id_niveau}"
            self.class_comboBox_2.addItem(item_text)
           
    def validate_and_save(self):
        if self.validate_fields():
            self.save_student()
        else:
            self.show_error_message()

    def validate_fields(self):
        # Vérifie que les champs obligatoires sont remplis
        nom = self.name_lineEdit.text()
        prenom = self.name_lineEdit_2.text()
        sexe = self.gender_comboBox.currentText()
        option_et_niveau = self.class_comboBox_2.currentText()
        date_naissance = self.dateNaiss_dateEdit.text()
        lieu_naissance = self.lieuNaiss_lineEdit.text()

        if not (nom and prenom and sexe and option_et_niveau and date_naissance and lieu_naissance):
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


    # def save_student(self):
    #     # Récupérer les données du formulaire
    #     nom = self.name_lineEdit.text()
    #     prenom = self.name_lineEdit_2.text()
    #     sexe = self.gender_comboBox.currentText()
    #     option_et_niveau = self.class_comboBox_2.currentText()
    #     date_naissance = self.dateNaiss_dateEdit.date().toString('yyyy-MM-dd')
    #     lieu_naissance = self.lieuNaiss_lineEdit.text()
    #     email = self.email_lineEdit.text()
    #     contact = self.contact_lineEdit.text()

    #     # Appeler la fonction pour sauvegarder les données dans la base de données
    #     save_student_to_db(nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact)

    #     # Fermer la boîte de dialogue après l'enregistrement
    #     self.accept()
    def save_student(self):
        # Récupérer les données du formulaire
        nom = self.name_lineEdit.text()
        prenom = self.name_lineEdit_2.text()
        sexe = self.gender_comboBox.currentText()
        option_et_niveau = self.class_comboBox_2.currentText()
        date_naissance = self.dateNaiss_dateEdit.date().toString('yyyy-MM-dd')
        lieu_naissance = self.lieuNaiss_lineEdit.text()
        email = self.email_lineEdit.text()
        contact = self.contact_lineEdit.text()

        # Appeler la fonction pour sauvegarder les données dans la base de données
        success, result = save_student_to_db(nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact)

        if success:
            # Afficher un message de succès avec le nom et le matricule
            QMessageBox.information(self, "Succès", f"L'apprenant {nom} {prenom} a été enregistré avec succès. Le matricule généré est {result}. Veuillez vous rendre à la page 'Paiements Apprenants' pour enregistrer ses paiements et générer automatiquement les reçus.")
            self.accept()  # Fermer la boîte de dialogue après l'enregistrement réussi
        else:
            # Afficher un message d'erreur avec les détails de l'erreur
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors de l'enregistrement de l'apprenant : {result}. Veuillez réessayer ou contacter le service client.")

