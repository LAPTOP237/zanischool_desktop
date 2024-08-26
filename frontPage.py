from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QMainWindow, QHBoxLayout,QMenu,QMessageBox
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from StudentPage import StudentPage
from StudentPayePage import StudentPayePage
from ui_index import Ui_MainWindow
from data.exportManager import ExportManager

from data.student_management import get_all_students, delete_student, search_students, filter_students, initialize_db,get_student_by_matricule
from updateStudentPages import StudentUpdatePage

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self,user_role):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ZANISCHOOL")
        self.user_role = user_role

        initialize_db()  # Initialiser la base de données au lancement
        self.load_students() # Chargement de la liste des etudiants
        # Configurez votre interface utilisateur ici
        
        # Redimensionner les colonnes en fonction de leur contenu
        self.tableWidget.resizeColumnsToContents()
        
        # Configurer les barres de défilement
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        #Cacher le Widget Menu
        self.icon_only_widget.setHidden(True)

        #Ccher les Dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)

        #Connecter nos differents boutons aux fonctions pour switcher entre les pages
        self.dashboard1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard2.clicked.connect(self.switch_to_dashboard_page)

        self.institute1.clicked.connect(self.switch_to_institute_page)
        self.institute2.clicked.connect(self.switch_to_institute_page)

        self.students_info.clicked.connect(self.switch_to_students_info_page)
        self.students_payement.clicked.connect(self.switch_to_students_payements_page)
        self.students_transactions.clicked.connect(self.switch_to_students_transactions_page)

        self.teachers_info.clicked.connect(self.switch_to_teachers_info_page)
        self.teachers_salaries.clicked.connect(self.switch_to_teachers_salaries_page)
        self.teachers_transactions.clicked.connect(self.switch_to_teachers_transactions_page)

        self.budgets.clicked.connect(self.switch_to_budgets_page)
        self.expenses.clicked.connect(self.switch_to_expenses_page)
        self.business_overview.clicked.connect(self.switch_to_business_overview_page)

        self.settings1.clicked.connect(self.switch_to_settings_page)
        self.settings2.clicked.connect(self.switch_to_settings_page)

        #Connecter les buttons a mon context menu 
        self.students1.clicked.connect(self.students_context_menu)
        self.teachers1.clicked.connect(self.teachers_context_menu)
        self.finances1.clicked.connect(self.finances_context_menu)

        # Connecter le bouton à la méthode pour ouvrir le formulaire d'ajout de l'apprenant
        self.addStudentBtn.clicked.connect(self.open_student_dialog)

        self.addPayeOldStudentBtn.clicked.connect(self.open_student_payement_dialog)

        #connecter mes buttons pour les filtre
        self.filterGender_comboBox.currentIndexChanged.connect(self.apply_filters)
        self.filterClass_comboBox.currentIndexChanged.connect(self.apply_filters)
        self.searchStudent_lineEdit.textChanged.connect(self.apply_search)

        # Configuration des boutons pour exportations
        self.exportPDF_btn.clicked.connect(self.on_export_pdf)
        self.exportExcel_btn.clicked.connect(self.on_export_excel)
        self.export_manager = ExportManager(self)
        

    #Methodes pour switcher entres les pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institute_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_students_info_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_students_payements_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_students_transactions_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teachers_info_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teachers_salaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teachers_transactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budgets_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_business_overview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    #Methodes pour afficher la context menu de sidebar icon_only
    def students_context_menu(self):
        self.show_custom_context_menu(self.students1,["Informations Apprenants","Paiements Apprenants","Transactions Apprenants"])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.students1,["Informations Enseignants","Salaires Enseignants","Transactions Enseignants"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.students1,["Budgets","Depenses","Stats"])


    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        #Definir le style de la context_menu
        menu.setStyleSheet("""
                        QMenu{
                           background-color:black;
                           color: white;
                           }
                        QMenu:selected{
                            background-color:white;
                           color:#3D30A2;
                           }
                        """)
        
        #Ajouter les actions au menu
        for item_text in menu_items:
            action = QAction(item_text,self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        #Afficher le menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()


    def handle_menu_item_click(self):

        text = self.sender().text()

        if text == "Informations Apprenants":
            self.switch_to_students_info_page()
        elif text == "Paiements Apprenants":
            self.switch_to_students_payements_page()
        elif text == "Transactions Apprenants":
            self.switch_to_students_transactions_page()
        elif text == "Informations Enseignants":
            self.switch_to_teachers_info_page()
        elif text == "Transactions Enseignants":
            self.switch_to_teachers_transactions_page()
        elif text == "Salaires Enseignants":
            self.switch_to_teachers_salaries_page()
        elif text == "Budgets":
            self.switch_to_budgets_page()
        elif text == "Depenses":
            self.switch_to_expenses_page()
        elif text == "Stats":
            self.switch_to_business_overview_page()
    
### Gerer la listes des apprenants

    def load_students(self):
        # Charge les données des étudiants dans le tableau
        students = get_all_students()
        self.tableWidget.setRowCount(0)
        for row_index, row in enumerate(students):
            self.tableWidget.insertRow(row_index)
            for col_index, item in enumerate(row[1:]):  # Exclure la colonne matricule pour l'instant
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(item)))
              # Ajouter des boutons d'action stylisés   
            self.add_actions_buttons(row_index)
            
            
    def add_actions_buttons(self,row_index):
        # Ajouter des boutons d'action stylisés
            edit_button = QPushButton()
            delete_button = QPushButton()
            
            # Configurer les icônes et styles des boutons
            edit_button.setIcon(QIcon("icons/icons8-edit-50.png"))
            edit_button.setStyleSheet("background-color: #0077BD; border-radius: 5px; color: white;margin-bottom:6px;")
            edit_button.setFixedSize(25, 25)
            delete_button.setIcon(QIcon("icons/icons8-delete-50.png"))
            delete_button.setStyleSheet("background-color: #FF4C4C; border-radius: 5px; color: white;margin-bottom:6px;")
            delete_button.setFixedSize(25, 25)
            
            edit_button.clicked.connect(lambda checked, r=row_index: self.edit_student(r))
            delete_button.clicked.connect(lambda checked, r=row_index: self.confirm_delete(r))
            
            # Ajouter les boutons côte à côte dans la colonne Actions
            button_layout = QHBoxLayout()
            button_layout.addWidget(edit_button)
            button_layout.addWidget(delete_button)
            
            # Créer un widget pour contenir les boutons
            button_widget = QWidget()
            button_widget.setLayout(button_layout)
            
            self.tableWidget.setCellWidget(row_index, 9, button_widget)

            # Désactiver les boutons de suppression et de modification pour les utilisateurs normaux
            if self.user_role != 'admin':
               # delete_button.setEnabled(False)
               # edit_button.setEnabled(False)
               pass
        

    def open_student_dialog(self):
        # Ouvrir la boîte de dialogue pour ajouter un nouvel étudiant
        dialog = StudentPage()
        if dialog.exec():
            self.load_students()  # Recharger les données après ajout

    def open_student_payement_dialog(self):
        # Ouvrir la boîte de dialogue pour ajouter un nouvel étudiant
        dialog = StudentPayePage()
        if dialog.exec():
            self.load_students()  # Recharger les données après ajout

    def edit_student(self, row_index):
        if self.user_role == 'admin':
            matricule = self.tableWidget.item(row_index, 0).text()
            # Récupérer les données de l'étudiant à partir de l'index de la ligne
            student_data = self.get_student_data(matricule)
            
            # Ouvrir la boîte de dialogue pour modifier les informations de l'étudiant
            dialog = StudentUpdatePage(self)
            
            # Charger les données de l'étudiant dans le formulaire
            dialog.load_student_data(student_data)
            
            if dialog.exec():
                self.load_students()  # Recharger les données après la modification
        else:
            QMessageBox.warning(self, "Erreur", "Vous n'avez pas les droits nécessaires pour la modification.")

    def get_student_data(self, matricule):
        return get_student_by_matricule(matricule)

    def confirm_delete(self, row_index):
        if self.user_role == 'admin':
            matricule = self.tableWidget.item(row_index, 0).text()  # Supposons que la première colonne est le matricule

            # Créer la boîte de dialogue de confirmation
            reply = QMessageBox.question(self, 'Confirmation', f"Êtes-vous sûr de vouloir supprimer l'apprenant avec le matricule {matricule} ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.delete_student(row_index)
        else:
            QMessageBox.warning(self, "Erreur", "Vous n'avez pas les droits nécessaires pour la suppression.")

    def delete_student(self, row_index):
        
        # Supprimer un étudiant de la base de données et mettre à jour le tableau
        matricule = self.tableWidget.item(row_index, 0).text()
        delete_student(matricule)
        self.load_students()
        

    def apply_filters(self):
        
        # Appliquer les filtres en fonction du sexe et de la classe
        gender_filter = self.filterGender_comboBox.currentText()
        class_filter = self.filterClass_comboBox.currentText()

        # Vérifier si les valeurs par défaut sont sélectionnées
        if gender_filter == "Selectionner le sexe":
            gender_filter = None
        if class_filter == "Selectionner la classe":
            class_filter = None
        
        students = filter_students(gender_filter, class_filter)
        self.tableWidget.setRowCount(0)
        for row_index, row in enumerate(students):
            self.tableWidget.insertRow(row_index)
            for col_index, item in enumerate(row[1:]):  # Exclure la colonne matricule pour l'instant
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(item)))
            
            # Ajouter des boutons d'action stylisés   
            self.add_actions_buttons(row_index)

    def apply_search(self):
        # Appliquer la recherche en temps réel sur le tableau
        search_text = self.searchStudent_lineEdit.text()
        
        students = search_students(search_text)
        self.tableWidget.setRowCount(0)
        for row_index, row in enumerate(students):
            self.tableWidget.insertRow(row_index)
            for col_index, item in enumerate(row[1:]):  # Exclure la colonne matricule pour l'instant
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(item)))
            
           # Ajouter des boutons d'action stylisés   
            self.add_actions_buttons(row_index)
### fin Gerer la listers des apprenants

##Exportation du table etudiant
    def on_export_pdf(self):
        """Handler pour le bouton d'exportation en PDF."""
        students_data = self.get_table_data()
        self.export_manager.export_to_pdf(students_data)

    def on_export_excel(self):
        """Handler pour le bouton d'exportation en Excel."""
        students_data = self.get_table_data()
        self.export_manager.export_to_excel(students_data)

    def get_table_data(self):
        """Récupère les données du QTableWidget."""
        data = []
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()

        for row in range(rows):
            row_data = {}
            for col in range(columns):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    row_data[self.tableWidget.horizontalHeaderItem(col).text()] = item.text()
            data.append(row_data)

        return data
##Fin Exportation du table etudiant
