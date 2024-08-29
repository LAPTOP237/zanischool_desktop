import sqlite3

db = 'zani_db.db'

def get_all_payments():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT recu.id_recu,students.matricule,students.nom, students.prenom,students.sexe,students.option_et_niveau,recu.raison,recu.montant_verse,recu.date_paye,recu.solde,recu.montant_restant FROM recu
        JOIN dossier ON recu.id_dossier = dossier.id_dossier
        JOIN students ON dossier.id_eleve = students.matricule
    ''')
    payments = cursor.fetchall()
    
    conn.close()
    return payments

def filter_payments(gender=None, class_option=None, date=None):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    query = '''
        SELECT recu.id_recu, students.matricule, students.nom, students.prenom, students.sexe,
               students.option_et_niveau, recu.raison, recu.montant_verse, recu.date_paye,
               recu.solde, recu.montant_restant
        FROM recu
        JOIN dossier ON recu.id_dossier = dossier.id_dossier
        JOIN students ON dossier.id_eleve = students.matricule
        WHERE 1=1
    '''
    params = []
    
    if gender:
        query += ' AND students.sexe = ?'
        params.append(gender)
    if class_option:
        query += ' AND students.option_et_niveau = ?'
        params.append(class_option)
    if date:
        query += ' AND recu.date_paye = ?'
        params.append(date)
    
    cursor.execute(query, params)
    payments = cursor.fetchall()
    
    conn.close()
    return payments


def search_payments(keyword):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    query = '''
        SELECT recu.id_recu,students.matricule,students.nom, students.prenom,students.sexe,students.option_et_niveau,recu.raison,recu.montant_verse,recu.date_paye,recu.solde,recu.montant_restant FROM recu
        JOIN dossier ON recu.id_dossier = dossier.id_dossier
        JOIN students ON dossier.id_eleve = students.matricule
        WHERE recu.raison LIKE ? OR recu.montant_verse LIKE ? OR recu.solde LIKE ?
    '''
    search_term = f'%{keyword}%'
    cursor.execute(query, (search_term, search_term, search_term))
    payments = cursor.fetchall()
    
    conn.close()
    return payments

def get_payment_by_matricule(matricule):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    query = '''
        SELECT recu.id_recu,students.matricule,students.nom, students.prenom,students.sexe,students.option_et_niveau,recu.raison,recu.montant_verse,recu.date_paye,recu.solde,recu.montant_restant FROM recu
        JOIN dossier ON recu.id_dossier = dossier.id_dossier
        JOIN students ON dossier.id_eleve = students.matricule
        WHERE students.matricule = ?
    '''
    cursor.execute(query, (matricule,))
    payment = cursor.fetchall()
    
    conn.close()
    return payment

def delete_payment(payment_id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    query = 'DELETE FROM recu WHERE id_recu = ?'
    cursor.execute(query, (payment_id,))
    
    conn.commit()
    conn.close()