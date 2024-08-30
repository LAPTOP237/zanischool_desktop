# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CompteDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CompteDial(QDialog):
    def setupUi(self, CompteDial):
        if not CompteDial.objectName():
            CompteDial.setObjectName(u"CompteDial")

        self.resize(548, 584)
        icon = QIcon()
        icon.addFile(u":/icons/logo_mc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 331, 31))
        font = QFont()
        font.setFamilies([u"Montserrat Black"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(61, 48, 162);")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 78, 497, 25))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(270, 520, 261, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveCompteBtn = QPushButton(self.layoutWidget)
        self.saveCompteBtn.setObjectName(u"saveCompteBtn")
        self.saveCompteBtn.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setBold(True)
        self.saveCompteBtn.setFont(font2)
        self.saveCompteBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout.addWidget(self.saveCompteBtn)

        self.compte_concel_btn = QPushButton(self.layoutWidget)
        self.compte_concel_btn.setObjectName(u"compte_concel_btn")
        self.compte_concel_btn.setMinimumSize(QSize(0, 35))
        self.compte_concel_btn.setFont(font2)
        self.compte_concel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout.addWidget(self.compte_concel_btn)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 110, 501, 361))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titulaire_lineEdit = QLineEdit(self.widget)
        self.titulaire_lineEdit.setObjectName(u"titulaire_lineEdit")
        self.titulaire_lineEdit.setMinimumSize(QSize(0, 35))
        self.titulaire_lineEdit.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setFamilies([u"Montserrat SemiBold"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(True)
        self.titulaire_lineEdit.setFont(font3)

        self.verticalLayout_3.addWidget(self.titulaire_lineEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.name_user_lineEdit = QLineEdit(self.widget)
        self.name_user_lineEdit.setObjectName(u"name_user_lineEdit")
        self.name_user_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_user_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.name_user_lineEdit.setFont(font3)

        self.verticalLayout_2.addWidget(self.name_user_lineEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout.addWidget(self.label_7)

        self.role_comboBox = QComboBox(self.widget)
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.role_comboBox.setObjectName(u"role_comboBox")
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setBold(True)
        font4.setItalic(True)
        self.role_comboBox.setFont(font4)

        self.verticalLayout.addWidget(self.role_comboBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.password_lineEdit = QLineEdit(self.widget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 35))
        self.password_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.password_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.password_lineEdit)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_6)

        self.confirm_password_lineEdit = QLineEdit(self.widget)
        self.confirm_password_lineEdit.setObjectName(u"confirm_password_lineEdit")
        self.confirm_password_lineEdit.setMinimumSize(QSize(0, 35))
        self.confirm_password_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.confirm_password_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.confirm_password_lineEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("CompteDial", u"Gestion des comptes", None))
        self.label.setText(QCoreApplication.translate("CompteDial", u"Creation de compte", None))
        self.label_3.setText(QCoreApplication.translate("CompteDial", u"Titulaire du compte", None))
        self.saveCompteBtn.setText(QCoreApplication.translate("CompteDial", u"Enregistrer", None))
        self.compte_concel_btn.setText(QCoreApplication.translate("CompteDial", u"Annuler", None))
        self.label_4.setText(QCoreApplication.translate("CompteDial", u"Nom d'utilisateur", None))
        self.label_7.setText(QCoreApplication.translate("CompteDial", u"Role", None))
        self.role_comboBox.setItemText(0, QCoreApplication.translate("CompteDial", u"user", None))
        self.role_comboBox.setItemText(1, QCoreApplication.translate("CompteDial", u"admin", None))

        self.label_5.setText(QCoreApplication.translate("CompteDial", u"Mot de passe", None))
        self.label_6.setText(QCoreApplication.translate("CompteDial", u"Confirmer le mot de passe", None))
    # retranslateUi

