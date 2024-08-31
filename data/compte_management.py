import sqlite3
import hashlib

db = 'zani_db.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

def add_user(titulaire, username, password, role):
    try:
        # Vérifier si le nom d'utilisateur existe déjà
        cursor.execute('SELECT COUNT(*) FROM users WHERE username = ?', (username,))
        user_exists = cursor.fetchone()[0]
        
        if user_exists:
            return "Nom d'utilisateur déjà existant."
        
        # Hachage du mot de passe
        hashed_password = hash_password(password)
        
        # Insertion du nouvel utilisateur
        cursor.execute('''
            INSERT INTO users (titulaire, username, password, role)
            VALUES (?, ?, ?, ?)
        ''', (titulaire, username, hashed_password, role))
        conn.commit()
        
        return "Compte créé avec succès."

    except sqlite3.DatabaseError as db_err:
        # Gestion des erreurs de base de données
        print(f"Erreur de base de données : {str(db_err)}")
        return "Erreur lors de l'enregistrement du compte."
    
    except Exception as e:
        # Gestion d'autres erreurs
        print(f"Erreur : {str(e)}")
        return "Erreur lors de l'enregistrement du compte."
    
def get_users():
    cursor.execute('SELECT titulaire, username, role FROM users')
    rows = cursor.fetchall()
    return rows

def update_user(user_id, titulaire, username, role):
    try:
        cursor.execute('''
            UPDATE users
            SET titulaire = ?, username = ?, role = ?
            WHERE id = ?
        ''', (titulaire, username, role, user_id))
        conn.commit()
        return "Compte mis à jour avec succès."
    except Exception as e:
        return f"Erreur lors de la mise à jour du compte : {str(e)}"


def delete_user(user_id):
    try:
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        return "Compte supprimé avec succès."
    except Exception as e:
        return f"Erreur lors de la suppression du compte : {str(e)}"
def change_password(user_id, current_password, new_password):
    cursor.execute('SELECT password FROM users WHERE id = ?', (user_id,))
    row = cursor.fetchone()
    if not row or not verify_password(current_password, row[0]):
        return "Mot de passe actuel incorrect."

    hashed_new_password = hash_password(new_password)
    cursor.execute('''
        UPDATE users
        SET password = ?
        WHERE id = ?
    ''', (hashed_new_password, user_id))
    conn.commit()
    return "Mot de passe mis à jour avec succès."


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password, hashed_password):
    return hash_password(plain_password) == hashed_password
