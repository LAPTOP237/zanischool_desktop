from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from auth.LoginPage import LoginPage
from data.config_centre import initialize_centre
from frontPage import MySideBar
from LoadingPage import LoadingDialog  # Importez la boîte de dialogue de chargement
from PySide6.QtCore import QTimer
import sys
from data.database import initialize_db
from data.auth import initialize_users

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Créer la boîte de dialogue de chargement
        loading_dialog = LoadingDialog(self)
        loading_dialog.start_loading()

        try:
            # Initialiser la base de données
            #initialize_db()
            initialize_users()
            initialize_centre()
        finally:
            # Assurez-vous de fermer la boîte de dialogue même en cas d'erreur
            loading_dialog.stop_loading()
        
        self.login_page = LoginPage(self)
        if self.login_page.exec() == QDialog.Accepted:
            user_role = self.login_page.get_user_role()  # Obtenir le rôle de l'utilisateur
            user_name = self.login_page.get_user_name()
            user_id = self.login_page.get_user_id()
            self.show_main_window(user_role,user_name,user_id)

    def show_main_window(self, user_role,user_name,user_id):
        self.my_sidebar = MySideBar(user_role,user_name,user_id)  # Passer le rôle de l'utilisateur
        self.setCentralWidget(self.my_sidebar)
        self.setWindowTitle("Mon Compagnon Scolaire")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Créer la fenêtre principale
    window = MainWindow()
    window.show()

    # Lancer l'application
    sys.exit(app.exec())