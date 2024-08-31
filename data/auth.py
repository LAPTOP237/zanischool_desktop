import sqlite3

from data.compte_management import hash_password

db = 'zani_db.db'

def initialize_users():
    conn = sqlite3.connect(db)  # Remplacez par le chemin de votre DB
    cursor = conn.cursor()
    
   # Vérifier si la table est vide
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        hash1 = hash_password('admin')
        hash2 = hash_password('user')
        # La table est vide, insérer des utilisateurs par défaut
        cursor.execute("INSERT INTO users (titulaire, username, password, role) VALUES (?, ?, ?,?)", ('Default','admin', hash1, 'admin'))
        cursor.execute("INSERT INTO users (titulaire, username, password, role) VALUES (?, ?, ?,?)", ('Default','user', hash2, 'user'))
    
    conn.commit()
    conn.close()



