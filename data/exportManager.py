import pandas as pd
from fpdf import FPDF
from PySide6.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime
import os

class ExportManager:
    def __init__(self, parent=None):
        self.parent = parent

    def export_to_pdf(self, students_data):
        """Exporte les données des étudiants en fichier PDF."""
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Enregistrer le fichier PDF", "", "Fichiers PDF (*.pdf)")
        if not file_name:
            return  # Annuler si aucun fichier n'est sélectionné

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Ajouter un titre
        pdf.cell(200, 10, txt="Liste des Apprenants", ln=True, align='C')

        # Ajouter les données des étudiants
        for student in students_data:
            print(student)
            student_info = f"{student['Matricule']} {student['Nom']} {student['Prénoms']} {student['Email']} - {student['Contact']}"
            pdf.cell(200, 10, txt=student_info, ln=True)

        pdf.output(file_name)
        QMessageBox.information(self.parent, "Succès", "Le fichier PDF a été créé avec succès.")

    def export_to_excel(self, students_data):
        """Exporte les données des étudiants en fichier Excel."""
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Enregistrer le fichier Excel", "", "Fichiers Excel (*.xlsx)")
        if not file_name:
            return  # Annuler si aucun fichier n'est sélectionné

        # Convertir les données en DataFrame
        df = pd.DataFrame(students_data)

        # Enregistrer le DataFrame dans un fichier Excel
        df.to_excel(file_name, index=False)
        QMessageBox.information(self.parent, "Succès", "Le fichier Excel a été créé avec succès.")


def generer_pdf_recu( matricule, date_paye, annee_scolaire, nom, prenom, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, option_et_niveau):
     # Définir le chemin du dossier et du fichier
    dossier_documents = os.path.expanduser("~/Documents/Zanischool/Recu")
    if not os.path.exists(dossier_documents):
        os.makedirs(dossier_documents)
    
    # Définir le nom du fichier PDF
    date_formatee = datetime.strptime(date_paye, "%Y-%m-%d").strftime("%d-%m-%Y")
    nom_fichier = f"Recu_{matricule}_{date_formatee}.pdf"
    chemin_fichier = os.path.join(dossier_documents, nom_fichier)

    # Créer le PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Définir les informations à afficher
    lignes = [
        f"Date: {date_paye}",
        f"Année Scolaire: {annee_scolaire}",
        f"Matricule: {matricule}",
        f"Nom: {nom}",
        f"Prénom: {prenom}",
        f"Filiere et Niveau: {option_et_niveau}",
        f"Date de Naissance: {date_naissance}",
        f"Lieu de Naissance: {lieu_naissance}",
        f"Montant Payé: {montant_verse}",
        f"Raison: {raison}",
        f"Montant Restant: {montant_restant}"
    ]
    
    # Ajouter les informations au PDF
    for ligne in lignes:
        pdf.cell(0, 10, ligne, ln=True)
    
    # Ajouter des lignes pour séparer les sections
    pdf.ln(10)
    pdf.cell(0, 10, '-' * 190, ln=True)
    pdf.ln(10)

    # Répéter les informations dans chaque section
    for _ in range(3):  # Répéter 3 fois pour chaque section
        pdf.cell(0, 10, f"Date: {date_paye}", ln=True)
        pdf.cell(0, 10, f"Année Scolaire: {annee_scolaire}", ln=True)
        pdf.cell(0, 10, f"Matricule: {matricule}", ln=True)
        pdf.cell(0, 10, f"Nom: {nom}", ln=True)
        pdf.cell(0, 10, f"Prénom: {prenom}", ln=True)
        pdf.cell(0, 10, f"Date de Naissance: {date_naissance}", ln=True)
        pdf.cell(0, 10, f"Lieu de Naissance: {lieu_naissance}", ln=True)
        pdf.cell(0, 10, f"Montant Payé: {montant_verse}", ln=True)
        pdf.cell(0, 10, f"Raison: {raison}", ln=True)
        pdf.cell(0, 10, f"Montant Restant: {montant_restant}", ln=True)
        pdf.ln(10)
        pdf.cell(0, 10, '-' * 190, ln=True)
        pdf.ln(10)
    
    # Enregistrer le PDF
    pdf.output(chemin_fichier)
    
    # Ouvrir le PDF automatiquement
    os.startfile(chemin_fichier)

    print(f"PDF généré et enregistré sous : {chemin_fichier}")