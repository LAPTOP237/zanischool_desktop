# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_StudentDialog(QDialog):
    def setupUi(self, StudentDialog):
        if not StudentDialog.objectName():
            StudentDialog.setObjectName(u"StudentDialog")

        
        self.resize(548, 584)
        icon = QIcon()
        icon.addFile(u":/icons/logo_zanischool.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(u"QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: rgb(61, 48, 162);\n"
"}\n"
"\n"
"QComboBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: rgb(61, 48, 162);\n"
"selection-background-color: rgb(176, 94, 255);\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 251, 31))
        font = QFont()
        font.setFamilies([u"Montserrat Black"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(61, 48, 162);")
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 511, 455))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Montserrat SemiBold"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(True)
        self.name_lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.name_lineEdit_2 = QLineEdit(self.layoutWidget)
        self.name_lineEdit_2.setObjectName(u"name_lineEdit_2")
        self.name_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.name_lineEdit_2.setMaximumSize(QSize(16777215, 35))
        self.name_lineEdit_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.name_lineEdit_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setItalic(True)
        self.gender_comboBox.setFont(font3)

        self.verticalLayout_3.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.class_comboBox_2 = QComboBox(self.layoutWidget)
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.setObjectName(u"class_comboBox_2")
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setBold(True)
        font4.setItalic(True)
        self.class_comboBox_2.setFont(font4)

        self.verticalLayout_4.addWidget(self.class_comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.dateNaiss_dateEdit = QDateEdit(self.layoutWidget)
        self.dateNaiss_dateEdit.setObjectName(u"dateNaiss_dateEdit")
        self.dateNaiss_dateEdit.setFont(font3)

        self.verticalLayout_5.addWidget(self.dateNaiss_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.lieuNaiss_lineEdit = QLineEdit(self.layoutWidget)
        self.lieuNaiss_lineEdit.setObjectName(u"lieuNaiss_lineEdit")
        self.lieuNaiss_lineEdit.setMinimumSize(QSize(0, 35))
        self.lieuNaiss_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lieuNaiss_lineEdit.setFont(font2)

        self.verticalLayout_6.addWidget(self.lieuNaiss_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.email_lineEdit = QLineEdit(self.layoutWidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.email_lineEdit.setFont(font2)

        self.verticalLayout_7.addWidget(self.email_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.contact_lineEdit = QLineEdit(self.layoutWidget)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        self.contact_lineEdit.setMinimumSize(QSize(0, 35))
        self.contact_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.contact_lineEdit.setFont(font2)

        self.verticalLayout_8.addWidget(self.contact_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 530, 221, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudentBtn = QPushButton(self.layoutWidget1)
        self.saveStudentBtn.setObjectName(u"saveStudentBtn")
        self.saveStudentBtn.setMinimumSize(QSize(0, 35))
        font5 = QFont()
        font5.setBold(True)
        self.saveStudentBtn.setFont(font5)
        self.saveStudentBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveStudentBtn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 35))
        self.cancel_btn.setFont(font5)
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("StudentDialog", u"Gestion de Apprenants", None))
        self.label.setText(QCoreApplication.translate("StudentDialog", u"Nouvel Apprenant", None))
        self.label_2.setText(QCoreApplication.translate("StudentDialog", u"Nom", None))
        self.label_3.setText(QCoreApplication.translate("StudentDialog", u"Pr\u00e9noms", None))
        self.label_4.setText(QCoreApplication.translate("StudentDialog", u"Sexe", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentDialog", u"F\u00e9minin", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentDialog", u"Masculin", None))

        self.label_5.setText(QCoreApplication.translate("StudentDialog", u"Option et Niveau", None))
        # self.class_comboBox_2.setItemText(0, QCoreApplication.translate("StudentDialog", u"ESCO 1", None))
        # self.class_comboBox_2.setItemText(1, QCoreApplication.translate("StudentDialog", u"ESCO 2", None))
        # self.class_comboBox_2.setItemText(2, QCoreApplication.translate("StudentDialog", u"ATELIER 1", None))
        # self.class_comboBox_2.setItemText(3, QCoreApplication.translate("StudentDialog", u"ATELIER 2", None))
        # self.class_comboBox_2.setItemText(4, QCoreApplication.translate("StudentDialog", u"COME 1", None))
        # self.class_comboBox_2.setItemText(5, QCoreApplication.translate("StudentDialog", u"COME 2", None))
        # self.class_comboBox_2.setItemText(6, QCoreApplication.translate("StudentDialog", u"COME 3", None))

        self.label_6.setText(QCoreApplication.translate("StudentDialog", u"Date de naissance", None))
        self.label_7.setText(QCoreApplication.translate("StudentDialog", u"Lieu de naissance", None))
        self.label_8.setText(QCoreApplication.translate("StudentDialog", u"Email", None))
        self.label_9.setText(QCoreApplication.translate("StudentDialog", u"Contact", None))
        self.saveStudentBtn.setText(QCoreApplication.translate("StudentDialog", u"Enregistrer", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentDialog", u"Annuler", None))
    # retranslateUi


    # Connecter le bouton cancel_btn pour fermer le formulaire d'ajout d'apprenant
    # self.cancel_btn.clicked.connect(self.reject)

