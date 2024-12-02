# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paperDetailsWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_paperDetailsWindow(object):
    def setupUi(self, paperDetailsWindow):
        if not paperDetailsWindow.objectName():
            paperDetailsWindow.setObjectName(u"paperDetailsWindow")
        paperDetailsWindow.resize(800, 638)
        paperDetailsWindow.setMaximumSize(QSize(800, 16777215))
        paperDetailsWindow.setStyleSheet(u"background-color:#f0f3f8")
        self.gridLayout_5 = QGridLayout(paperDetailsWindow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.widget_3 = QWidget(paperDetailsWindow)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.widget_3, 1, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(paperDetailsWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.textBrowser = QTextBrowser(paperDetailsWindow)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(320, 0))
        self.textBrowser.setStyleSheet(u"border:0px")

        self.verticalLayout.addWidget(self.textBrowser)

        self.label_2 = QLabel(paperDetailsWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWebEngineView(paperDetailsWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 3)

        self.widget_2 = QWidget(paperDetailsWindow)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 0))
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 0, 93, 28))

        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(paperDetailsWindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton = QPushButton(paperDetailsWindow)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(100, -1, 100, -1)
        self.label_3 = QLabel(paperDetailsWindow)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 4, 1)

        self.label_4 = QLabel(paperDetailsWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 10))
        self.label_4.setMaximumSize(QSize(70, 20))

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_5 = QLabel(paperDetailsWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(70, 10))
        self.label_5.setMaximumSize(QSize(70, 20))

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.retranslateUi(paperDetailsWindow)
        self.pushButton.clicked.connect(paperDetailsWindow.select)
        self.pushButton_2.clicked.connect(paperDetailsWindow.output)

        QMetaObject.connectSlotsByName(paperDetailsWindow)
    # setupUi

    def retranslateUi(self, paperDetailsWindow):
        paperDetailsWindow.setWindowTitle(QCoreApplication.translate("paperDetailsWindow", u"\u8be6\u60c5", None))
        self.label.setText(QCoreApplication.translate("paperDetailsWindow", u"\u6458\u8981\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("paperDetailsWindow", u"\u9605\u8bfb\u539f\u6587", None))
        self.pushButton_2.setText(QCoreApplication.translate("paperDetailsWindow", u"\u5bfc\u51fa", None))
        self.pushButton.setText(QCoreApplication.translate("paperDetailsWindow", u"\u8282\u70b9\u68c0\u7d22", None))
        self.label_3.setText(QCoreApplication.translate("paperDetailsWindow", u"\u85cf\u836f\u56db\u81e3\u9897\u7c92\u5927\u9f20\u53e3\u670d\u7ed9\u836f13\u5468\u957f\u671f\u6bd2\u6027\u7814\u7a76", None))
        self.label_4.setText(QCoreApplication.translate("paperDetailsWindow", u"\u7f51\u7edc\u9996\u53d1", None))
        self.label_5.setText(QCoreApplication.translate("paperDetailsWindow", u"\u7f51\u7edc\u9996\u53d1", None))
    # retranslateUi

