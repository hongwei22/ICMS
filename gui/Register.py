# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sidebar = QtWidgets.QVBoxLayout()
        self.sidebar.setSpacing(0)
        self.sidebar.setObjectName("sidebar")
        self.logo = ClickableLabel(Dialog)
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Image/Register/Logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.sidebar.addWidget(self.logo)
        self.title_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_title.setFont(font)
        self.title_title.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.title_title.setTextFormat(QtCore.Qt.RichText)
        self.title_title.setAlignment(QtCore.Qt.AlignCenter)
        self.title_title.setWordWrap(True)
        self.title_title.setObjectName("title_title")
        self.sidebar.addWidget(self.title_title)
        self.title_selection = QtWidgets.QVBoxLayout()
        self.title_selection.setSpacing(0)
        self.title_selection.setObjectName("title_selection")
        self.title_home = QtWidgets.QHBoxLayout()
        self.title_home.setContentsMargins(-1, -1, 0, -1)
        self.title_home.setSpacing(0)
        self.title_home.setObjectName("title_home")
        self.title_home_img = ClickableLabel(Dialog)
        self.title_home_img.setMinimumSize(QtCore.QSize(0, 0))
        self.title_home_img.setMouseTracking(False)
        self.title_home_img.setAutoFillBackground(False)
        self.title_home_img.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_home_img.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title_home_img.setText("")
        self.title_home_img.setPixmap(QtGui.QPixmap("Image/Register/house.png"))
        self.title_home_img.setScaledContents(False)
        self.title_home_img.setAlignment(QtCore.Qt.AlignCenter)
        self.title_home_img.setObjectName("title_home_img")
        self.title_home.addWidget(self.title_home_img)
        self.title_home_text = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_home_text.setFont(font)
        self.title_home_text.setMouseTracking(True)
        self.title_home_text.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_home_text.setScaledContents(False)
        self.title_home_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_home_text.setObjectName("title_home_text")
        self.title_home.addWidget(self.title_home_text)
        self.title_home.setStretch(0, 40)
        self.title_home.setStretch(1, 60)
        self.title_selection.addLayout(self.title_home)
        self.title_info = QtWidgets.QHBoxLayout()
        self.title_info.setSpacing(0)
        self.title_info.setObjectName("title_info")
        self.title_info_img = ClickableLabel(Dialog)
        self.title_info_img.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_info_img.setText("")
        self.title_info_img.setPixmap(QtGui.QPixmap("Image/Register/User Manual.png"))
        self.title_info_img.setAlignment(QtCore.Qt.AlignCenter)
        self.title_info_img.setObjectName("title_info_img")
        self.title_info.addWidget(self.title_info_img)
        self.title_info_text = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_info_text.setFont(font)
        self.title_info_text.setMouseTracking(True)
        self.title_info_text.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_info_text.setScaledContents(False)
        self.title_info_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_info_text.setObjectName("title_info_text")
        self.title_info.addWidget(self.title_info_text)
        self.title_info.setStretch(0, 40)
        self.title_info.setStretch(1, 60)
        self.title_selection.addLayout(self.title_info)
        self.title_record = QtWidgets.QHBoxLayout()
        self.title_record.setSpacing(0)
        self.title_record.setObjectName("title_record")
        self.title_record_img = ClickableLabel(Dialog)
        self.title_record_img.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_record_img.setText("")
        self.title_record_img.setPixmap(QtGui.QPixmap("Image/Register/search.png"))
        self.title_record_img.setAlignment(QtCore.Qt.AlignCenter)
        self.title_record_img.setObjectName("title_record_img")
        self.title_record.addWidget(self.title_record_img)
        self.title_record_text = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_record_text.setFont(font)
        self.title_record_text.setMouseTracking(True)
        self.title_record_text.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_record_text.setScaledContents(False)
        self.title_record_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_record_text.setObjectName("title_record_text")
        self.title_record.addWidget(self.title_record_text)
        self.title_record.setStretch(0, 40)
        self.title_record.setStretch(1, 60)
        self.title_selection.addLayout(self.title_record)
        self.title_upload = QtWidgets.QHBoxLayout()
        self.title_upload.setSpacing(0)
        self.title_upload.setObjectName("title_upload")
        self.title_upload_img = ClickableLabel(Dialog)
        self.title_upload_img.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_upload_img.setText("")
        self.title_upload_img.setPixmap(QtGui.QPixmap("Image/Register/download.png"))
        self.title_upload_img.setAlignment(QtCore.Qt.AlignCenter)
        self.title_upload_img.setObjectName("title_upload_img")
        self.title_upload.addWidget(self.title_upload_img)
        self.title_upload_text = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_upload_text.setFont(font)
        self.title_upload_text.setMouseTracking(True)
        self.title_upload_text.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title_upload_text.setScaledContents(False)
        self.title_upload_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_upload_text.setObjectName("title_upload_text")
        self.title_upload.addWidget(self.title_upload_text)
        self.title_upload.setStretch(0, 40)
        self.title_upload.setStretch(1, 60)
        self.title_selection.addLayout(self.title_upload)
        self.sidebar.addLayout(self.title_selection)
        self.about_us = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.about_us.setFont(font)
        self.about_us.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"padding-right: 8px;")
        self.about_us.setTextFormat(QtCore.Qt.RichText)
        self.about_us.setWordWrap(True)
        self.about_us.setIndent(10)
        self.about_us.setObjectName("about_us")
        self.sidebar.addWidget(self.about_us)
        self.sidebar.setStretch(0, 25)
        self.sidebar.setStretch(1, 5)
        self.sidebar.setStretch(2, 40)
        self.sidebar.setStretch(3, 30)
        self.horizontalLayout_2.addLayout(self.sidebar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, 100, 100, 100)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.login_title.setWordWrap(False)
        self.login_title.setObjectName("login_title")
        self.verticalLayout.addWidget(self.login_title)
        self.login_error = QtWidgets.QLabel(Dialog)
        self.login_error.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.login_error.setObjectName("login_error")
        self.verticalLayout.addWidget(self.login_error)
        self.login_email = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_email.setFont(font)
        self.login_email.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_email.setObjectName("login_email")
        self.verticalLayout.addWidget(self.login_email)
        self.login_email_text = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_email_text.setFont(font)
        self.login_email_text.setInputMask("")
        self.login_email_text.setText("")
        self.login_email_text.setObjectName("login_email_text")
        self.verticalLayout.addWidget(self.login_email_text)
        self.login_password = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_password.setFont(font)
        self.login_password.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_password.setObjectName("login_password")
        self.verticalLayout.addWidget(self.login_password)
        self.login_password_text = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_password_text.setFont(font)
        self.login_password_text.setText("")
        self.login_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_text.setObjectName("login_password_text")
        self.verticalLayout.addWidget(self.login_password_text)
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
        self.login_forget.setFont(font)
        self.login_forget.setAcceptDrops(False)
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
        self.signup_link.setFont(font)
        self.signup_link.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.signup_link.setOpenExternalLinks(True)
        self.signup_link.setObjectName("signup_link")
        self.horizontalLayout.addWidget(self.signup_link)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.title_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">INTELLIGENT AUTOMATED CROPS <br/>MONITORING SYSTEM</span></p></body></html>"))
        self.title_home_text.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Home</span></p></body></html>"))
        self.title_info_text.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">How it works?</span></p></body></html>"))
        self.title_record_text.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Past Records</span></p></body></html>"))
        self.title_upload_text.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Data Upload</span></p></body></html>"))
        self.about_us.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">About Us</span></p><p><span style=\" color:#ffffff;\">Our project aims to automated the monitoring of crops using camera and image recognition. In our system, users will be notified about the type of pests on the crops and the recommended solution as soon as possible and this enables early detection and reduce losses!</span></p></body></html>"))
        self.login_title.setText(_translate("Dialog", "Hi, Welcome Back! ????"))
        self.login_error.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">Please login first</span></p></body></html>"))
        self.login_email.setText(_translate("Dialog", "Email / Username"))
        self.login_email_text.setPlaceholderText(_translate("Dialog", "Username"))
        self.login_password.setText(_translate("Dialog", "Password"))
        self.login_password_text.setPlaceholderText(_translate("Dialog", "Enter Your Password"))
        self.login_remember.setText(_translate("Dialog", "    Remember me"))
        self.login_forget.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline; color:#5500ff;\">Forget Password</span></p></body></html>"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_title.setText(_translate("Dialog", "<html><head/><body><p>Don\'t have an account yet? </p></body></html>"))
        self.signup_link.setText(_translate("Dialog", "<html><head/><body><p><a href=\"localhost:8000\"><span style=\" text-decoration: underline; color:#0000ff;\"> Sign up here!</span></a></p></body></html>"))
from clickablelabel import ClickableLabel
