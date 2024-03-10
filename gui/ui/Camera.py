# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\Camera.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(1222, 855)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camera_video = QtWidgets.QLabel(Dialog)
        self.camera_video.setText("")
        self.camera_video.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_video.setObjectName("camera_video")
        self.horizontalLayout_2.addWidget(self.camera_video)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.camera_capture = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.camera_capture.setFont(font)
        self.camera_capture.setObjectName("camera_capture")
        self.verticalLayout_3.addWidget(self.camera_capture)
        self.camera_real = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.camera_real.setFont(font)
        self.camera_real.setObjectName("camera_real")
        self.verticalLayout_3.addWidget(self.camera_real)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.setStretch(0, 3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.camera_capture.setText(_translate("Dialog", "Capture"))
        self.camera_real.setText(_translate("Dialog", "Real Time"))
from core.clickableLabel import ClickableLabel
