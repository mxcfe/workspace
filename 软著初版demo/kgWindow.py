# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kgWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_kgWindow(object):
    def setupUi(self, kgWindow):
        if not kgWindow.objectName():
            kgWindow.setObjectName(u"kgWindow")
        kgWindow.resize(704, 525)
        self.widget = QWebEngineView(kgWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 701, 521))
        self.widget.setMinimumSize(QSize(500, 500))
        self.gridLayoutWidget_2 = QWidget(kgWindow)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(480, 10, 211, 31))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.retranslateUi(kgWindow)
        self.pushButton_2.clicked.connect(kgWindow.select)

        QMetaObject.connectSlotsByName(kgWindow)
    # setupUi

    def retranslateUi(self, kgWindow):
        kgWindow.setWindowTitle(QCoreApplication.translate("kgWindow", u"\u8282\u70b9\u56fe\u8c31", None))
        self.pushButton_2.setText(QCoreApplication.translate("kgWindow", u"\u8282\u70b9\u68c0\u7d22", None))
    # retranslateUi

