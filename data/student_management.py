import sqlite3
from datetime import datetime
from data.exportManager import generer_pdf_recu
from data.recu_paye_student import generate_receipt_pdf

import os
import ctypes

def get_connection():
    """Retourne une connexion à la base de données."""
    return sqlite3.connect('data/zani_db.db')

def initialize_db():
    """Initialise la base de données et crée les tables si elles n'existent pas."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        matricule TEXT PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        sexe TEXT NOT NULL,
        option_et_niveau TEXT NOT NULL,
        date_naissance TEXT NOT NULL,
        lieu_naissance TEXT NOT NULL,
        email TEXT,
        contact TEXT,
        created_at TEXT NOT NULL,
        last_update TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def get_all_students():
    """Retourne tous les étudiants de la base de données."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_etudes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_niveau, id_filiere FROM etude")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(matricule):
    """Supprime un étudiant de la base de données par matricule."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE matricule = ?", (matricule,))
    conn.commit()
    conn.close()

def search_students(search_text):
    """Retourne les étudiants qui correspondent au texte de recherche."""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT * FROM students
        WHERE nom LIKE ? OR prenom LIKE ? OR email LIKE ? OR contact LIKE ?
    """
    params = [f"%{search_text}%" for _ in range(4)]
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

def filter_students(gender_filter=None, class_filter=None):
    """Retourne les étudiants filtrés par sexe et classe."""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM students WHERE 1=1"
    params = []
    if gender_filter:
        query += " AND sexe = ?"
        params.append(gender_filter)
    if class_filter:
        query += " AND option_et_niveau = ?"
        params.append(class_filter)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_matricule(sexe):
    current_year = datetime.now().strftime("%Y")
    prefix = 'F' if sexe == 'Féminin' else 'M'  # Utiliser 'M' pour Masculin
    conn = sqlite3.connect('data/zani_db.db')
    cursor = conn.cursor()
    
    # Trouver le dernier matricule de l'année en cours
    cursor.execute("SELECT matricule FROM students WHERE matricule LIKE ? ORDER BY matricule DESC LIMIT 1", (f"{current_year}{prefix}%",))
    last_matricule = cursor.fetchone()
    number = 1
    if last_matricule:
        last_number = int(last_matricule[0][6:])  # Extrait le numéro de l'ancien matricule
        number = last_number + 1

    matricule = f"{current_year}{prefix}{number:05d}"
    conn.close()
    return matricule
def update_student(matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact):
    """Met à jour les informations d'un étudiant dans la base de données."""
    conn = get_connection()
    cursor = conn.cursor()

    # Générer un nouveau matricule si le sexe a changé
    current_year = datetime.now().strftime("%Y")
    prefix = 'F' if sexe == 'Féminin' else 'M'
    new_matricule = f"{current_year}{prefix}{matricule[6:]}"

    cursor.execute('''
        UPDATE students
        SET matricule = ?,
            nom = ?,
            prenom = ?,
            sexe = ?,
            option_et_niveau = ?,
            date_naissance = ?,
            lieu_naissance = ?,
            email = ?,
            contact = ?,
            last_update = datetime('now')
        WHERE matricule = ?
    ''', (new_matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact, matricule))

    conn.commit()
    conn.close()


# def save_student_to_db(nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact):
#     matricule = generate_matricule(sexe)
    
#     conn = sqlite3.connect('data/zani_db.db')
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         INSERT INTO students (matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact, created_at, last_update)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
#     ''', (matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact))
    
#     conn.commit()
#     conn.close()


def save_student_to_db(nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact):
    matricule = generate_matricule(sexe)
    
    try:
        conn = sqlite3.connect('data/zani_db.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO students (matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact, created_at, last_update)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
        ''', (matricule, nom, prenom, sexe, option_et_niveau, date_naissance, lieu_naissance, email, contact))
        
        conn.commit()
        conn.close()

        return True, matricule  # Retourner True et le matricule généré si l'insertion est un succès
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'apprenant: {e}")
        return False, str(e)  # Retourner False et le message d'erreur si une exception se produit


def get_student_by_matricule(matricule):
    """Récupère les données d'un étudiant à partir de son matricule."""
    conn = sqlite3.connect('data/zani_db.db')  
    cursor = conn.cursor()
    
    query = "SELECT * FROM students WHERE matricule = ?"
    cursor.execute(query, (matricule,))
    student_data = cursor.fetchone()
    
    conn.close()
    
    if student_data:
        # Supposons que les colonnes de la table Eleve soient dans cet ordre :
        columns = ['id','matricule', 'nom', 'prenom', 'sexe', 'option_et_niveau', 'date_naissance', 'lieu_naissance', 'email', 'contact']
        
        # Créer un dictionnaire avec les données de l'étudiant
        student_info = dict(zip(columns, student_data))
        print(student_info)
        return student_info
    else:
        return None  # Retourne None si l'étudiant n'est pas trouvé
    
def get_students_from_db():
    # Connexion à la base de données
    conn = sqlite3.connect('data/zani_db.db')
    cursor = conn.cursor()
    
    # Requête SQL pour obtenir les données des étudiants
    query = "SELECT matricule, nom, prenom FROM students"
    cursor.execute(query)
    
    # Récupération des résultats
    rows = cursor.fetchall()
    
    # Fermeture de la connexion
    conn.close()
    
    # Formatage des résultats en liste de dictionnaires
    students = [
        {"matricule": row[0], "nom": row[1], "prenom": row[2]}
        for row in rows
    ]
    
    return students

def get_etude_id_by_matricule(matricule):
    """Récupère l'ID de l'étude d'un étudiant à partir de son matricule."""
    conn = sqlite3.connect('data/zani_db.db')
    cursor = conn.cursor()

    # Récupération de l'information option_et_niveau de l'étudiant
    query = "SELECT option_et_niveau FROM students WHERE matricule = ?"
    cursor.execute(query, (matricule,))
    result = cursor.fetchone()
    
    if result:
        option_et_niveau = result[0]
        try:
            # Supposons que option_et_niveau soit sous la forme "id_filiere id_niveau"
            id_filiere, id_niveau = option_et_niveau.split()

            # Requête pour récupérer l'ID de l'étude
            query = "SELECT id_etude FROM etude WHERE id_filiere = ? AND id_niveau = ?"
            cursor.execute(query, (id_filiere, id_niveau))
            etude_id = cursor.fetchone()
            
            conn.close()
            
            if etude_id:
                return etude_id[0]  # Retourne l'ID de l'étude
            else:
                print("Aucune étude trouvée pour les données fournies.")
                return None
        except ValueError:
            print("Erreur de format dans option_et_niveau.")
            return None
    else:
        conn.close()
        print("Aucun étudiant trouvé avec ce matricule.")
        return None
    

#Enregistrer le paiment d'un etudiant dans la bd
# def save_payement_to_db(matricule, raison, montant_verse, date_paye, annee_scolaire):
    
#     conn = sqlite3.connect('data/zani_db.db')
#     cursor = conn.cursor()

#     datedeb, datefin = parse_annee_scolaire(annee_scolaire)

#      # Vérifier si l'année scolaire existe déjà, sinon la créer
#     cursor.execute("""
#         SELECT id_scolarite FROM annee_scolaire 
#         WHERE debut = ? AND fin = ?
#     """, (datedeb, datefin))
#     annee_scolarite1 = cursor.fetchone()
    
#     if annee_scolarite1 is None:
#         cursor.execute("""
#             INSERT INTO annee_scolaire (debut, fin)
#             VALUES (?, ?)
#         """, (datedeb, datefin))
#         annee_scolarite_id = cursor.lastrowid
#     else:
#         annee_scolarite_id = annee_scolarite1[0]
   
#    # Remplacer la virgule par un point pour les conversions
#     montant_verse = montant_verse.replace(',', '.')
    
#     try:
#         montant_verse = float(montant_verse)
#     except ValueError:
#         print("Erreur de conversion pour le montant versé.")
#         return
    
#    # Récupérer l'id_dossier correspondant à l'étudiant pour l'année scolaire donnée
#     cursor.execute("""
#         SELECT d.id_dossier, e.frais_scolaire, r.solde, s.nom, s.prenom, s.date_naissance, s.lieu_naissance, s.option_et_niveau
#         FROM dossier d
#         JOIN students s ON d.id_eleve = s.matricule
#         JOIN etude e ON d.id_etude = e.id_etude
#         LEFT JOIN recu r ON d.id_dossier = r.id_dossier
#         WHERE s.matricule = ? AND d.id_scolarite = ?
#     """, (matricule, annee_scolarite_id))
    
#     result = cursor.fetchone()
    
#     if not result:
#         print("Dossier non trouvé.")
#          # Créer le nouveau dossier
#         cursor.execute("""
#             INSERT INTO dossier (id_eleve, id_scolarite, id_etude)
#             VALUES (?, ?, ?)
#         """, (matricule, annee_scolarite_id, get_etude_id_by_matricule(matricule)))
#         conn.commit()
#         print("Nouveau dossier créé avec succès.")

#       # Récupérer l'id_dossier correspondant à l'étudiant pour l'année scolaire donnée
#         cursor.execute("""
#         SELECT d.id_dossier, e.frais_scolaire, r.solde, s.nom, s.prenom, s.date_naissance, s.lieu_naissance, s.option_et_niveau
#         FROM dossier d
#         JOIN students s ON d.id_eleve = s.matricule
#         JOIN etude e ON d.id_etude = e.id_etude
#         LEFT JOIN recu r ON d.id_dossier = r.id_dossier
#         WHERE s.matricule = ? AND d.id_scolarite = ?
#     """, (matricule, annee_scolarite_id))
    
#         result = cursor.fetchone()

#     id_dossier, frais_scolaire, solde, nom, prenom, date_naissance, lieu_naissance, option_et_niveau= result

#     # Calculer le nouveau solde et le montant restant
#     id_dossier1 = id_dossier
#     cursor.execute("""
#             SELECT montant_restant FROM recu WHERE id_dossier = ? ORDER BY id_recu DESC LIMIT 1;
#         """, (id_dossier1,))
#     result1 = cursor.fetchone()

#     if result1 :
#         montant_restant = result1[0]
#         montant_restant = montant_restant - montant_verse
#         nouveau_solde = frais_scolaire - montant_restant
#     else:
#         montant_restant = frais_scolaire - montant_verse
#         nouveau_solde = frais_scolaire - montant_restant
        

#     # Insérer le nouveau reçu dans la base de données
#     cursor.execute("""
#         INSERT INTO recu (id_dossier, raison, montant_verse, montant_restant, solde, date_paye)
#         VALUES (?, ?, ?, ?, ?, ?)
#     """, (id_dossier, raison, montant_verse, montant_restant, nouveau_solde, date_paye))

#     conn.commit()
#     conn.close()

#     # Générer le PDF du reçu après l'enregistrement
#     generate_receipt_pdf(matricule, date_paye, annee_scolaire, nom, prenom, date_naissance, lieu_naissance, montant_verse, raison, montant_restant,option_et_niveau)


#     print("Paiement enregistré avec succès.")

def save_payement_to_db(matricule, raison, montant_verse, date_paye, annee_scolaire):
    conn = sqlite3.connect('data/zani_db.db')
    cursor = conn.cursor()
    
    datedeb, datefin = parse_annee_scolaire(annee_scolaire)

    try:
        # Vérifier si l'année scolaire existe déjà, sinon la créer
        cursor.execute("""
            SELECT id_scolarite FROM annee_scolaire 
            WHERE debut = ? AND fin = ?
        """, (datedeb, datefin))
        annee_scolarite1 = cursor.fetchone()
        
        if annee_scolarite1 is None:
            cursor.execute("""
                INSERT INTO annee_scolaire (debut, fin)
                VALUES (?, ?)
            """, (datedeb, datefin))
            annee_scolarite_id = cursor.lastrowid
        else:
            annee_scolarite_id = annee_scolarite1[0]

        # Remplacer la virgule par un point pour les conversions
        montant_verse = montant_verse.replace(',', '.')
        montant_verse = float(montant_verse)
        
        # Récupérer l'id_dossier correspondant à l'étudiant pour l'année scolaire donnée
        cursor.execute("""
            SELECT d.id_dossier, e.frais_scolaire, r.solde, s.nom, s.prenom, s.date_naissance, s.lieu_naissance, s.option_et_niveau
            FROM dossier d
            JOIN students s ON d.id_eleve = s.matricule
            JOIN etude e ON d.id_etude = e.id_etude
            LEFT JOIN recu r ON d.id_dossier = r.id_dossier
            WHERE s.matricule = ? AND d.id_scolarite = ?
        """, (matricule, annee_scolarite_id))
        
        result = cursor.fetchone()
        
        if not result:
            # Créer le nouveau dossier
            cursor.execute("""
                INSERT INTO dossier (id_eleve, id_scolarite, id_etude)
                VALUES (?, ?, ?)
            """, (matricule, annee_scolarite_id, get_etude_id_by_matricule(matricule)))
            conn.commit()
            print("Nouveau dossier créé avec succès.")
            
            # Récupérer l'id_dossier correspondant à l'étudiant pour l'année scolaire donnée
            cursor.execute("""
                SELECT d.id_dossier, e.frais_scolaire, r.solde, s.nom, s.prenom, s.date_naissance, s.lieu_naissance, s.option_et_niveau
                FROM dossier d
                JOIN students s ON d.id_eleve = s.matricule
                JOIN etude e ON d.id_etude = e.id_etude
                LEFT JOIN recu r ON d.id_dossier = r.id_dossier
                WHERE s.matricule = ? AND d.id_scolarite = ?
            """, (matricule, annee_scolarite_id))
            
            result = cursor.fetchone()

        id_dossier, frais_scolaire, solde, nom, prenom, date_naissance, lieu_naissance, option_et_niveau = result

        # Calculer le nouveau solde et le montant restant
        cursor.execute("""
            SELECT montant_restant FROM recu WHERE id_dossier = ? ORDER BY id_recu DESC LIMIT 1;
        """, (id_dossier,))
        result1 = cursor.fetchone()

        if result1:
            montant_restant = result1[0]
            montant_restant = montant_restant - montant_verse
            nouveau_solde = frais_scolaire - montant_restant
        else:
            montant_restant = frais_scolaire - montant_verse
            nouveau_solde = frais_scolaire - montant_restant

        # Insérer le nouveau reçu dans la base de données
        cursor.execute("""
            INSERT INTO recu (id_dossier, raison, montant_verse, montant_restant, solde, date_paye)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_dossier, raison, montant_verse, montant_restant, nouveau_solde, date_paye))

        conn.commit()

        # Générer le PDF du reçu après l'enregistrement
        generate_receipt_pdf(matricule, date_paye, annee_scolaire, nom, prenom, date_naissance, lieu_naissance, montant_verse, raison, montant_restant, option_et_niveau)
        
        # Ouvrir le PDF généré pour impression
        # pdf_path = os.path.join('Documents/Recus', f'{matricule}_{date_paye}.pdf')
        # if os.path.isfile(pdf_path):
        #     os.startfile(pdf_path, 'print')
        
        return "Le paiement a été enregistré avec succès et le reçu est enregistré dans Documents/Recus et s'ouvrira automatiquement pour l'impression."
    
    except Exception as e:
        print(f"Erreur: {e}")
        return "Une erreur s'est produite, veuillez réessayer ou contacter le service client."

    finally:
        conn.close()

#Creer un new dossier etudiant
def create_new_dossier(matricule, debut_annee, fin_annee, niveau, filiere):
    # Connexion à la base de données
    conn = sqlite3.connect('data/zani_db.db')
    cursor = conn.cursor()
    
    # Vérifier si l'année scolaire existe déjà, sinon la créer
    cursor.execute("""
        SELECT id_scolarite FROM annee_scolaire 
        WHERE debut = ? AND fin = ?
    """, (debut_annee, fin_annee))
    annee_scolarite = cursor.fetchone()
    
    if annee_scolarite is None:
        cursor.execute("""
            INSERT INTO annee_scolaire (debut, fin)
            VALUES (?, ?)
        """, (debut_annee, fin_annee))
        annee_scolarite_id = cursor.lastrowid
    else:
        annee_scolarite_id = annee_scolarite[0]
    
    # Vérifier si l'étude existe déjà, sinon la créer
    cursor.execute("""
        SELECT id_etude FROM etude 
        WHERE id_niveau = ? AND id_filiere = ?
    """, (niveau, filiere))
    etude = cursor.fetchone()
    
    if etude is None:
        cursor.execute("""
            INSERT INTO etude (id_niveau, id_filiere)
            VALUES (?, ?)
        """, (niveau, filiere))
        etude_id = cursor.lastrowid
    else:
        etude_id = etude[0]
    
    # Vérifier si un dossier existe déjà pour cet élève, cette année et cette étude
    cursor.execute("""
        SELECT id_dossier FROM dossier 
        WHERE id_eleve = ? AND id_scolarite = ? AND id_etude = ?
    """, (matricule, annee_scolarite_id, etude_id))
    dossier = cursor.fetchone()
    
    if dossier is None:
        # Créer le nouveau dossier
        cursor.execute("""
            INSERT INTO dossier (id_eleve, id_scolarite, id_etude)
            VALUES (?, ?, ?)
        """, (matricule, annee_scolarite_id, etude_id))
        conn.commit()
        print("Nouveau dossier créé avec succès.")
    else:
        print("Un dossier existe déjà pour cet élève, cette année académique et cette étude.")
    
    # Fermeture de la connexion à la base de données
    conn.close()

def parse_annee_scolaire(annee_scolaire):
    """
    Convertit une chaîne de texte de la forme '2024 - 2025' en deux variables :
    datedeb et datefin.

    :param annee_scolaire: Chaîne de texte représentant l'année scolaire, par exemple '2024 - 2025'
    :return: Tuple (datedeb, datefin) où datedeb et datefin sont des entiers.
    """
    try:
        # Diviser la chaîne de texte en deux parties
        datedeb_str, datefin_str = annee_scolaire.split(' - ')
        
        # Convertir les parties en entiers
        datedeb = int(datedeb_str.strip())
        datefin = int(datefin_str.strip())
        
        return datedeb, datefin
    except ValueError:
        raise ValueError("La chaîne d'année scolaire n'est pas au format attendu 'YYYY - YYYY'")
    except Exception as e:
        raise e

