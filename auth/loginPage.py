from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import Qt
import sqlite3

db = 'zani_db.db'
class LoginPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Connexion')
        self.setFixedSize(300, 150)
        
        self.username_lineEdit = QLineEdit(self)
        self.username_lineEdit.setPlaceholderText('Nom d\'utilisateur')
        
        self.password_lineEdit = QLineEdit(self)
        self.password_lineEdit.setPlaceholderText('Mot de passe')
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton('Se connecter', self)
        self.login_button.clicked.connect(self.check_credentials)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Nom d\'utilisateur:'))
        self.layout.addWidget(self.username_lineEdit)
        self.layout.addWidget(QLabel('Mot de passe:'))
        self.layout.addWidget(self.password_lineEdit)
        self.layout.addWidget(self.login_button)
        self.setLayout(self.layout)
        
        self.user_role = None  # Attribut pour stocker le rôle de l'utilisateur

    def check_credentials(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        
        conn = sqlite3.connect('db')
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            self.user_role = result[0]  # Stocker le rôle de l'utilisateur
            self.accept()  # Connexion réussie, fermer le dialogue
        else:
            QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def get_user_role(self):
        return self.user_role  # Méthode pour obtenir le rôle de l'utilisateur
