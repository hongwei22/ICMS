# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
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
        Dialog.resize(1425, 856)
        Dialog.setAcceptDrops(False)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
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
        self.horizontalLayout_6.addLayout(self.sidebar)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(100, -1, 50, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.user_title.setFont(font)
        self.user_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_title.setObjectName("user_title")
        self.horizontalLayout.addWidget(self.user_title)
        self.user_profile = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_profile.setFont(font)
        self.user_profile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_profile.setObjectName("user_profile")
        self.horizontalLayout.addWidget(self.user_profile)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_add = ClickableLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_add.setFont(font)
        self.user_add.setStyleSheet("border: 2px solid black")
        self.user_add.setObjectName("user_add")
        self.horizontalLayout_2.addWidget(self.user_add)
        self.user_filtered = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_filtered.setFont(font)
        self.user_filtered.setAlignment(QtCore.Qt.AlignCenter)
        self.user_filtered.setObjectName("user_filtered")
        self.horizontalLayout_2.addWidget(self.user_filtered)
        self.user_search_btn = ClickableLabel(Dialog)
        self.user_search_btn.setText("")
        self.user_search_btn.setPixmap(QtGui.QPixmap("Image/User/search.png"))
        self.user_search_btn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_search_btn.setObjectName("user_search_btn")
        self.horizontalLayout_2.addWidget(self.user_search_btn)
        self.user_search = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_search.setFont(font)
        self.user_search.setObjectName("user_search")
        self.horizontalLayout_2.addWidget(self.user_search)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.user_pest_down = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest_down.setFont(font)
        self.user_pest_down.setStyleSheet("border: 2px solid black")
        self.user_pest_down.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest_down.setObjectName("user_pest_down")
        self.horizontalLayout_5.addWidget(self.user_pest_down)
        self.user_pest_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest_title.setFont(font)
        self.user_pest_title.setStyleSheet("border: 2px solid black")
        self.user_pest_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest_title.setObjectName("user_pest_title")
        self.horizontalLayout_5.addWidget(self.user_pest_title)
        self.user_host_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host_title.setFont(font)
        self.user_host_title.setStyleSheet("border: 2px solid black")
        self.user_host_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host_title.setObjectName("user_host_title")
        self.horizontalLayout_5.addWidget(self.user_host_title)
        self.user_total_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total_title.setFont(font)
        self.user_total_title.setStyleSheet("border: 2px solid black")
        self.user_total_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total_title.setObjectName("user_total_title")
        self.horizontalLayout_5.addWidget(self.user_total_title)
        self.user_date_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date_title.setFont(font)
        self.user_date_title.setStyleSheet("border: 2px solid black")
        self.user_date_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date_title.setObjectName("user_date_title")
        self.horizontalLayout_5.addWidget(self.user_date_title)
        self.user_trash_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_trash_title.setFont(font)
        self.user_trash_title.setStyleSheet("border: 2px solid black")
        self.user_trash_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash_title.setObjectName("user_trash_title")
        self.horizontalLayout_5.addWidget(self.user_trash_title)
        self.user_edit_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_edit_title.setFont(font)
        self.user_edit_title.setStyleSheet("border: 2px solid black")
        self.user_edit_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit_title.setObjectName("user_edit_title")
        self.horizontalLayout_5.addWidget(self.user_edit_title)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 967, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.user_img1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.user_img1.setStyleSheet("border: 2px solid black")
        self.user_img1.setText("")
        self.user_img1.setPixmap(QtGui.QPixmap("Image/User/Pest1.png"))
        self.user_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_img1.setObjectName("user_img1")
        self.verticalLayout_2.addWidget(self.user_img1)
        self.user_img2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.user_img2.setStyleSheet("border: 2px solid black")
        self.user_img2.setText("")
        self.user_img2.setPixmap(QtGui.QPixmap("Image/User/Pest2.png"))
        self.user_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_img2.setObjectName("user_img2")
        self.verticalLayout_2.addWidget(self.user_img2)
        self.user_img3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.user_img3.setStyleSheet("border: 2px solid black")
        self.user_img3.setText("")
        self.user_img3.setPixmap(QtGui.QPixmap("Image/User/Pest1.png"))
        self.user_img3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_img3.setObjectName("user_img3")
        self.verticalLayout_2.addWidget(self.user_img3)
        self.user_img4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.user_img4.setStyleSheet("border: 2px solid black")
        self.user_img4.setText("")
        self.user_img4.setPixmap(QtGui.QPixmap("Image/User/Pest1.png"))
        self.user_img4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_img4.setObjectName("user_img4")
        self.verticalLayout_2.addWidget(self.user_img4)
        self.user_img5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.user_img5.setStyleSheet("border: 2px solid black")
        self.user_img5.setText("")
        self.user_img5.setPixmap(QtGui.QPixmap("Image/User/Pest1.png"))
        self.user_img5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_img5.setObjectName("user_img5")
        self.verticalLayout_2.addWidget(self.user_img5)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.user_pest1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest1.setFont(font)
        self.user_pest1.setStyleSheet("border: 2px solid black")
        self.user_pest1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest1.setObjectName("user_pest1")
        self.verticalLayout_3.addWidget(self.user_pest1)
        self.user_pest2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest2.setFont(font)
        self.user_pest2.setStyleSheet("border: 2px solid black")
        self.user_pest2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest2.setObjectName("user_pest2")
        self.verticalLayout_3.addWidget(self.user_pest2)
        self.user_pest3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest3.setFont(font)
        self.user_pest3.setStyleSheet("border: 2px solid black")
        self.user_pest3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest3.setObjectName("user_pest3")
        self.verticalLayout_3.addWidget(self.user_pest3)
        self.user_pest4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest4.setFont(font)
        self.user_pest4.setStyleSheet("border: 2px solid black")
        self.user_pest4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest4.setObjectName("user_pest4")
        self.verticalLayout_3.addWidget(self.user_pest4)
        self.user_pest5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_pest5.setFont(font)
        self.user_pest5.setStyleSheet("border: 2px solid black")
        self.user_pest5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pest5.setObjectName("user_pest5")
        self.verticalLayout_3.addWidget(self.user_pest5)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.user_host1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host1.setFont(font)
        self.user_host1.setStyleSheet("border: 2px solid black")
        self.user_host1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host1.setObjectName("user_host1")
        self.verticalLayout_4.addWidget(self.user_host1)
        self.user_host2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host2.setFont(font)
        self.user_host2.setStyleSheet("border: 2px solid black")
        self.user_host2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host2.setObjectName("user_host2")
        self.verticalLayout_4.addWidget(self.user_host2)
        self.user_host3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host3.setFont(font)
        self.user_host3.setStyleSheet("border: 2px solid black")
        self.user_host3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host3.setObjectName("user_host3")
        self.verticalLayout_4.addWidget(self.user_host3)
        self.user_host4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host4.setFont(font)
        self.user_host4.setStyleSheet("border: 2px solid black")
        self.user_host4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host4.setObjectName("user_host4")
        self.verticalLayout_4.addWidget(self.user_host4)
        self.user_host5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_host5.setFont(font)
        self.user_host5.setStyleSheet("border: 2px solid black")
        self.user_host5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_host5.setObjectName("user_host5")
        self.verticalLayout_4.addWidget(self.user_host5)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.user_total1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total1.setFont(font)
        self.user_total1.setStyleSheet("border: 2px solid black")
        self.user_total1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total1.setObjectName("user_total1")
        self.verticalLayout_5.addWidget(self.user_total1)
        self.user_total2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total2.setFont(font)
        self.user_total2.setStyleSheet("border: 2px solid black")
        self.user_total2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total2.setObjectName("user_total2")
        self.verticalLayout_5.addWidget(self.user_total2)
        self.user_total3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total3.setFont(font)
        self.user_total3.setStyleSheet("border: 2px solid black")
        self.user_total3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total3.setObjectName("user_total3")
        self.verticalLayout_5.addWidget(self.user_total3)
        self.user_total4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total4.setFont(font)
        self.user_total4.setStyleSheet("border: 2px solid black")
        self.user_total4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total4.setObjectName("user_total4")
        self.verticalLayout_5.addWidget(self.user_total4)
        self.user_total5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_total5.setFont(font)
        self.user_total5.setStyleSheet("border: 2px solid black")
        self.user_total5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_total5.setObjectName("user_total5")
        self.verticalLayout_5.addWidget(self.user_total5)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 2)
        self.verticalLayout_5.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.user_date1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date1.setFont(font)
        self.user_date1.setStyleSheet("border: 2px solid black")
        self.user_date1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date1.setObjectName("user_date1")
        self.verticalLayout_6.addWidget(self.user_date1)
        self.user_date2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date2.setFont(font)
        self.user_date2.setStyleSheet("border: 2px solid black")
        self.user_date2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date2.setObjectName("user_date2")
        self.verticalLayout_6.addWidget(self.user_date2)
        self.user_date3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date3.setFont(font)
        self.user_date3.setStyleSheet("border: 2px solid black")
        self.user_date3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date3.setObjectName("user_date3")
        self.verticalLayout_6.addWidget(self.user_date3)
        self.user_date4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date4.setFont(font)
        self.user_date4.setStyleSheet("border: 2px solid black")
        self.user_date4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date4.setObjectName("user_date4")
        self.verticalLayout_6.addWidget(self.user_date4)
        self.user_date5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_date5.setFont(font)
        self.user_date5.setStyleSheet("border: 2px solid black")
        self.user_date5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_date5.setObjectName("user_date5")
        self.verticalLayout_6.addWidget(self.user_date5)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 2)
        self.verticalLayout_6.setStretch(3, 2)
        self.verticalLayout_6.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.user_trash1 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_trash1.setStyleSheet("border: 2px solid black")
        self.user_trash1.setText("")
        self.user_trash1.setPixmap(QtGui.QPixmap("Image/User/Trash.png"))
        self.user_trash1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash1.setObjectName("user_trash1")
        self.verticalLayout_7.addWidget(self.user_trash1)
        self.user_trash2 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_trash2.setStyleSheet("border: 2px solid black")
        self.user_trash2.setText("")
        self.user_trash2.setPixmap(QtGui.QPixmap("Image/User/Trash.png"))
        self.user_trash2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash2.setObjectName("user_trash2")
        self.verticalLayout_7.addWidget(self.user_trash2)
        self.user_trash3 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_trash3.setStyleSheet("border: 2px solid black")
        self.user_trash3.setText("")
        self.user_trash3.setPixmap(QtGui.QPixmap("Image/User/Trash.png"))
        self.user_trash3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash3.setObjectName("user_trash3")
        self.verticalLayout_7.addWidget(self.user_trash3)
        self.user_trash4 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_trash4.setStyleSheet("border: 2px solid black")
        self.user_trash4.setText("")
        self.user_trash4.setPixmap(QtGui.QPixmap("Image/User/Trash.png"))
        self.user_trash4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash4.setObjectName("user_trash4")
        self.verticalLayout_7.addWidget(self.user_trash4)
        self.user_trash5 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_trash5.setStyleSheet("border: 2px solid black")
        self.user_trash5.setText("")
        self.user_trash5.setPixmap(QtGui.QPixmap("Image/User/Trash.png"))
        self.user_trash5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_trash5.setObjectName("user_trash5")
        self.verticalLayout_7.addWidget(self.user_trash5)
        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(3, 2)
        self.verticalLayout_7.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.user_edit1 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_edit1.setStyleSheet("border: 2px solid black")
        self.user_edit1.setText("")
        self.user_edit1.setPixmap(QtGui.QPixmap("Image/User/edit.png"))
        self.user_edit1.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit1.setObjectName("user_edit1")
        self.verticalLayout_8.addWidget(self.user_edit1)
        self.user_edit2 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_edit2.setStyleSheet("border: 2px solid black")
        self.user_edit2.setText("")
        self.user_edit2.setPixmap(QtGui.QPixmap("Image/User/edit.png"))
        self.user_edit2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit2.setObjectName("user_edit2")
        self.verticalLayout_8.addWidget(self.user_edit2)
        self.user_edit3 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_edit3.setStyleSheet("border: 2px solid black")
        self.user_edit3.setText("")
        self.user_edit3.setPixmap(QtGui.QPixmap("Image/User/edit.png"))
        self.user_edit3.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit3.setObjectName("user_edit3")
        self.verticalLayout_8.addWidget(self.user_edit3)
        self.user_edit4 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_edit4.setStyleSheet("border: 2px solid black")
        self.user_edit4.setText("")
        self.user_edit4.setPixmap(QtGui.QPixmap("Image/User/edit.png"))
        self.user_edit4.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit4.setObjectName("user_edit4")
        self.verticalLayout_8.addWidget(self.user_edit4)
        self.user_edit5 = ClickableLabel(self.scrollAreaWidgetContents)
        self.user_edit5.setStyleSheet("border: 2px solid black")
        self.user_edit5.setText("")
        self.user_edit5.setPixmap(QtGui.QPixmap("Image/User/edit.png"))
        self.user_edit5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edit5.setObjectName("user_edit5")
        self.verticalLayout_8.addWidget(self.user_edit5)
        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_8.setStretch(3, 2)
        self.verticalLayout_8.setStretch(4, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout_9.setStretch(3, 10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

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
        self.user_title.setText(_translate("Dialog", "Hello, John"))
        self.user_profile.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline; color:#5500ff;\">Logout?</span></p></body></html>"))
        self.user_add.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#000000;\">+ Add Pest </span></p></body></html>"))
        self.user_filtered.setText(_translate("Dialog", "Occurence of pests"))
        self.user_search.setPlaceholderText(_translate("Dialog", "Search"))
        self.user_pest_down.setText(_translate("Dialog", "Image"))
        self.user_pest_title.setText(_translate("Dialog", "Pest"))
        self.user_host_title.setText(_translate("Dialog", "Host"))
        self.user_total_title.setText(_translate("Dialog", "Apperance"))
        self.user_date_title.setText(_translate("Dialog", "Date"))
        self.user_trash_title.setText(_translate("Dialog", "Delete"))
        self.user_edit_title.setText(_translate("Dialog", "Edit"))
        self.user_pest1.setText(_translate("Dialog", "Aphids"))
        self.user_pest2.setText(_translate("Dialog", "Grasshopper"))
        self.user_pest3.setText(_translate("Dialog", "Aphids"))
        self.user_pest4.setText(_translate("Dialog", "Aphids"))
        self.user_pest5.setText(_translate("Dialog", "Aphids"))
        self.user_host1.setText(_translate("Dialog", "Aphelandra"))
        self.user_host2.setText(_translate("Dialog", "Cucumber"))
        self.user_host3.setText(_translate("Dialog", "Aphelandra"))
        self.user_host4.setText(_translate("Dialog", "Aphelandra"))
        self.user_host5.setText(_translate("Dialog", "Aphelandra"))
        self.user_total1.setText(_translate("Dialog", "5"))
        self.user_total2.setText(_translate("Dialog", "2"))
        self.user_total3.setText(_translate("Dialog", "5"))
        self.user_total4.setText(_translate("Dialog", "5"))
        self.user_total5.setText(_translate("Dialog", "5"))
        self.user_date1.setText(_translate("Dialog", "26/12/2022"))
        self.user_date2.setText(_translate("Dialog", "26/12/2022"))
        self.user_date3.setText(_translate("Dialog", "26/12/2022"))
        self.user_date4.setText(_translate("Dialog", "26/12/2022"))
        self.user_date5.setText(_translate("Dialog", "26/12/2022"))
from clickablelabel import ClickableLabel
