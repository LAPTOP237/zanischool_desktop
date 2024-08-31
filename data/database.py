import sqlite3

db = 'zani_db.db'

def initialize_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    print("Creating tables...")
    # Créer la table students si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricule TEXT UNIQUE,
            nom TEXT,
            prenom TEXT,
            sexe TEXT,
            option_et_niveau TEXT,
            date_naissance DATE,
            lieu_naissance TEXT,
            email TEXT,
            contact TEXT,
            created_at DATE DEFAULT (datetime('now')),
            last_update DATE DEFAULT (datetime('now'))
        )
    ''')

    # Création de la table users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulaire TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT CHECK(role IN ('admin', 'user')) NOT NULL
        );
    ''')

    # Création de la table annee_scolaire
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS annee_scolaire (
            id_scolarite	INTEGER,
            debut	INT,
            fin	INT,
            PRIMARY KEY("id_scolarite" AUTOINCREMENT)
        );
            ''')
    
    # Création de la table dossier ( dossier de l'apprenant pour chaque année scolaire)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "dossier" (
	"id_dossier"	INTEGER NOT NULL,
	"id_eleve"	TEXT,
	"id_etude"	INT,
	"id_scolarite"	INT,
	PRIMARY KEY("id_dossier" AUTOINCREMENT),
	FOREIGN KEY("id_scolarite") REFERENCES "annee_scolaire"("id_scolarite"),
	FOREIGN KEY("id_etude") REFERENCES "etude"("id_etude"),
	FOREIGN KEY("id_eleve") REFERENCES "students"("matricule")
);
            ''')
     # Création de la table etude ( concatenation de l'option et niveau )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "etude" (
	"id_etude"	INTEGER,
	"id_niveau"	TEXT,
	"id_filiere"	TEXT,
	"frais_scolaire"	INT,
	PRIMARY KEY("id_etude" AUTOINCREMENT),
	FOREIGN KEY("id_niveau") REFERENCES "niveau"("valeur"),
	FOREIGN KEY("id_filiere") REFERENCES "filiere"("sigle")
);
            ''')
    
     # Création de la table filiere 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "filiere" (
	"sigle"	TEXT NOT NULL,
    "valeur"	TEXT,
	PRIMARY KEY("sigle")
);
            ''')
    
    # Création de la table niveau 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "niveau" (
	"valeur"	TEXT NOT NULL,
	PRIMARY KEY("valeur")
);
            ''')
    
    # Création de la table niveau 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "recu" (
	"id_recu"	INTEGER,
	"id_dossier"	INT,
    "raison"   TEXT, 
	"montant_verse"	DOUBLE,
	"montant_restant"	DOUBLE,
    "solde" DOUBLE,
	"date_paye" DATE,
	PRIMARY KEY("id_recu" AUTOINCREMENT),
	FOREIGN KEY("id_dossier") REFERENCES "dossier"("id_dossier")
);
            ''')
    
     
     # Création de la table Matiere 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "matiere" (
	"id_matiere"	INTEGER,
	"intitule"	TEXT,
	PRIMARY KEY("id_matiere" AUTOINCREMENT)
);
            ''')
    # Création de la table note 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "note" (
	"id_note"	INTEGER,
	"id_matiere"	INT,
	"id_dossier"	INT,
	"valeur"	REAL,
	PRIMARY KEY("id_note" AUTOINCREMENT),
	FOREIGN KEY("id_dossier") REFERENCES "dossier"("id_dossier"),
	FOREIGN KEY("id_matiere") REFERENCES "matiere"("id_matiere")
);
            ''')
    
    conn.commit()
    conn.close()
