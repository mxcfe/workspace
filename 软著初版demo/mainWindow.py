# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(920, 532)
        mainWindow.setMinimumSize(QSize(920, 532))
        mainWindow.setMaximumSize(QSize(920, 532))
        mainWindow.setDockNestingEnabled(False)
        self.action = QAction(mainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(mainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionCopy = QAction(mainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(mainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.action_3 = QAction(mainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action1 = QAction(mainWindow)
        self.action1.setObjectName(u"action1")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 240))
        self.label_2.setPixmap(QPixmap(u"icon/main.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(10, 50))

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.userinfo = QWidget(self.centralwidget)
        self.userinfo.setObjectName(u"userinfo")
        self.gridLayout_9 = QGridLayout(self.userinfo)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.userinfo)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.gridLayout_9.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.userinfo)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(11)
        self.label_4.setFont(font1)

        self.gridLayout_9.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.userinfo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_9.addWidget(self.label_8, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.userinfo)

        self.userlogin = QWidget(self.centralwidget)
        self.userlogin.setObjectName(u"userlogin")
        self.userlogin.setMaximumSize(QSize(148, 16777215))
        self.gridLayout_8 = QGridLayout(self.userlogin)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_3 = QLineEdit(self.userlogin)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_8.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.userlogin)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_8.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.userlogin)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.gridLayout_8.addWidget(self.lineEdit_4, 2, 0, 1, 1)

        self.label_7 = QLabel(self.userlogin)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.userlogin)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.tabWidget.setFont(font2)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(24, 24))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout_4 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_4 = QSplitter(self.tabWidgetPage1)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.btn_find_paper = QPushButton(self.splitter_4)
        self.btn_find_paper.setObjectName(u"btn_find_paper")
        self.btn_find_paper.setMinimumSize(QSize(96, 96))
        self.btn_find_paper.setMaximumSize(QSize(96, 96))
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        self.btn_find_paper.setFont(font3)
        self.btn_find_paper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_find_paper.setAcceptDrops(False)
        self.btn_find_paper.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/\u5546\u54c1\u7ba1\u7406.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_find_paper.setIcon(icon)
        self.btn_find_paper.setIconSize(QSize(64, 64))
        self.btn_find_paper.setCheckable(False)
        self.btn_find_paper.setAutoRepeat(False)
        self.btn_find_paper.setAutoExclusive(False)
        self.btn_find_paper.setAutoDefault(False)
        self.btn_find_paper.setFlat(False)
        self.splitter_4.addWidget(self.btn_find_paper)
        self.label_11 = QLabel(self.splitter_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 20))
        self.label_11.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.splitter_4.addWidget(self.label_11)

        self.gridLayout.addWidget(self.splitter_4, 0, 3, 1, 1)

        self.splitter_7 = QSplitter(self.tabWidgetPage1)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.btn_find_paper_3 = QPushButton(self.splitter_7)
        self.btn_find_paper_3.setObjectName(u"btn_find_paper_3")
        self.btn_find_paper_3.setMinimumSize(QSize(96, 96))
        self.btn_find_paper_3.setMaximumSize(QSize(96, 96))
        self.btn_find_paper_3.setFont(font3)
        self.btn_find_paper_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_find_paper_3.setAcceptDrops(False)
        self.btn_find_paper_3.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/\u5bfc\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_find_paper_3.setIcon(icon1)
        self.btn_find_paper_3.setIconSize(QSize(64, 64))
        self.btn_find_paper_3.setCheckable(False)
        self.btn_find_paper_3.setAutoRepeat(False)
        self.btn_find_paper_3.setAutoExclusive(False)
        self.btn_find_paper_3.setAutoDefault(False)
        self.btn_find_paper_3.setFlat(False)
        self.splitter_7.addWidget(self.btn_find_paper_3)
        self.label_16 = QLabel(self.splitter_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setFont(font4)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.splitter_7.addWidget(self.label_16)

        self.gridLayout.addWidget(self.splitter_7, 2, 5, 1, 1)

        self.label_13 = QLabel(self.tabWidgetPage1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 50))
        self.label_13.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)

        self.splitter_3 = QSplitter(self.tabWidgetPage1)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.btn_kg_all = QPushButton(self.splitter_3)
        self.btn_kg_all.setObjectName(u"btn_kg_all")
        self.btn_kg_all.setMinimumSize(QSize(96, 96))
        self.btn_kg_all.setMaximumSize(QSize(96, 96))
        font5 = QFont()
        font5.setFamily(u"SimSun")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        self.btn_kg_all.setFont(font5)
        self.btn_kg_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kg_all.setAcceptDrops(False)
#if QT_CONFIG(statustip)
        self.btn_kg_all.setStatusTip(u"\u5c55\u793a\u6570\u636e\u5e93\u77e5\u8bc6\u56fe\u8c31\u6982\u51b5")
#endif // QT_CONFIG(statustip)
        self.btn_kg_all.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icon/puzzle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_kg_all.setIcon(icon2)
        self.btn_kg_all.setIconSize(QSize(64, 64))
        self.btn_kg_all.setCheckable(False)
        self.btn_kg_all.setAutoRepeat(False)
        self.btn_kg_all.setAutoExclusive(False)
        self.btn_kg_all.setAutoDefault(False)
        self.btn_kg_all.setFlat(False)
        self.splitter_3.addWidget(self.btn_kg_all)
        self.label_10 = QLabel(self.splitter_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.label_10)

        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.label_14 = QLabel(self.tabWidgetPage1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 50))
        self.label_14.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_17 = QLabel(self.tabWidgetPage1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 50))
        self.label_17.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.label_17, 0, 4, 1, 1)

        self.splitter_5 = QSplitter(self.tabWidgetPage1)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.btn_find_node = QPushButton(self.splitter_5)
        self.btn_find_node.setObjectName(u"btn_find_node")
        self.btn_find_node.setMinimumSize(QSize(96, 96))
        self.btn_find_node.setMaximumSize(QSize(96, 96))
        self.btn_find_node.setFont(font3)
        self.btn_find_node.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_find_node.setAcceptDrops(False)
        self.btn_find_node.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icon/\u653e\u5927\u955c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_find_node.setIcon(icon3)
        self.btn_find_node.setIconSize(QSize(64, 64))
        self.btn_find_node.setCheckable(False)
        self.btn_find_node.setAutoRepeat(False)
        self.btn_find_node.setAutoExclusive(False)
        self.btn_find_node.setAutoDefault(False)
        self.btn_find_node.setFlat(False)
        self.splitter_5.addWidget(self.btn_find_node)
        self.label_12 = QLabel(self.splitter_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 20))
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setIndent(1)
        self.splitter_5.addWidget(self.label_12)

        self.gridLayout.addWidget(self.splitter_5, 0, 5, 1, 1)

        self.splitter_2 = QSplitter(self.tabWidgetPage1)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.btn_history = QPushButton(self.splitter_2)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setMinimumSize(QSize(96, 96))
        self.btn_history.setMaximumSize(QSize(96, 96))
        self.btn_history.setFont(font5)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setAcceptDrops(False)
        self.btn_history.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icon/\u5b66\u4e60\u4e2d\u5fc3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_history.setIcon(icon4)
        self.btn_history.setIconSize(QSize(64, 64))
        self.btn_history.setCheckable(False)
        self.btn_history.setAutoRepeat(False)
        self.btn_history.setAutoExclusive(False)
        self.btn_history.setAutoDefault(False)
        self.btn_history.setFlat(False)
        self.splitter_2.addWidget(self.btn_history)
        self.label_30 = QLabel(self.splitter_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 20))
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setFont(font4)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_30)

        self.gridLayout.addWidget(self.splitter_2, 2, 0, 1, 1)

        self.splitter_6 = QSplitter(self.tabWidgetPage1)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.btn_find_paper_2 = QPushButton(self.splitter_6)
        self.btn_find_paper_2.setObjectName(u"btn_find_paper_2")
        self.btn_find_paper_2.setMinimumSize(QSize(96, 96))
        self.btn_find_paper_2.setMaximumSize(QSize(96, 96))
        self.btn_find_paper_2.setFont(font3)
        self.btn_find_paper_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_find_paper_2.setAcceptDrops(False)
        self.btn_find_paper_2.setStyleSheet(u"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-width: 3px;\n"
"	border-color: #999999;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"QPushButton{\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(80, 80, 80);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icon/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_find_paper_2.setIcon(icon5)
        self.btn_find_paper_2.setIconSize(QSize(64, 64))
        self.btn_find_paper_2.setCheckable(False)
        self.btn_find_paper_2.setAutoRepeat(False)
        self.btn_find_paper_2.setAutoExclusive(False)
        self.btn_find_paper_2.setAutoDefault(False)
        self.btn_find_paper_2.setFlat(False)
        self.splitter_6.addWidget(self.btn_find_paper_2)
        self.label_15 = QLabel(self.splitter_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font4)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.splitter_6.addWidget(self.label_15)

        self.gridLayout.addWidget(self.splitter_6, 2, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u"icon/\u9996\u9875.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage1, icon6, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.gridLayout_7 = QGridLayout(self.tabWidgetPage2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget = QWebEngineView(self.tabWidgetPage2)
        self.widget.setObjectName(u"widget")

        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage2, icon2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.gridLayout_5 = QGridLayout(self.tabWidgetPage3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.tabWidgetPage3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.tabWidgetPage3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 0, 1, 1, 1)

        self.tableWidget = QTableWidget(self.tabWidgetPage3)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tabWidgetPage3, icon, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_6.addWidget(self.pushButton_4, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.widget_2 = QWebEngineView(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 361))

        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, icon3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.gridLayout_10 = QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.tableWidget1 = QTableWidget(self.tab_2)
        if (self.tableWidget1.columnCount() < 2):
            self.tableWidget1.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tableWidget1.setObjectName(u"tableWidget1")

        self.verticalLayout_3.addWidget(self.tableWidget1)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.tableWidget2 = QTableWidget(self.tab_2)
        if (self.tableWidget2.columnCount() < 2):
            self.tableWidget2.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.tableWidget2.setObjectName(u"tableWidget2")

        self.verticalLayout_5.addWidget(self.tableWidget2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, icon4, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.pushButton.clicked.connect(mainWindow.find_paper)
        self.pushButton_2.clicked.connect(mainWindow.find_node)
        self.pushButton_3.clicked.connect(mainWindow.login)
        self.btn_find_paper_3.clicked.connect(mainWindow.output)
        self.btn_find_paper_2.clicked.connect(mainWindow.input)
        self.pushButton_4.clicked.connect(mainWindow.saveImg)

        self.tabWidget.setCurrentIndex(0)
        self.btn_find_paper.setDefault(False)
        self.btn_find_paper_3.setDefault(False)
        self.btn_kg_all.setDefault(False)
        self.btn_find_node.setDefault(False)
        self.btn_history.setDefault(False)
        self.btn_find_paper_2.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("mainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.action.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_2.setText(QCoreApplication.translate("mainWindow", u"daoru", None))
#if QT_CONFIG(shortcut)
        self.action_2.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("mainWindow", u"\u590d\u5236", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("mainWindow", u"\u7c98\u8d34", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.action_3.setText(QCoreApplication.translate("mainWindow", u"daochu", None))
#if QT_CONFIG(shortcut)
        self.action_3.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action1.setText(QCoreApplication.translate("mainWindow", u"\u5173\u4e8e", None))
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u6635\u79f0\uff1awjsw", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4\uff1a\n"
"01-01 23:15:33", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u7528\u6237\u540d", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"\u6ce8\u518c/\u767b\u5f55", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u5bc6\u7801", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u6ce8\u518c/\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.btn_find_paper.setToolTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_find_paper.setStatusTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(statustip)
        self.btn_find_paper.setText("")
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u8bba\u6587\u68c0\u7d22", None))
#if QT_CONFIG(tooltip)
        self.btn_find_paper_3.setToolTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_find_paper_3.setStatusTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(statustip)
        self.btn_find_paper_3.setText("")
        self.label_16.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa", None))
        self.label_13.setText("")
#if QT_CONFIG(tooltip)
        self.btn_kg_all.setToolTip(QCoreApplication.translate("mainWindow", u"\u5c55\u793a\u6570\u636e\u5e93\u77e5\u8bc6\u56fe\u8c31\u6982\u51b5", None))
#endif // QT_CONFIG(tooltip)
        self.btn_kg_all.setText("")
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u8c31\u5c55\u793a", None))
        self.label_14.setText("")
        self.label_17.setText("")
#if QT_CONFIG(tooltip)
        self.btn_find_node.setToolTip(QCoreApplication.translate("mainWindow", u"\u6839\u636e\u5173\u952e\u5b57\u67e5\u8be2\u8282\u70b9\u56fe\u8c31", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_find_node.setStatusTip(QCoreApplication.translate("mainWindow", u"\u6839\u636e\u5173\u952e\u5b57\u67e5\u8be2\u8282\u70b9\u56fe\u8c31", None))
#endif // QT_CONFIG(statustip)
        self.btn_find_node.setText("")
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u8282\u70b9\u68c0\u7d22", None))
#if QT_CONFIG(tooltip)
        self.btn_history.setToolTip(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u6240\u6709\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_history.setStatusTip(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u6240\u6709\u6570\u636e", None))
#endif // QT_CONFIG(statustip)
        self.btn_history.setText("")
        self.label_30.setText(QCoreApplication.translate("mainWindow", u"\u5386\u53f2\u68c0\u7d22", None))
#if QT_CONFIG(tooltip)
        self.btn_find_paper_2.setToolTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_find_paper_2.setStatusTip(QCoreApplication.translate("mainWindow", u"\u6309\u6307\u5b9a\u5185\u5bb9\u67e5\u8be2\u8bba\u6587", None))
#endif // QT_CONFIG(statustip)
        self.btn_find_paper_2.setText("")
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("mainWindow", u"\u4e3b\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("mainWindow", u"\u56fe\u8c31\u5c55\u793a", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u8bba\u6587\u68c0\u7d22", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\u4f5c\u8005", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\u7c7b\u522b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"\u51fa\u7248\u793e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"\u51fa\u7248\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"\u4e0b\u8f7d\u91cf", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"\u5173\u952e\u5b57", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QCoreApplication.translate("mainWindow", u"\u8bba\u6587\u68c0\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"\u8282\u70b9\u68c0\u7d22", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u8282\u70b9\u68c0\u7d22", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u8bba\u6587\u68c0\u7d22\u8bb0\u5f55", None))
        ___qtablewidgetitem7 = self.tableWidget1.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22\u5185\u5bb9", None));
        ___qtablewidgetitem8 = self.tableWidget1.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"\u65f6\u95f4", None));
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u8282\u70b9\u68c0\u7d22\u8bb0\u5f55", None))
        ___qtablewidgetitem9 = self.tableWidget2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem10 = self.tableWidget2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22\u65f6\u95f4", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"\u5386\u53f2\u68c0\u7d22", None))
    # retranslateUi

