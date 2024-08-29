import sqlite3
from data.database import initialize_db

db = 'zani_db.db'

def create_filiere(sigle, valeur):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO filiere (sigle, valeur)
    VALUES (?, ?)
    """, (sigle, valeur))

    conn.commit()
    conn.close()

def create_niveau(valeur):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO niveau (valeur)
    VALUES (?)
    """, (valeur,))

    conn.commit()
    conn.close()

def create_etude(id_niveau, id_filiere, frais_scolaire):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO etude (id_niveau, id_filiere, frais_scolaire)
    VALUES (?, ?, ?)
    """, (id_niveau, id_filiere, frais_scolaire))

    conn.commit()
    conn.close()

def create_annee_scolaire(debut, fin):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO annee_scolaire (debut, fin)
    VALUES (?, ?)
    """, (debut, fin))

    conn.commit()
    conn.close()

def create_missing_dossiers(annee_debut, annee_fin):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Récupérer l'ID de l'année scolaire
    cursor.execute("""
    SELECT id_scolarite FROM annee_scolaire WHERE debut = ? AND fin = ?
    """, (annee_debut, annee_fin))
    id_scolarite = cursor.fetchone()

    if not id_scolarite:
        print(f"Année scolaire {annee_debut}-{annee_fin} non trouvée.")
        return
    id_scolarite = id_scolarite[0]

    # Récupérer tous les étudiants qui n'ont pas de dossier pour cette année académique
    cursor.execute("""
    SELECT s.matricule, e.id_etude FROM students s
    JOIN etude e ON s.option_et_niveau = e.id_filiere || ' ' || e.id_niveau
    WHERE NOT EXISTS (
        SELECT 1 FROM dossier d
        WHERE d.id_eleve = s.matricule AND d.id_scolarite = ?
    )
    """, (id_scolarite,))

    students_without_dossier = cursor.fetchall()

    # Créer les dossiers pour les étudiants qui n'en ont pas
    for student in students_without_dossier:
        matricule, id_etude = student
        cursor.execute("""
        INSERT INTO dossier (id_eleve, id_etude, id_scolarite)
        VALUES (?, ?, ?)
        """, (matricule, id_etude, id_scolarite))

    conn.commit()
    conn.close()
    print(f"Dossiers créés pour les étudiants sans dossier pour l'année académique {annee_debut}-{annee_fin}.")

def check_filiere_exists(sigle):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM filiere WHERE sigle = ?", (sigle,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

def check_niveau_exists(valeur):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM niveau WHERE valeur = ?", (valeur,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

def check_etude_exists(id_niveau, id_filiere):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM etude WHERE id_niveau = ? AND id_filiere = ?", (id_niveau, id_filiere))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

def check_annee_scolaire_exists(debut, fin):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM annee_scolaire WHERE debut = ? AND fin = ?", (debut, fin))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

def initialize_centre():
    # Créer les filières
    filieres = [('COM', 'Couture'), ('ESCO', 'Esthétique'), ('ATELIER', 'Atelier')]
    for sigle, valeur in filieres:
        if not check_filiere_exists(sigle):
            create_filiere(sigle, valeur)

    # Créer les niveaux
    niveaux = ['1A', '1B', '2A', '2B', '3', 'A', 'B']
    for niveau in niveaux:
        if not check_niveau_exists(niveau):
            create_niveau(niveau)

    # Créer les études avec les frais de scolarité
    etudes = [
        ('1A', 'COM', 80000),
        ('1B', 'COM', 80000),
        ('2A', 'COM', 90000),
        ('2B', 'COM', 90000),
        ('3', 'COM', 100000),
        ('A', 'ATELIER', 120000),
        ('B', 'ATELIER', 120000),
        ('1A', 'ESCO', 100000),
        ('1B', 'ESCO', 100000),
        ('2A', 'ESCO', 120000),
        ('2B', 'ESCO', 120000),
        ('3', 'ESCO', 160000)
    ]
    
    for niveau, filiere, frais in etudes:
        if not check_etude_exists(niveau, filiere):
            create_etude(niveau, filiere, frais)

    # Créer les années scolaires
    annees_scolaires = [(2024, 2025), (2023, 2024), (2022, 2023)]
    for debut, fin in annees_scolaires:
        if not check_annee_scolaire_exists(debut, fin):
            create_annee_scolaire(debut, fin)

    # Utiliser la fonction pour créer les dossiers pour l'année académique 2024-2025
    create_missing_dossiers(2024, 2025)

    print("tout est ok")

initialize_db()
# Appel de la fonction pour initialiser le centre
print('db crée...')
initialize_centre()
