# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(1147, 778)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = ClickableLabel(Dialog)
        self.logo.setEnabled(True)
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(".\\src\\img/register/ICMS.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.sidebar_home = ClickableLabel(Dialog)
        self.sidebar_home.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar_home.setMouseTracking(False)
        self.sidebar_home.setAutoFillBackground(False)
        self.sidebar_home.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar_home.setText("")
        self.sidebar_home.setPixmap(QtGui.QPixmap(".\\src\\img/register/home.png"))
        self.sidebar_home.setScaledContents(False)
        self.sidebar_home.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_home.setObjectName("sidebar_home")
        self.verticalLayout_2.addWidget(self.sidebar_home)
        self.sidebar_camera = ClickableLabel(Dialog)
        self.sidebar_camera.setStyleSheet("background-color: rgb(0,0,0)")
        self.sidebar_camera.setText("")
        self.sidebar_camera.setPixmap(QtGui.QPixmap(".\\src\\img/register/camera.png"))
        self.sidebar_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_camera.setObjectName("sidebar_camera")
        self.verticalLayout_2.addWidget(self.sidebar_camera)
        self.sidebar_record = ClickableLabel(Dialog)
        self.sidebar_record.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_record.setText("")
        self.sidebar_record.setPixmap(QtGui.QPixmap(".\\src\\img/register/search.png"))
        self.sidebar_record.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_record.setObjectName("sidebar_record")
        self.verticalLayout_2.addWidget(self.sidebar_record)
        self.sidebar_logout = ClickableLabel(Dialog)
        self.sidebar_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sidebar_logout.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_logout.setText("")
        self.sidebar_logout.setPixmap(QtGui.QPixmap(".\\src\\img/register/exit.png"))
        self.sidebar_logout.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_logout.setObjectName("sidebar_logout")
        self.verticalLayout_2.addWidget(self.sidebar_logout)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, 100, 100, 100)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.login_title.setWordWrap(False)
        self.login_title.setObjectName("login_title")
        self.verticalLayout.addWidget(self.login_title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_msg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_msg.setFont(font)
        self.login_msg.setStyleSheet("color: red;")
        self.login_msg.setText("")
        self.login_msg.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.login_msg.setObjectName("login_msg")
        self.horizontalLayout_2.addWidget(self.login_msg)
        self.login_msg_register = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.login_msg_register.setFont(font)
        self.login_msg_register.setStyleSheet("color: red;")
        self.login_msg_register.setText("")
        self.login_msg_register.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_msg_register.setObjectName("login_msg_register")
        self.horizontalLayout_2.addWidget(self.login_msg_register)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_email = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_email.setFont(font)
        self.login_email.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_email.setObjectName("login_email")
        self.verticalLayout.addWidget(self.login_email)
        self.login_email_text = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_email_text.setFont(font)
        self.login_email_text.setInputMask("")
        self.login_email_text.setText("")
        self.login_email_text.setObjectName("login_email_text")
        self.verticalLayout.addWidget(self.login_email_text)
        self.login_password = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_password.setFont(font)
        self.login_password.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_password.setObjectName("login_password")
        self.verticalLayout.addWidget(self.login_password)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_password_text = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_password_text.setFont(font)
        self.login_password_text.setStyleSheet("")
        self.login_password_text.setText("")
        self.login_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_text.setObjectName("login_password_text")
        self.horizontalLayout_3.addWidget(self.login_password_text)
        self.show_password = ClickableLabel(Dialog)
        self.show_password.setStyleSheet("background: white")
        self.show_password.setText("")
        self.show_password.setPixmap(QtGui.QPixmap(".\\src\\img/register/hidden.png"))
        self.show_password.setObjectName("show_password")
        self.horizontalLayout_3.addWidget(self.show_password)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.login_checkbox = QtWidgets.QHBoxLayout()
        self.login_checkbox.setContentsMargins(-1, -1, 30, -1)
        self.login_checkbox.setSpacing(0)
        self.login_checkbox.setObjectName("login_checkbox")
        self.login_remember = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_remember.setFont(font)
        self.login_remember.setObjectName("login_remember")
        self.login_checkbox.addWidget(self.login_remember)
        self.login_forget = ClickableLabel(Dialog)
        self.login_forget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.login_forget.setFont(font)
        self.login_forget.setAcceptDrops(False)
        self.login_forget.setStyleSheet("color: #0000ff;")
        self.login_forget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_forget.setObjectName("login_forget")
        self.login_checkbox.addWidget(self.login_forget)
        self.login_checkbox.setStretch(0, 60)
        self.login_checkbox.setStretch(1, 40)
        self.verticalLayout.addLayout(self.login_checkbox)
        self.login_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signup_title = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_title.setFont(font)
        self.signup_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.signup_title.setOpenExternalLinks(True)
        self.signup_title.setObjectName("signup_title")
        self.horizontalLayout.addWidget(self.signup_title)
        self.signup_link = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.signup_link.setFont(font)
        self.signup_link.setStyleSheet("color: #0000ff")
        self.signup_link.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.signup_link.setOpenExternalLinks(True)
        self.signup_link.setObjectName("signup_link")
        self.horizontalLayout.addWidget(self.signup_link)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.login_title.setText(_translate("Dialog", "Welcome"))
        self.login_email.setText(_translate("Dialog", "Email / Username"))
        self.login_email_text.setPlaceholderText(_translate("Dialog", "Username"))
        self.login_password.setText(_translate("Dialog", "Password"))
        self.login_password_text.setPlaceholderText(_translate("Dialog", "Password"))
        self.login_remember.setText(_translate("Dialog", "    Remember me"))
        self.login_forget.setText(_translate("Dialog", "Forget Password"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_title.setText(_translate("Dialog", "Don\'t have an account yet? "))
        self.signup_link.setText(_translate("Dialog", "Sign up here"))
from core.clickableLabel import ClickableLabel
