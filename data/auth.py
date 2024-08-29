import sqlite3

db = 'zani_db.db'

def initialize_users():
    conn = sqlite3.connect(db)  # Remplacez par le chemin de votre DB
    cursor = conn.cursor()
    
   # Vérifier si la table est vide
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # La table est vide, insérer des utilisateurs par défaut
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('admin', 'admin', 'admin'))
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('user', 'user', 'user'))
    
    conn.commit()
    conn.close()



