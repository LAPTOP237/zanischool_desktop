# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentPayeDialog.ui'
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
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(QDialog):
    def setupUi(self, StudentPayeDialog):
        if not StudentPayeDialog.objectName():
            StudentPayeDialog.setObjectName(u"StudentPayeDialog")
        self.resize(547, 584)
        icon = QIcon()
        icon.addFile(u":/icons/logo_mc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
"QDoubleSpinBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
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
"font-size:15px;\n"
"}\n"
"\n"
"")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(310, 530, 221, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.savePayementBtn = QPushButton(self.layoutWidget_2)
        self.savePayementBtn.setObjectName(u"savePayementBtn")
        self.savePayementBtn.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setBold(True)
        self.savePayementBtn.setFont(font)
        self.savePayementBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.savePayementBtn)

        self.paye_cancel_btn = QPushButton(self.layoutWidget_2)
        self.paye_cancel_btn.setObjectName(u"paye_cancel_btn")
        self.paye_cancel_btn.setMinimumSize(QSize(0, 35))
        self.paye_cancel_btn.setFont(font)
        self.paye_cancel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.paye_cancel_btn)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 331, 31))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Black"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(61, 48, 162);")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 61, 521, 461))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.name_searchlineEdit = QLineEdit(self.widget)
        self.name_searchlineEdit.setObjectName(u"name_searchlineEdit")
        self.name_searchlineEdit.setFont(font)

        self.verticalLayout_7.addWidget(self.name_searchlineEdit)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.paye_matricule_lineEdit = QLineEdit(self.widget)
        self.paye_matricule_lineEdit.setObjectName(u"paye_matricule_lineEdit")
        self.paye_matricule_lineEdit.setMinimumSize(QSize(0, 35))
        self.paye_matricule_lineEdit.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setFamilies([u"Montserrat SemiBold"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(True)
        self.paye_matricule_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.paye_matricule_lineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.verticalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.paye_amount_doubleSpinBox = QDoubleSpinBox(self.widget)
        self.paye_amount_doubleSpinBox.setObjectName(u"paye_amount_doubleSpinBox")
        self.paye_amount_doubleSpinBox.setWrapping(False)

        self.verticalLayout_3.addWidget(self.paye_amount_doubleSpinBox)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6)

        self.paye_date_dateEdit = QDateEdit(self.widget)
        self.paye_date_dateEdit.setObjectName(u"paye_date_dateEdit")
        self.paye_date_dateEdit.setFont(font)
        self.paye_date_dateEdit.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.paye_date_dateEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.paye_annee_comboBox = QComboBox(self.widget)
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.addItem("")
        self.paye_annee_comboBox.setObjectName(u"paye_annee_comboBox")
        font4 = QFont()
        self.paye_annee_comboBox.setFont(font4)

        self.verticalLayout_5.addWidget(self.paye_annee_comboBox)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Gestions de Apprenants", None))
        self.savePayementBtn.setText(QCoreApplication.translate("Dialog", u"Enregistrer", None))
        self.paye_cancel_btn.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nouveau Paiement", None))
        self.name_searchlineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Entrez le nom ici pour rechercher automatiquement le matricule", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Matricule", None))
        self.paye_matricule_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Entrez le matricule de l'apprenant", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Raison", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Inscription", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Premiere Tranche", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Deuxieme Tranche", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Montant vers\u00e9", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Date de paiement", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Annee Scolaire", None))
        self.paye_annee_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"2024 - 2025", None))
        self.paye_annee_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"2023 -2024", None))
        self.paye_annee_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"2022-2023", None))
        self.paye_annee_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"2021-2022", None))
        self.paye_annee_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"2020-2021", None))
        self.paye_annee_comboBox.setItemText(5, "")
        self.paye_annee_comboBox.setItemText(6, "")

    # retranslateUi

