from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from auth.loginPage import LoginPage
from frontPage import MySideBar
import sys
from data.database import initialize_db
from data.auth import initialize_users
from data.config_centre import initialize_centre

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialiser la base de données
        initialize_db()
        initialize_users()
        #initialize_centre()
        
        self.login_page = LoginPage(self)
        if self.login_page.exec() == QDialog.Accepted:
            user_role = self.login_page.get_user_role()  # Obtenir le rôle de l'utilisateur
            self.show_main_window(user_role)

    def show_main_window(self, user_role):
        self.my_sidebar = MySideBar(user_role)  # Passer le rôle de l'utilisateur
        self.setCentralWidget(self.my_sidebar)
        self.setWindowTitle("ZANISCHOOL")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
