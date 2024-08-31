# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 882)
        icon = QIcon()
        icon.addFile(u":/icons/logo_mc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(81, 0))
        self.icon_only_widget.setMaximumSize(QSize(81, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(61, 48, 162);\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height:30px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 22, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.icon_only_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setPixmap(QPixmap(u":/icons/logo_mc2.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(25)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 25, -1, -1)
        self.dashboard1 = QPushButton(self.icon_only_widget)
        self.dashboard1.setObjectName(u"dashboard1")
        self.dashboard1.setStyleSheet(u"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard1.setIcon(icon1)
        self.dashboard1.setIconSize(QSize(100, 20))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.dashboard1)

        self.institute1 = QPushButton(self.icon_only_widget)
        self.institute1.setObjectName(u"institute1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/institute.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/institute1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institute1.setIcon(icon2)
        self.institute1.setIconSize(QSize(100, 20))
        self.institute1.setCheckable(True)
        self.institute1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.institute1)

        self.students1 = QPushButton(self.icon_only_widget)
        self.students1.setObjectName(u"students1")
        icon3 = QIcon()
        icon3.addFile(u":/icons/students.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/students1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students1.setIcon(icon3)
        self.students1.setIconSize(QSize(100, 20))
        self.students1.setCheckable(True)
        self.students1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.students1)

        self.teachers1 = QPushButton(self.icon_only_widget)
        self.teachers1.setObjectName(u"teachers1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/teacher.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/teacher1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers1.setIcon(icon4)
        self.teachers1.setIconSize(QSize(100, 20))
        self.teachers1.setCheckable(True)
        self.teachers1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.teachers1)

        self.finances1 = QPushButton(self.icon_only_widget)
        self.finances1.setObjectName(u"finances1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/fianances.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/fianances1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances1.setIcon(icon5)
        self.finances1.setIconSize(QSize(100, 20))
        self.finances1.setCheckable(True)
        self.finances1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.finances1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 396, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(25)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.settings1 = QPushButton(self.icon_only_widget)
        self.settings1.setObjectName(u"settings1")
        icon6 = QIcon()
        icon6.addFile(u":/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings1.setIcon(icon6)
        self.settings1.setIconSize(QSize(100, 20))
        self.settings1.setCheckable(True)
        self.settings1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.settings1)

        self.signout1 = QPushButton(self.icon_only_widget)
        self.signout1.setObjectName(u"signout1")
        icon7 = QIcon()
        icon7.addFile(u":/icons/signout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout1.setIcon(icon7)
        self.signout1.setIconSize(QSize(100, 20))
        self.signout1.setCheckable(True)
        self.signout1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.signout1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(255, 0))
        self.icon_text_widget.setMaximumSize(QSize(255, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(61, 48, 162);\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height:30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo_mc2.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Montserrat Black"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(24)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 25, -1, -1)
        self.dashboard2 = QPushButton(self.icon_text_widget)
        self.dashboard2.setObjectName(u"dashboard2")
        self.dashboard2.setStyleSheet(u"QPushButton{\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/dashboard3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard2.setIcon(icon8)
        self.dashboard2.setIconSize(QSize(150, 20))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard2)

        self.institute2 = QPushButton(self.icon_text_widget)
        self.institute2.setObjectName(u"institute2")
        self.institute2.setStyleSheet(u"QPushButton{\n"
"padding-left:-64px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/institute3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/institute2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institute2.setIcon(icon9)
        self.institute2.setIconSize(QSize(150, 20))
        self.institute2.setCheckable(True)
        self.institute2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institute2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.students2 = QPushButton(self.students)
        self.students2.setObjectName(u"students2")
        self.students2.setStyleSheet(u"QPushButton{\n"
"padding-left:-18px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students2.setIcon(icon10)
        self.students2.setIconSize(QSize(150, 20))
        self.students2.setCheckable(True)
        self.students2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.students2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(61, 48, 162);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(176, 94, 255);\n"
"}")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.students_info = QPushButton(self.students_dropdown)
        self.students_info.setObjectName(u"students_info")
        self.students_info.setStyleSheet(u"")
        self.students_info.setCheckable(True)
        self.students_info.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.students_info)

        self.students_payement = QPushButton(self.students_dropdown)
        self.students_payement.setObjectName(u"students_payement")
        self.students_payement.setCheckable(True)
        self.students_payement.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.students_payement)

        self.students_transactions = QPushButton(self.students_dropdown)
        self.students_transactions.setObjectName(u"students_transactions")
        self.students_transactions.setCheckable(True)
        self.students_transactions.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.students_transactions)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teachers2_2 = QPushButton(self.teachers)
        self.teachers2_2.setObjectName(u"teachers2_2")
        self.teachers2_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-18px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/teacher3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/teacher4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers2_2.setIcon(icon11)
        self.teachers2_2.setIconSize(QSize(150, 20))
        self.teachers2_2.setCheckable(True)
        self.teachers2_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.teachers2_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(61, 48, 162);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(176, 94, 255);\n"
"}")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teachers_info = QPushButton(self.teachers_dropdown)
        self.teachers_info.setObjectName(u"teachers_info")
        self.teachers_info.setCheckable(True)
        self.teachers_info.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teachers_info)

        self.teachers_salaries = QPushButton(self.teachers_dropdown)
        self.teachers_salaries.setObjectName(u"teachers_salaries")
        self.teachers_salaries.setCheckable(True)
        self.teachers_salaries.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teachers_salaries)

        self.teachers_transactions = QPushButton(self.teachers_dropdown)
        self.teachers_transactions.setObjectName(u"teachers_transactions")
        self.teachers_transactions.setCheckable(True)
        self.teachers_transactions.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teachers_transactions)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setFrameShape(QFrame.StyledPanel)
        self.finances.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finances2 = QPushButton(self.finances)
        self.finances2.setObjectName(u"finances2")
        self.finances2.setStyleSheet(u"QPushButton{\n"
"padding-left:-32px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/fianances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/fianances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances2.setIcon(icon12)
        self.finances2.setIconSize(QSize(150, 20))
        self.finances2.setCheckable(True)
        self.finances2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.finances2)

        self.finances_dropdown = QFrame(self.finances)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(61, 48, 162);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(176, 94, 255);\n"
"}")
        self.finances_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finances_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setCheckable(True)
        self.budgets.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finances_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setCheckable(True)
        self.expenses.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finances_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setCheckable(True)
        self.business_overview.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finances_dropdown)


        self.verticalLayout_7.addWidget(self.finances)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(25)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings2 = QPushButton(self.icon_text_widget)
        self.settings2.setObjectName(u"settings2")
        self.settings2.setStyleSheet(u"QPushButton{\n"
"padding-left:-40px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/settings3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings2.setIcon(icon13)
        self.settings2.setIconSize(QSize(150, 20))
        self.settings2.setCheckable(True)
        self.settings2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings2)

        self.signout2 = QPushButton(self.icon_text_widget)
        self.signout2.setObjectName(u"signout2")
        self.signout2.setStyleSheet(u"QPushButton{\n"
"padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/signout3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout2.setIcon(icon14)
        self.signout2.setIconSize(QSize(150, 20))
        self.signout2.setCheckable(True)
        self.signout2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout2)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 80))
        self.header_widget.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.label_26 = QLabel(self.header_widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(55, 47))
        self.label_26.setMaximumSize(QSize(55, 16777215))
        self.label_26.setPixmap(QPixmap(u":/icons/logo_mc.png"))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_26)

        self.menu_burger = QPushButton(self.header_widget)
        self.menu_burger.setObjectName(u"menu_burger")
        self.menu_burger.setStyleSheet(u"border:none;")
        icon15 = QIcon()
        icon15.addFile(u":/icons/menu_burger1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_burger.setIcon(icon15)
        self.menu_burger.setIconSize(QSize(29, 29))
        self.menu_burger.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu_burger)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.header_widget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_4.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        self.label_6.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.search_global_lineEdit = QLineEdit(self.header_widget)
        self.search_global_lineEdit.setObjectName(u"search_global_lineEdit")
        self.search_global_lineEdit.setMinimumSize(QSize(150, 0))
        self.search_global_lineEdit.setMaximumSize(QSize(16777215, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setStrikeOut(False)
        self.search_global_lineEdit.setFont(font3)
        self.search_global_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	border-radius:5px;\n"
"	padding:5px;\n"
"    \n"
"}")

        self.horizontalLayout_3.addWidget(self.search_global_lineEdit)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icons/user1.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_20.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(905, 771))
        self.main_screen_widget.setMaximumSize(QSize(16777215, 16777215))
        self.main_screen_widget.setStyleSheet(u"border-radius:3px;\n"
"background-color: rgb(243, 243, 243);")
        self.gridLayout_2 = QGridLayout(self.main_screen_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_15 = QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_24 = QLabel(self.page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(700, 51))
        self.label_24.setMaximumSize(QSize(700, 71))
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_24.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.horizontalSpacer_7 = QSpacerItem(24, 128, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(111, 131))
        self.label_21.setMaximumSize(QSize(111, 131))
        self.label_21.setPixmap(QPixmap(u":/icons/logo_mc.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_21)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(800, 400))
        self.label.setMaximumSize(QSize(1500, 765))
        self.label.setPixmap(QPixmap(u":/icons/CFPSF .jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_9)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 271, 31))
        font5 = QFont()
        font5.setFamilies([u"Montserrat SemiBold"])
        font5.setPointSize(14)
        self.label_8.setFont(font5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.verticalLayout_17.addWidget(self.label_9)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_19)


        self.gridLayout_4.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.addStudentBtn = QPushButton(self.page_3)
        self.addStudentBtn.setObjectName(u"addStudentBtn")
        self.addStudentBtn.setMinimumSize(QSize(200, 35))
        self.addStudentBtn.setMaximumSize(QSize(285, 16777215))
        font6 = QFont()
        font6.setBold(True)
        self.addStudentBtn.setFont(font6)
        self.addStudentBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(0, 117, 0);\n"
"font-weight:bold;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons8-add-male-user-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addStudentBtn.setIcon(icon16)

        self.horizontalLayout_7.addWidget(self.addStudentBtn)

        self.exportPDF_btn = QPushButton(self.page_3)
        self.exportPDF_btn.setObjectName(u"exportPDF_btn")
        self.exportPDF_btn.setMinimumSize(QSize(200, 35))
        self.exportPDF_btn.setMaximumSize(QSize(285, 16777215))
        self.exportPDF_btn.setFont(font6)
        self.exportPDF_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportPDF_btn.setIcon(icon17)

        self.horizontalLayout_7.addWidget(self.exportPDF_btn)

        self.exportExcel_btn = QPushButton(self.page_3)
        self.exportExcel_btn.setObjectName(u"exportExcel_btn")
        self.exportExcel_btn.setMinimumSize(QSize(200, 35))
        self.exportExcel_btn.setMaximumSize(QSize(285, 16777215))
        self.exportExcel_btn.setFont(font6)
        self.exportExcel_btn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportExcel_btn.setIcon(icon18)

        self.horizontalLayout_7.addWidget(self.exportExcel_btn)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(70, 16777215))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        self.label_22.setFont(font7)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.filterGender_comboBox = QComboBox(self.page_3)
        self.filterGender_comboBox.addItem("")
        self.filterGender_comboBox.addItem("")
        self.filterGender_comboBox.addItem("")
        self.filterGender_comboBox.setObjectName(u"filterGender_comboBox")
        self.filterGender_comboBox.setMaximumSize(QSize(170, 16777215))
        self.filterGender_comboBox.setStyleSheet(u"QComboBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: black;\n"
"selection-background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_8.addWidget(self.filterGender_comboBox)

        self.filterClass_comboBox = QComboBox(self.page_3)
        self.filterClass_comboBox.addItem("")
        self.filterClass_comboBox.setObjectName(u"filterClass_comboBox")
        self.filterClass_comboBox.setMaximumSize(QSize(185, 16777215))
        self.filterClass_comboBox.setStyleSheet(u"QComboBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: black;\n"
"selection-background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_8.addWidget(self.filterClass_comboBox)

        self.searchStudent_lineEdit = QLineEdit(self.page_3)
        self.searchStudent_lineEdit.setObjectName(u"searchStudent_lineEdit")
        self.searchStudent_lineEdit.setMinimumSize(QSize(300, 0))
        self.searchStudent_lineEdit.setMaximumSize(QSize(16777215, 31))
        self.searchStudent_lineEdit.setFont(font3)
        self.searchStudent_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:1px solid black;\n"
"	border-radius:5px;\n"
"	padding:5px;\n"
"    \n"
"}")

        self.horizontalLayout_8.addWidget(self.searchStudent_lineEdit)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(self.page_3)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(500, 0))
        self.tableWidget.setStyleSheet(u"QHeaderView:section{\n"
"font-weight:bold;\n"
"background-color:black;\n"
"color:white;}")

        self.gridLayout_4.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_16 = QVBoxLayout(self.page_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 26))
        self.label_10.setMaximumSize(QSize(16777215, 26))
        self.label_10.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_10)

        self.label_20 = QLabel(self.page_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font2)

        self.verticalLayout_14.addWidget(self.label_20)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.addPayeOldStudentBtn = QPushButton(self.page_4)
        self.addPayeOldStudentBtn.setObjectName(u"addPayeOldStudentBtn")
        self.addPayeOldStudentBtn.setMinimumSize(QSize(230, 35))
        self.addPayeOldStudentBtn.setMaximumSize(QSize(285, 16777215))
        self.addPayeOldStudentBtn.setFont(font6)
        self.addPayeOldStudentBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(0, 117, 0);\n"
"font-weight:bold;\n"
"}")
        self.addPayeOldStudentBtn.setIcon(icon16)

        self.horizontalLayout_13.addWidget(self.addPayeOldStudentBtn)

        self.exportPDF_btn_2 = QPushButton(self.page_4)
        self.exportPDF_btn_2.setObjectName(u"exportPDF_btn_2")
        self.exportPDF_btn_2.setMinimumSize(QSize(200, 35))
        self.exportPDF_btn_2.setMaximumSize(QSize(285, 16777215))
        self.exportPDF_btn_2.setFont(font6)
        self.exportPDF_btn_2.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")
        self.exportPDF_btn_2.setIcon(icon17)

        self.horizontalLayout_13.addWidget(self.exportPDF_btn_2)

        self.exportExcel_btn_2 = QPushButton(self.page_4)
        self.exportExcel_btn_2.setObjectName(u"exportExcel_btn_2")
        self.exportExcel_btn_2.setMinimumSize(QSize(200, 35))
        self.exportExcel_btn_2.setMaximumSize(QSize(285, 16777215))
        self.exportExcel_btn_2.setFont(font6)
        self.exportExcel_btn_2.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(187, 187, 187);\n"
"font-weight:bold;\n"
"}")
        self.exportExcel_btn_2.setIcon(icon18)

        self.horizontalLayout_13.addWidget(self.exportExcel_btn_2)

        self.horizontalSpacer_6 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_23 = QLabel(self.page_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(70, 16777215))
        self.label_23.setFont(font7)

        self.horizontalLayout_6.addWidget(self.label_23)

        self.filterGender_comboBox_2 = QComboBox(self.page_4)
        self.filterGender_comboBox_2.addItem("")
        self.filterGender_comboBox_2.addItem("")
        self.filterGender_comboBox_2.addItem("")
        self.filterGender_comboBox_2.setObjectName(u"filterGender_comboBox_2")
        self.filterGender_comboBox_2.setMaximumSize(QSize(170, 16777215))
        self.filterGender_comboBox_2.setStyleSheet(u"QComboBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: black;\n"
"selection-background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.filterGender_comboBox_2)

        self.filterClass_comboBox_2 = QComboBox(self.page_4)
        self.filterClass_comboBox_2.addItem("")
        self.filterClass_comboBox_2.setObjectName(u"filterClass_comboBox_2")
        self.filterClass_comboBox_2.setMaximumSize(QSize(185, 16777215))
        self.filterClass_comboBox_2.setStyleSheet(u"QComboBox{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: black;\n"
"selection-background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.filterClass_comboBox_2)

        self.filterDate_dateEdit = QDateEdit(self.page_4)
        self.filterDate_dateEdit.setObjectName(u"filterDate_dateEdit")
        self.filterDate_dateEdit.setMinimumSize(QSize(130, 0))
        self.filterDate_dateEdit.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"height:35px;\n"
"padding-left:15px;\n"
"color:white;\n"
"background-color: black;\n"
"selection-background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.filterDate_dateEdit)

        self.searchStudent_lineEdit_2 = QLineEdit(self.page_4)
        self.searchStudent_lineEdit_2.setObjectName(u"searchStudent_lineEdit_2")
        self.searchStudent_lineEdit_2.setMinimumSize(QSize(200, 0))
        self.searchStudent_lineEdit_2.setMaximumSize(QSize(16777215, 31))
        self.searchStudent_lineEdit_2.setFont(font3)
        self.searchStudent_lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border:1px solid black;\n"
"	border-radius:5px;\n"
"	padding:5px;\n"
"    \n"
"}")

        self.horizontalLayout_6.addWidget(self.searchStudent_lineEdit_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.tableWidget_2 = QTableWidget(self.page_4)
        if (self.tableWidget_2.columnCount() < 12):
            self.tableWidget_2.setColumnCount(12)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem21)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(500, 500))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 600))
        self.tableWidget_2.setStyleSheet(u"QHeaderView:section{\n"
"font-weight:bold;\n"
"background-color:black;\n"
"color:white;}")

        self.verticalLayout_16.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 321, 31))
        self.label_11.setFont(font5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 10, 331, 31))
        self.label_12.setFont(font5)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 0, 271, 31))
        self.label_13.setFont(font5)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 321, 31))
        self.label_14.setFont(font5)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 0, 271, 31))
        self.label_15.setFont(font5)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 10, 271, 31))
        self.label_16.setFont(font5)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 0, 271, 31))
        self.label_17.setFont(font5)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 271, 31))
        self.label_18.setFont(font5)
        self.layoutWidget = QWidget(self.page_12)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 419, 41))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gest_compte_pushButton = QPushButton(self.layoutWidget)
        self.gest_compte_pushButton.setObjectName(u"gest_compte_pushButton")
        self.gest_compte_pushButton.setMinimumSize(QSize(200, 35))
        self.gest_compte_pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.gest_compte_pushButton)

        self.uptade_compte_pushButton = QPushButton(self.layoutWidget)
        self.uptade_compte_pushButton.setObjectName(u"uptade_compte_pushButton")
        self.uptade_compte_pushButton.setMinimumSize(QSize(210, 35))
        self.uptade_compte_pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(176, 94, 255);\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.uptade_compte_pushButton)

        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_18 = QVBoxLayout(self.page_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_25 = QLabel(self.page_13)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)

        self.verticalLayout_18.addWidget(self.label_25)

        self.add_compte_pushButton = QPushButton(self.page_13)
        self.add_compte_pushButton.setObjectName(u"add_compte_pushButton")
        self.add_compte_pushButton.setMinimumSize(QSize(200, 35))
        self.add_compte_pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-size:15px;\n"
"	background-color: rgb(61, 48, 162);\n"
"font-weight:bold;\n"
"}")

        self.verticalLayout_18.addWidget(self.add_compte_pushButton)

        self.verticalSpacer_5 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.compte_tableWidget = QTableWidget(self.page_13)
        if (self.compte_tableWidget.columnCount() < 4):
            self.compte_tableWidget.setColumnCount(4)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.compte_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.compte_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.compte_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.compte_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        self.compte_tableWidget.setObjectName(u"compte_tableWidget")
        self.compte_tableWidget.setMinimumSize(QSize(850, 550))
        self.compte_tableWidget.setStyleSheet(u"QHeaderView:section{\n"
"font-weight:bold;\n"
"background-color:black;\n"
"color:white;}")

        self.verticalLayout_18.addWidget(self.compte_tableWidget)

        self.verticalSpacer_6 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page_13)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.main_screen_widget)


        self.gridLayout_3.addLayout(self.verticalLayout_20, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.students2.toggled.connect(self.students_dropdown.setHidden)
        self.teachers2_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.finances2.toggled.connect(self.finances_dropdown.setHidden)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.institute2.toggled.connect(self.institute1.setChecked)
        self.students2.toggled.connect(self.students1.setChecked)
        self.teachers2_2.toggled.connect(self.teachers1.setChecked)
        self.finances2.toggled.connect(self.finances1.setChecked)
        self.settings2.toggled.connect(self.settings1.setChecked)
        self.signout2.toggled.connect(self.signout1.setChecked)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.institute1.toggled.connect(self.institute2.setChecked)
        self.students1.toggled.connect(self.students2.setChecked)
        self.teachers1.toggled.connect(self.teachers2_2.setChecked)
        self.settings1.toggled.connect(self.settings2.setChecked)
        self.signout1.toggled.connect(self.signout2.setChecked)
        self.menu_burger.toggled.connect(self.icon_text_widget.setHidden)
        self.menu_burger.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.dashboard1.setText("")
        self.institute1.setText("")
        self.students1.setText("")
        self.teachers1.setText("")
        self.finances1.setText("")
        self.settings1.setText("")
        self.signout1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M.C. SCHOOL", None))
        self.dashboard2.setText("")
        self.institute2.setText("")
        self.students2.setText("")
        self.students_info.setText(QCoreApplication.translate("MainWindow", u"Informations Apprenants", None))
        self.students_payement.setText(QCoreApplication.translate("MainWindow", u"Paiements Apprenants", None))
        self.students_transactions.setText(QCoreApplication.translate("MainWindow", u"Transactions Apprenants", None))
        self.teachers2_2.setText("")
        self.teachers_info.setText(QCoreApplication.translate("MainWindow", u"Informations Enseignants", None))
        self.teachers_salaries.setText(QCoreApplication.translate("MainWindow", u"Salaires Enseignants", None))
        self.teachers_transactions.setText(QCoreApplication.translate("MainWindow", u"Transactions Enseignants", None))
        self.finances2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Depenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.settings2.setText("")
        self.signout2.setText("")
        self.label_26.setText("")
        self.menu_burger.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Centre de Formation Professionnel Sainte Famille", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Heureux de vous revoir!", None))
        self.search_global_lineEdit.setText("")
        self.search_global_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici...", None))
        self.label_5.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Bienvenue sur Mon Compagnon Scolaire", None))
        self.label_21.setText("")
        self.label.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Centre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Informations Apprenants", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ceci est la page pour enregistrer les informations des apprenants", None))
        self.addStudentBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter un Apprenant", None))
        self.exportPDF_btn.setText(QCoreApplication.translate("MainWindow", u"Exporter le PDF", None))
        self.exportExcel_btn.setText(QCoreApplication.translate("MainWindow", u"Exporter Excel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par :", None))
        self.filterGender_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Selectionner le sexe", None))
        self.filterGender_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"F\u00e9minin", None))
        self.filterGender_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Masculin", None))

        self.filterClass_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Selectionner la classe", None))

        self.searchStudent_lineEdit.setText("")
        self.searchStudent_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9noms", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sexe", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lieu de naissance", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Classe", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Paiements Apprenants", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ceci est la page pour enregistrer les paiements des apprenants et generer les recus", None))
        self.addPayeOldStudentBtn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer un paiement", None))
        self.exportPDF_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exporter le PDF", None))
        self.exportExcel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exporter Excel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par :", None))
        self.filterGender_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Selectionner le sexe", None))
        self.filterGender_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"F\u00e9minin", None))
        self.filterGender_comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Masculin", None))

        self.filterClass_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Selectionner la classe", None))

        self.searchStudent_lineEdit_2.setText("")
        self.searchStudent_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici...", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9noms", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Sexe", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Classe", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Raison", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Montant vers\u00e9", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Date de versement", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Solde", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Reste", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Transactions Apprenants", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Informations Enseignants", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Salaires Enseignants", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Transactions Enseigants", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Depenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.gest_compte_pushButton.setText(QCoreApplication.translate("MainWindow", u"Gestion des comptes", None))
        self.uptade_compte_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mettre a jour mon compte", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Gestions des comptes", None))
        self.add_compte_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter un compte", None))
        ___qtablewidgetitem22 = self.compte_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Titulaire", None));
        ___qtablewidgetitem23 = self.compte_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nom utilisateur", None));
        ___qtablewidgetitem24 = self.compte_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem25 = self.compte_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
    # retranslateUi

