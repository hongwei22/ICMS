# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\UM\Year 3\Sem 2\KIX3001\ICMS\gui\src\Upload.ui'
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
        Dialog.resize(1146, 721)
        Dialog.setAcceptDrops(False)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logo = ClickableLabel(Dialog)
        self.logo.setEnabled(True)
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Image/Register/ICMS.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_3.addWidget(self.logo)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.sidebar_home = ClickableLabel(Dialog)
        self.sidebar_home.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar_home.setMouseTracking(False)
        self.sidebar_home.setAutoFillBackground(False)
        self.sidebar_home.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar_home.setText("")
        self.sidebar_home.setPixmap(QtGui.QPixmap("Image/Register/home.png"))
        self.sidebar_home.setScaledContents(False)
        self.sidebar_home.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_home.setObjectName("sidebar_home")
        self.verticalLayout_3.addWidget(self.sidebar_home)
        self.sidebar_record = ClickableLabel(Dialog)
        self.sidebar_record.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_record.setText("")
        self.sidebar_record.setPixmap(QtGui.QPixmap("Image/Register/search.png"))
        self.sidebar_record.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_record.setObjectName("sidebar_record")
        self.verticalLayout_3.addWidget(self.sidebar_record)
        self.sidebar_logout = ClickableLabel(Dialog)
        self.sidebar_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sidebar_logout.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_logout.setText("")
        self.sidebar_logout.setPixmap(QtGui.QPixmap("Image/Register/exit.png"))
        self.sidebar_logout.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_logout.setObjectName("sidebar_logout")
        self.verticalLayout_3.addWidget(self.sidebar_logout)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 2)
        self.verticalLayout_3.setStretch(5, 5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.upload_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.upload_title.setFont(font)
        self.upload_title.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_title.setObjectName("upload_title")
        self.verticalLayout_2.addWidget(self.upload_title)
        self.upload_title_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.upload_title_2.setFont(font)
        self.upload_title_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.upload_title_2.setObjectName("upload_title_2")
        self.verticalLayout_2.addWidget(self.upload_title_2)
        self.upload_image = ClickableLabel(Dialog)
        self.upload_image.setText("")
        self.upload_image.setPixmap(QtGui.QPixmap("Image/Upload/Upload.png"))
        self.upload_image.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_image.setObjectName("upload_image")
        self.verticalLayout_2.addWidget(self.upload_image)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload_filename1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filename1.setFont(font)
        self.upload_filename1.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filename1.setObjectName("upload_filename1")
        self.horizontalLayout.addWidget(self.upload_filename1)
        self.upload_filesize1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filesize1.setFont(font)
        self.upload_filesize1.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filesize1.setObjectName("upload_filesize1")
        self.horizontalLayout.addWidget(self.upload_filesize1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.upload_filename2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filename2.setFont(font)
        self.upload_filename2.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filename2.setObjectName("upload_filename2")
        self.horizontalLayout_2.addWidget(self.upload_filename2)
        self.upload_filesize2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filesize2.setFont(font)
        self.upload_filesize2.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filesize2.setObjectName("upload_filesize2")
        self.horizontalLayout_2.addWidget(self.upload_filesize2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.upload_filename3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filename3.setFont(font)
        self.upload_filename3.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filename3.setObjectName("upload_filename3")
        self.horizontalLayout_3.addWidget(self.upload_filename3)
        self.upload_filesize1_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.upload_filesize1_3.setFont(font)
        self.upload_filesize1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_filesize1_3.setObjectName("upload_filesize1_3")
        self.horizontalLayout_3.addWidget(self.upload_filesize1_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.upload_title.setText(_translate("Dialog", "Data Upload"))
        self.upload_title_2.setText(_translate("Dialog", "Local File Upload"))
        self.upload_filename1.setText(_translate("Dialog", "pic1.jpg"))
        self.upload_filesize1.setText(_translate("Dialog", "4MB"))
        self.upload_filename2.setText(_translate("Dialog", "pic2.jpg"))
        self.upload_filesize2.setText(_translate("Dialog", "2MB"))
        self.upload_filename3.setText(_translate("Dialog", "pic3.jpg"))
        self.upload_filesize1_3.setText(_translate("Dialog", "8MB"))
from core.clickableLabel import ClickableLabel
