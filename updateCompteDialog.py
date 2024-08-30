# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateCompteDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_updateCompteDialog(QDialog):
    def setupUi(self, updateCompteDialog):
        if not updateCompteDialog.objectName():
            updateCompteDialog.setObjectName(u"updateCompteDialog")
        self.resize(548, 400)
        icon = QIcon()
        icon.addFile(u":/icons/logo_mc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
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
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 340, 261, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.updatePasswordBtn = QPushButton(self.layoutWidget)
        self.updatePasswordBtn.setObjectName(u"updatePasswordBtn")
        self.updatePasswordBtn.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setBold(True)
        self.updatePasswordBtn.setFont(font1)
        self.updatePasswordBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout.addWidget(self.updatePasswordBtn)

        self.update_pass_concel_btn = QPushButton(self.layoutWidget)
        self.update_pass_concel_btn.setObjectName(u"update_pass_concel_btn")
        self.update_pass_concel_btn.setMinimumSize(QSize(0, 35))
        self.update_pass_concel_btn.setFont(font1)
        self.update_pass_concel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout.addWidget(self.update_pass_concel_btn)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 87, 501, 223))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.update_old_pass_lineEdit = QLineEdit(self.layoutWidget1)
        self.update_old_pass_lineEdit.setObjectName(u"update_old_pass_lineEdit")
        self.update_old_pass_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_old_pass_lineEdit.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setFamilies([u"Montserrat SemiBold"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(True)
        self.update_old_pass_lineEdit.setFont(font3)

        self.verticalLayout_2.addWidget(self.update_old_pass_lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.update_new_pass_lineEdit = QLineEdit(self.layoutWidget1)
        self.update_new_pass_lineEdit.setObjectName(u"update_new_pass_lineEdit")
        self.update_new_pass_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_new_pass_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_new_pass_lineEdit.setFont(font3)

        self.verticalLayout_3.addWidget(self.update_new_pass_lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout.addWidget(self.label_5)

        self.update_confirm_pass_lineEdit = QLineEdit(self.layoutWidget1)
        self.update_confirm_pass_lineEdit.setObjectName(u"update_confirm_pass_lineEdit")
        self.update_confirm_pass_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_confirm_pass_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_confirm_pass_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.update_confirm_pass_lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("updateCompteDialog", u"Mise a jour de compte", None))
        self.label.setText(QCoreApplication.translate("updateCompteDialog", u"Mise \u00e0 jour du Compte", None))
        self.updatePasswordBtn.setText(QCoreApplication.translate("updateCompteDialog", u"Enregistrer", None))
        self.update_pass_concel_btn.setText(QCoreApplication.translate("updateCompteDialog", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("updateCompteDialog", u"Ancien mot de passe", None))
        self.label_4.setText(QCoreApplication.translate("updateCompteDialog", u"Nouveau mot de passe", None))
        self.label_5.setText(QCoreApplication.translate("updateCompteDialog", u"Confirmer mot de passe", None))
    # retranslateUi

