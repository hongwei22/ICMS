# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\UM\Year 3\Sem 2\KIX3001\ICMS\gui\src\Loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_text = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_text.setFont(font)
        self.welcome_text.setStyleSheet("color: black;")
        self.welcome_text.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_text.setObjectName("welcome_text")
        self.verticalLayout.addWidget(self.welcome_text)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border-radius: 10px;\n"
"    background-color: #d4ebd3;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background-color: #5c965a;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome_text.setText(_translate("Form", "Welcome"))
