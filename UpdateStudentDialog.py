# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateStudentDialog.ui'
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

class Ui_UpdateStudent_Dialog(QDialog):
    def setupUi(self, UpdateStudent_Dialog):
        if not UpdateStudent_Dialog.objectName():
            UpdateStudent_Dialog.setObjectName(u"UpdateStudent_Dialog")
        UpdateStudent_Dialog.resize(548, 584)
        icon = QIcon()
        icon.addFile(u":/icons/logo_zanischool.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        UpdateStudent_Dialog.setWindowIcon(icon)
        self.layoutWidget = QWidget(UpdateStudent_Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 530, 221, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.updateStudentBtn = QPushButton(self.layoutWidget)
        self.updateStudentBtn.setObjectName(u"updateStudentBtn")
        self.updateStudentBtn.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setBold(True)
        self.updateStudentBtn.setFont(font)
        self.updateStudentBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.updateStudentBtn)

        self.update_cancel_btn = QPushButton(self.layoutWidget)
        self.update_cancel_btn.setObjectName(u"update_cancel_btn")
        self.update_cancel_btn.setMinimumSize(QSize(0, 35))
        self.update_cancel_btn.setFont(font)
        self.update_cancel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_cancel_btn)

        self.layoutWidget_2 = QWidget(UpdateStudent_Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 70, 511, 455))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.update_name_lineEdit = QLineEdit(self.layoutWidget_2)
        self.update_name_lineEdit.setObjectName(u"update_name_lineEdit")
        self.update_name_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_name_lineEdit.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Montserrat SemiBold"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(True)
        self.update_name_lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.update_name_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.update_name_lineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.update_name_lineEdit_2.setObjectName(u"update_name_lineEdit_2")
        self.update_name_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.update_name_lineEdit_2.setMaximumSize(QSize(16777215, 35))
        self.update_name_lineEdit_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.update_name_lineEdit_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.update_gender_comboBox = QComboBox(self.layoutWidget_2)
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.setObjectName(u"update_gender_comboBox")
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setItalic(True)
        self.update_gender_comboBox.setFont(font3)

        self.verticalLayout_3.addWidget(self.update_gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.update_class_comboBox_2 = QComboBox(self.layoutWidget_2)
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.setObjectName(u"update_class_comboBox_2")
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setBold(True)
        font4.setItalic(True)
        self.update_class_comboBox_2.setFont(font4)

        self.verticalLayout_4.addWidget(self.update_class_comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.update_dateNaiss_dateEdit = QDateEdit(self.layoutWidget_2)
        self.update_dateNaiss_dateEdit.setObjectName(u"update_dateNaiss_dateEdit")
        self.update_dateNaiss_dateEdit.setFont(font3)

        self.verticalLayout_5.addWidget(self.update_dateNaiss_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.update_lieuNaiss_lineEdit = QLineEdit(self.layoutWidget_2)
        self.update_lieuNaiss_lineEdit.setObjectName(u"update_lieuNaiss_lineEdit")
        self.update_lieuNaiss_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_lieuNaiss_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_lieuNaiss_lineEdit.setFont(font2)

        self.verticalLayout_6.addWidget(self.update_lieuNaiss_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_email_lineEdit = QLineEdit(self.layoutWidget_2)
        self.update_email_lineEdit.setObjectName(u"update_email_lineEdit")
        self.update_email_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_email_lineEdit.setFont(font2)

        self.verticalLayout_7.addWidget(self.update_email_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.update_contact_lineEdit = QLineEdit(self.layoutWidget_2)
        self.update_contact_lineEdit.setObjectName(u"update_contact_lineEdit")
        self.update_contact_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_contact_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_contact_lineEdit.setFont(font2)

        self.verticalLayout_8.addWidget(self.update_contact_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.line = QFrame(UpdateStudent_Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(UpdateStudent_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 331, 31))
        font5 = QFont()
        font5.setFamilies([u"Montserrat Black"])
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setItalic(True)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(61, 48, 162);")

        self.retranslateUi(UpdateStudent_Dialog)

        QMetaObject.connectSlotsByName(UpdateStudent_Dialog)
    # setupUi

    def retranslateUi(self, UpdateStudent_Dialog):
        UpdateStudent_Dialog.setWindowTitle(QCoreApplication.translate("UpdateStudent_Dialog", u"Gestions de Apprenants", None))
        self.updateStudentBtn.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Enregistrer", None))
        self.update_cancel_btn.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Annuler", None))
        self.label_2.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Nom", None))
        self.label_3.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Pr\u00e9noms", None))
        self.label_4.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Sexe", None))
        self.update_gender_comboBox.setItemText(0, QCoreApplication.translate("UpdateStudent_Dialog", u"F\u00e9minin", None))
        self.update_gender_comboBox.setItemText(1, QCoreApplication.translate("UpdateStudent_Dialog", u"Masculin", None))

        self.label_5.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Option et Niveau", None))
        self.update_class_comboBox_2.setItemText(0, QCoreApplication.translate("UpdateStudent_Dialog", u"ESCO 1", None))
        self.update_class_comboBox_2.setItemText(1, QCoreApplication.translate("UpdateStudent_Dialog", u"ESCO 2", None))
        self.update_class_comboBox_2.setItemText(2, QCoreApplication.translate("UpdateStudent_Dialog", u"ATELIER 1", None))
        self.update_class_comboBox_2.setItemText(3, QCoreApplication.translate("UpdateStudent_Dialog", u"ATELIER 2", None))
        self.update_class_comboBox_2.setItemText(4, QCoreApplication.translate("UpdateStudent_Dialog", u"COME 1", None))
        self.update_class_comboBox_2.setItemText(5, QCoreApplication.translate("UpdateStudent_Dialog", u"COME 2", None))
        self.update_class_comboBox_2.setItemText(6, QCoreApplication.translate("UpdateStudent_Dialog", u"COME 3", None))

        self.label_6.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Date de naissance", None))
        self.label_7.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Lieu de naissance", None))
        self.label_8.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Email", None))
        self.label_9.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Contact", None))
        self.label.setText(QCoreApplication.translate("UpdateStudent_Dialog", u"Mise \u00e0 jour Apprenant", None))
    # retranslateUi

