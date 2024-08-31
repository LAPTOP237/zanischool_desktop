from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sqlite3

from data.compte_management import hash_password

db = 'zani_db.db'

class LoginPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Connexion à Mon Compagnon Scolaire')
        self.setFixedSize(500, 300)  # Augmenter la taille pour accueillir le logo et le formulaire
        
        # Logo et message de bienvenue
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('icons/logo_mc.png').scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(self.logo_pixmap)
        
        self.welcome_label = QLabel('Heureux de vous revoir!', self)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000;padding:0px; margin:0px")
        self.welcome_label.setFixedWidth(250)  # Ajuster la largeur
        self.welcome_label.setFixedHeight(50)  # Ajuster la hauteur
        
        # Formulaire de connexion
        self.username_lineEdit = QLineEdit(self)
        self.username_lineEdit.setPlaceholderText('Nom d\'utilisateur')
        self.username_lineEdit.setFixedWidth(250)  # Ajuster la largeur
        self.username_lineEdit.setFixedHeight(30)  # Ajuster la hauteur
        self.username_lineEdit.setStyleSheet("""
            QLineEdit {
                font-weight: bold;
                padding: 0px;  /* Espace interne autour du texte */
                margin: 0px;    /* Marge autour du bouton */
                border: 1px solid rgb(61, 48, 162);
                border-radius: 5px;
            }
        """)

        self.password_lineEdit = QLineEdit(self)
        self.password_lineEdit.setPlaceholderText('Mot de passe')
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setFixedWidth(250)  # Ajuster la largeur
        self.password_lineEdit.setFixedHeight(30)  # Ajuster la hauteur
        self.password_lineEdit.setStyleSheet("""
            QLineEdit {
                font-weight: bold;
                padding: 0px;  /* Espace interne autour du texte */
                margin: 0px;    /* Marge autour du bouton */
                border: 1px solid rgb(61, 48, 162);
                border-radius: 5px;
            }
        """)
        
        self.login_button = QPushButton('Se connecter', self)
        self.login_button.clicked.connect(self.check_credentials)
        self.login_button.setFixedWidth(250)  # Ajuster la largeur
        self.login_button.setFixedHeight(35)  # Ajuster la hauteur

        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(61, 48, 162);
                color: white;
                font-weight: bold;
                padding: 0px;  /* Espace interne autour du texte */
                margin: 0px;    /* Marge autour du bouton */
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgb(30, 22, 88);
            }
            QPushButton:pressed {
                background-color: rgb(30, 22, 88);
            }
        """)
        
        # Layouts pour l'organisation des widgets
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.logo_label)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.welcome_label)
        form_layout.addWidget(self.username_lineEdit)
        form_layout.addWidget(self.password_lineEdit)
        form_layout.addWidget(self.login_button)
        
        right_widget = QWidget()
        right_widget.setLayout(form_layout)
        right_widget.setStyleSheet("padding: 20px; background-color: #f5f5f5; border-radius: 10px;")
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(right_widget)
        
        self.setLayout(main_layout)
        self.user_role = None  # Attribut pour stocker le rôle de l'utilisateur

    def check_credentials(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        hashed_password = hash_password(password)
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT role,id,titulaire,username FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            self.user_role = result[0]
            self.user_id = result[1]
            self.user_titulaire = result[2]
            self.user_name = result[3]  # Stocker le rôle de l'utilisateur
            self.accept()  # Connexion réussie, fermer le dialogue
        else:
            QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def get_user_role(self):
        return self.user_role  # Méthode pour obtenir le rôle de l'utilisateur
    
    def get_user_id(self):
        return self.user_id
    
    def get_user_name(self):
        return self.user_name

