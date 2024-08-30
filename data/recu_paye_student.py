from fpdf import FPDF
import os
from datetime import datetime

class PDF(FPDF):
    def __init__(self, unit='mm'):
        super().__init__(unit=unit)

    def add_receipt_section(self, y_start, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, section_title):
        # Positionnement de départ de la section
        self.set_y(y_start)
        
        # Logo de Sainte Famille à gauche
        self.image('icons/logo_centre.png', 5, y_start, 25, 14)  # Ajustez le chemin et les dimensions
        
        # Logo de Zanischool à droite
        self.image('icons/logo_mc.png', 185, y_start, 14, 14)  # Ajustez le chemin et les dimensions
        
        self.set_xy(35,y_start)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Centre de Formation Professionnelle Sainte Famille', 0, 1, 'L')
        
        # Titre au centre
        self.set_xy(85, y_start + 5)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Reçu de paiement', 0, 1, 'L')

        # Première ligne: Matricule et Date
        self.set_font('Arial', '', 12)
        self.set_xy(20, y_start + 20)
        self.cell(0, 10, 'Matricule:', 0, 0, 'L')
        self.set_xy(40, y_start + 20)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, matricule, 0, 1, 'L')
        
        self.set_xy(150, y_start + 20)
        self.set_font('Arial', 'B', 12)
        date_objet1 = datetime.strptime(date, '%d-%m-%Y')
        date_formatee1 = date_objet1.strftime('%d/%m/%Y')
        self.cell(0, 10, date_formatee1, 0, 1, 'L')
        
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
        date_formatee = date_objet.strftime('%d/%m/%Y')
        self.cell(0, 10, f'{date_formatee} à {lieu_naissance.upper()}', 0, 1, 'L')
        
        # Quatrième ligne:
        self.set_xy(20, y_start + 41) 
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Option et niveau:', 0, 0, 'L')
        self.set_xy(55, y_start + 41) 
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'{filiere} {niveau}', 0, 1, 'L')


        montant_str = str(montant_verse)  # Conversion en string
        montant_str = montant_str.replace('.', ',')  # Remplacement du point par une virgule
        # Cinquième ligne:
        self.set_xy(20, y_start + 48) 
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Montant versé:', 0, 0, 'L')
        self.set_xy(50, y_start + 48) 
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, montant_str, 0, 1, 'L')

        # Sixième ligne:
        self.set_xy(130, y_start + 55) 
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Raison:', 0, 0, 'L')
        self.set_xy(145, y_start + 55) 
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, raison, 0, 1, 'L')

        montant_str1 = str(montant_restant)  # Conversion en string
        montant_str1 = montant_str1.replace('.', ',')  # Remplacement du point par une virgule
        # Septième ligne:
        self.set_xy(20, y_start + 55) 
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Montant restant:', 0, 0, 'L')
        self.set_xy(53, y_start + 55) 
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, montant_str1, 0, 1, 'L')

        # SIGNATURE
        self.set_xy(30, y_start + 62)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Signature Parent', 0, 1, 'L')

         # SIGNATURE
        self.set_xy(150, y_start + 62)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Signature Caissier(e)', 0, 1, 'L')
        
        # # Ajouter un filigrane
        self.set_text_color(200, 200, 200)  # Couleur grise pour le filigrane
        self.set_font("Arial", size=9)
        self.rotate(90,x=50,y=y_start+100)
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

    def create_receipt(self, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant):
        # Ajouter trois sections de reçus sur la même page avec un espacement vertical
        self.add_page()
        y_positions = [5, 93, 186]  # Les positions y de chaque section
        sections = ["Coupon Apprenant", "Coupon Sécretariat", "Coupon Direction"]  # Les titres de chaque section
        for i, y_start in enumerate(y_positions):
            self.add_receipt_section(y_start, matricule, date, nom, prenom, filiere, niveau, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, sections[i])

def generate_receipt_pdf(matricule, date_paye, annee_scolaire, nom, prenom, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, option_et_niveau):
    # Définir le chemin du dossier et du fichier
    dossier_documents = os.path.expanduser("~/Documents/Zanischool/Recu")
    if not os.path.exists(dossier_documents):
        os.makedirs(dossier_documents)
    
    # Format de la date pour le fichier
    date_formatee = datetime.strptime(date_paye, "%Y-%m-%d").strftime("%d-%m-%Y")
    nom_fichier = f"Recu_{matricule}_{date_formatee}.pdf"
    chemin_fichier = os.path.join(dossier_documents, nom_fichier)

    # Vérifier si le fichier existe et ajouter un suffixe si nécessaire
    compteur = 1
    chemin_fichier_unique = chemin_fichier

    while os.path.exists(chemin_fichier_unique):
        # Obtenir le nom de fichier sans extension et l'extension
        nom1, extension = os.path.splitext(nom_fichier)
        
        # Créer un nouveau nom de fichier avec le compteur
        nouveau_nom_fichier = f"{nom1}_{compteur:02}{extension}"
        
        # Mettre à jour le chemin du fichier unique
        chemin_fichier_unique = os.path.join(dossier_documents, nouveau_nom_fichier)
        
        # Incrémenter le compteur pour la prochaine vérification
        compteur += 1

    # Création du PDF
    pdf = PDF()
    pdf.create_receipt(matricule, date_formatee, nom, prenom, option_et_niveau.split()[0], option_et_niveau.split()[1], date_naissance, lieu_naissance, montant_verse, raison, montant_restant)
    pdf.output(chemin_fichier_unique)

    # Ouvrir le PDF automatiquement
    os.startfile(chemin_fichier_unique)

    print(f"PDF généré et enregistré sous : {chemin_fichier_unique}")

# Exemple d'utilisation
# generate_receipt_pdf(
#     matricule='123456',
#     date_paye='2024-08-20',
#     annee_scolaire='2024-2025',
#     nom='Doe',
#     prenom='John',
#     date_naissance='2002-01-20',
#     lieu_naissance='Ville',
#     montant_verse='80,000 FCFA',
#     raison='Inscription',
#     montant_restant='20,000 FCFA',
#     option_et_niveau='COM 1A'
# )
