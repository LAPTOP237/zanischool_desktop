from fpdf import FPDF
import os
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter

class PDF(FPDF):
    def __init__(self, unit='mm'):
        super().__init__(unit=unit)

    def add_receipt_section(self, y_start, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, section_title, recu_id):
        try:
            # Positionnement de départ de la section
            self.set_y(y_start)

            # Logo de Sainte Famille à gauche
            self.image('icons/logo_centre.png', 5, y_start, 25, 14)  # Ajustez le chemin et les dimensions

            # Logo de Zanischool à droite
            self.image('icons/logo_mc.png', 185, y_start, 14, 14)  # Ajustez le chemin et les dimensions

            self.set_xy(35, y_start)
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'Centre de Formation Professionnelle Sainte Famille', 0, 1, 'L')

            # Titre au centre
            self.set_xy(85, y_start + 5)
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, 'Reçu de paiement', 0, 1, 'L')

            # Numéro de reçu
            date_objet2 = datetime.strptime(date, '%Y-%m-%d')
            self.set_xy(150, y_start + 5)
            self.set_font('Arial', 'B', 11)
            self.cell(0, 10, f'{date_objet2.strftime("%Y")}RP{recu_id}', 0, 1, 'L')

            # Première ligne: Matricule et Date
            self.set_font('Arial', '', 12)
            self.set_xy(20, y_start + 20)
            self.cell(0, 10, 'Matricule:', 0, 0, 'L')
            self.set_xy(40, y_start + 20)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, matricule, 0, 1, 'L')

            self.set_xy(150, y_start + 20)
            self.set_font('Arial', 'B', 12)
            date_objet1 = datetime.strptime(date, '%Y-%m-%d')
            self.cell(0, 10, date_objet1.strftime('%d/%m/%Y'), 0, 1, 'L')

            # Deuxième ligne: Nom, Prénom, Filière et Niveau
            self.set_xy(20, y_start + 27)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Nom et prénoms:', 0, 0, 'L')
            self.set_xy(60, y_start + 27)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'{nom.upper()} {prenom.upper()}', 0, 1, 'L')

            # Troisième ligne: Date et lieu de naissance
            self.set_xy(20, y_start + 34)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Date et lieu de naissance:', 0, 0, 'L')
            self.set_xy(70, y_start + 34)
            self.set_font('Arial', 'B', 12)
            date_objet = datetime.strptime(date_naissance, '%Y-%m-%d')
            self.cell(0, 10, f'{date_objet.strftime("%d/%m/%Y")} à {lieu_naissance.upper()}', 0, 1, 'L')

            # Quatrième ligne: Option et niveau
            self.set_xy(20, y_start + 41)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Option et niveau:', 0, 0, 'L')
            self.set_xy(55, y_start + 41)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'{filiere} {niveau}', 0, 1, 'L')

            # Cinquième ligne: Montant versé
            montant_str = str(montant_verse).replace('.', ',')
            self.set_xy(20, y_start + 48)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Montant versé:', 0, 0, 'L')
            self.set_xy(50, y_start + 48)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, montant_str, 0, 1, 'L')

            # Sixième ligne: Raison
            self.set_xy(130, y_start + 55)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Raison:', 0, 0, 'L')
            self.set_xy(145, y_start + 55)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, raison, 0, 1, 'L')

            # Septième ligne: Montant restant
            montant_str1 = str(montant_restant).replace('.', ',')
            self.set_xy(20, y_start + 55)
            self.set_font('Arial', '', 12)
            self.cell(0, 10, 'Montant restant:', 0, 0, 'L')
            self.set_xy(53, y_start + 55)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, montant_str1, 0, 1, 'L')

            # Signatures
            self.set_xy(30, y_start + 62)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Signature Parent', 0, 1, 'L')

            self.set_xy(150, y_start + 62)
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Signature Caissier(e)', 0, 1, 'L')

            # Filigrane
            self.set_text_color(200, 200, 200)  # Couleur grise pour le filigrane
            self.set_font("Arial", size=9)
            self.rotate(90, x=50, y=y_start + 100)
            self.text(120, y_start + 65, "© M.C. Sarl")  # Positionner le texte au centre avec une rotation

            # Réinitialiser la rotation pour le reste du texte
            self.rotate(0)

            # Réinitialiser la couleur du texte
            self.set_text_color(0, 0, 0)  # Noir pour le texte normal
            # Pied de page
            self.set_xy(90, y_start + 75)
            # Titre de la section (Coupon)
            self.set_font('Arial', 'B', 10)
            self.cell(0, 10, section_title, 0, 1, 'L')

            self.set_xy(150, y_start + 75)
            # Positionnement en bas à gauche
            self.set_font('Arial', 'I', 5)
            self.cell(0, 10, f'Date de génération: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', 0, 0, 'L')

            # Ligne de séparation
            self.set_xy(0, y_start + 85)
            self.line(0, self.get_y(), 210, self.get_y())

        except Exception as e:
            return f"Erreur lors de l'ajout de la section du reçu : {e}"

    def create_receipt(self, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, recu_id):
        try:
            # Ajouter trois sections de reçus sur la même page avec un espacement vertical
            self.add_page()
            y_positions = [5, 93, 186]  # Les positions y de chaque section
            sections = ["Coupon Apprenant", "Coupon Sécretariat", "Coupon Direction"]  # Les titres de chaque section
            for i, y_start in enumerate(y_positions):
                error_message = self.add_receipt_section(y_start, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, sections[i], recu_id)
                if error_message:
                    return error_message
            return None
        except Exception as e:
            return f"Erreur lors de la création du reçu : {e}"

def generate_receipt_pdf(matricule, date_paye, nom, prenom, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, option_et_niveau, recu_id):
    try:

         # Définir le chemin du dossier et du fichier
        dossier_path = os.path.expanduser("~/Documents/MonCompagnonScolaire/Recu")
        if not os.path.exists(dossier_path):
            os.makedirs(dossier_path)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        # Définir le chemin complet du fichier PDF
        fichier_pdf = os.path.join(dossier_path, f"{nom}_{prenom}_recu_{timestamp}.pdf")
        name_file =  f"{nom}_{prenom}_recu_{timestamp}.pdf"
        
        pdf = PDF()
        error_message = pdf.create_receipt(
            matricule, date_paye, nom, prenom, 
            option_et_niveau.split()[0], option_et_niveau.split()[1], 
            date_naissance, lieu_naissance, 
            montant_verse, raison, montant_restant, recu_id
        )

        if error_message:
            return error_message

        pdf.output(fichier_pdf)
        os.startfile(fichier_pdf)
        ajouter_mot_de_passe_pdf(fichier_pdf, 'secret123',name_file)
        return None
    except Exception as e:
        return f"Erreur lors de la génération du PDF : {e}"
    
def ajouter_mot_de_passe_pdf(fichier_pdf, mot_de_passe,name_file):
    # Lire le fichier PDF existant
    reader = PdfReader(fichier_pdf)
    writer = PdfWriter()

    # Copier le contenu du lecteur vers le rédacteur
    for page in reader.pages:
        writer.add_page(page)

    # Définir un mot de passe utilisateur pour le fichier
    writer.encrypt(user_password=mot_de_passe)

    
    dossier_path2 = os.path.expanduser("~/Documents/MonCompagnonScolaire/Recus")
    if not os.path.exists(dossier_path2):
        os.makedirs(dossier_path2)

    fichier_pdf_protege = os.path.join(dossier_path2, name_file)
    
    # Sauvegarder le nouveau fichier PDF avec le mot de passe
    with open(fichier_pdf_protege, 'wb') as fichier_sortie:
        writer.write(fichier_sortie)

    print(f"Le fichier PDF protégé par mot de passe a été sauvegardé sous {fichier_pdf_protege}")


