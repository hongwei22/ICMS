# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
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
        Dialog.resize(1150, 837)
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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 25, -1, -1)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.home_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.home_title.setFont(font)
        self.home_title.setStyleSheet("")
        self.home_title.setAlignment(QtCore.Qt.AlignCenter)
        self.home_title.setObjectName("home_title")
        self.verticalLayout_7.addWidget(self.home_title)
        self.home_news = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.home_news.setFont(font)
        self.home_news.setStyleSheet("padding-left:30px")
        self.home_news.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.home_news.setObjectName("home_news")
        self.verticalLayout_7.addWidget(self.home_news)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 386, 1080))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_img1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_img1.setText("")
        self.home_img1.setPixmap(QtGui.QPixmap("Image/Home/Home1.png"))
        self.home_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.home_img1.setObjectName("home_img1")
        self.horizontalLayout.addWidget(self.home_img1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, -1, 50, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_fav1 = ClickableLabel(self.scrollAreaWidgetContents)
        self.home_fav1.setText("")
        self.home_fav1.setPixmap(QtGui.QPixmap("Image/Home/HomeV.png"))
        self.home_fav1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.home_fav1.setObjectName("home_fav1")
        self.verticalLayout.addWidget(self.home_fav1)
        self.home_info1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_info1.setWordWrap(True)
        self.home_info1.setObjectName("home_info1")
        self.verticalLayout.addWidget(self.home_info1)
        self.home_date1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_date1.setObjectName("home_date1")
        self.verticalLayout.addWidget(self.home_date1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.home_img2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_img2.setText("")
        self.home_img2.setPixmap(QtGui.QPixmap("Image/Home/Home2.png"))
        self.home_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.home_img2.setObjectName("home_img2")
        self.horizontalLayout_2.addWidget(self.home_img2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(15, 0, 50, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_fav2 = ClickableLabel(self.scrollAreaWidgetContents)
        self.home_fav2.setText("")
        self.home_fav2.setPixmap(QtGui.QPixmap("Image/Home/HomeV.png"))
        self.home_fav2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.home_fav2.setObjectName("home_fav2")
        self.verticalLayout_2.addWidget(self.home_fav2)
        self.home_info2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_info2.setWordWrap(True)
        self.home_info2.setObjectName("home_info2")
        self.verticalLayout_2.addWidget(self.home_info2)
        self.home_date2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_date2.setObjectName("home_date2")
        self.verticalLayout_2.addWidget(self.home_date2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.home_img3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_img3.setText("")
        self.home_img3.setPixmap(QtGui.QPixmap("Image/Home/Home3.png"))
        self.home_img3.setAlignment(QtCore.Qt.AlignCenter)
        self.home_img3.setObjectName("home_img3")
        self.horizontalLayout_3.addWidget(self.home_img3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(15, 0, 50, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.home_fav3 = ClickableLabel(self.scrollAreaWidgetContents)
        self.home_fav3.setText("")
        self.home_fav3.setPixmap(QtGui.QPixmap("Image/Home/HomeV.png"))
        self.home_fav3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.home_fav3.setObjectName("home_fav3")
        self.verticalLayout_3.addWidget(self.home_fav3)
        self.home_info3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_info3.setWordWrap(True)
        self.home_info3.setObjectName("home_info3")
        self.verticalLayout_3.addWidget(self.home_info3)
        self.home_date3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_date3.setObjectName("home_date3")
        self.verticalLayout_3.addWidget(self.home_date3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.home_img4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_img4.setText("")
        self.home_img4.setPixmap(QtGui.QPixmap("Image/Home/Home4.png"))
        self.home_img4.setAlignment(QtCore.Qt.AlignCenter)
        self.home_img4.setObjectName("home_img4")
        self.horizontalLayout_4.addWidget(self.home_img4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 0, 50, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.home_fav4 = ClickableLabel(self.scrollAreaWidgetContents)
        self.home_fav4.setText("")
        self.home_fav4.setPixmap(QtGui.QPixmap("Image/Home/HomeV.png"))
        self.home_fav4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.home_fav4.setObjectName("home_fav4")
        self.verticalLayout_4.addWidget(self.home_fav4)
        self.home_info4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_info4.setWordWrap(True)
        self.home_info4.setObjectName("home_info4")
        self.verticalLayout_4.addWidget(self.home_info4)
        self.home_date4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.home_date4.setObjectName("home_date4")
        self.verticalLayout_4.addWidget(self.home_date4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.home_img_side = QtWidgets.QLabel(Dialog)
        self.home_img_side.setText("")
        self.home_img_side.setPixmap(QtGui.QPixmap("Image/Home/HomeSide.png"))
        self.home_img_side.setScaledContents(False)
        self.home_img_side.setObjectName("home_img_side")
        self.verticalLayout_5.addWidget(self.home_img_side)
        self.home_info_side = QtWidgets.QLabel(Dialog)
        self.home_info_side.setWordWrap(True)
        self.home_info_side.setObjectName("home_info_side")
        self.verticalLayout_5.addWidget(self.home_info_side)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 15)

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
        self.home_title.setText(_translate("Dialog", "Pest Appear Alert"))
        self.home_news.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#0000ff;\">Newest pest appear</span></p></body></html>"))
        self.home_info1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aphids<br/></span><span style=\" font-size:10pt;\"><br/>Host: Aphelandra<br/>Solution: Use insecticidal soaps and oils, employ natural predators like ladybugs</span></p></body></html>"))
        self.home_date1.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">09:21 AM 26/12/2022</p></body></html>"))
        self.home_info2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aphids<br/></span><span style=\" font-size:10pt;\"><br/>Host: Aphelandra<br/>Solution: Use insecticidal soaps and oils, employ natural predators like ladybugs</span></p></body></html>"))
        self.home_date2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">09:21 AM 26/12/2022</p></body></html>"))
        self.home_info3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aphids<br/></span><span style=\" font-size:10pt;\"><br/>Host: Aphelandra<br/>Solution: Use insecticidal soaps and oils, employ natural predators like ladybugs</span></p></body></html>"))
        self.home_date3.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">09:21 AM 26/12/2022</p></body></html>"))
        self.home_info4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aphids<br/></span><span style=\" font-size:10pt;\"><br/>Host: Aphelandra<br/>Solution: Use insecticidal soaps and oils, employ natural predators like ladybugs</span></p></body></html>"))
        self.home_date4.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">09:21 AM 26/12/2022</p></body></html>"))
        self.home_info_side.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Grasshopper</span></p><p><span style=\" font-size:10pt;\"><br/>Grasshoppers are a common garden pest that, in large numbers, can devastate entire crops. If grasshoppers are targeting plants in your garden, consider dusting the leaves and stems of those plants with all-purpose flour or kaolin clay, which will stick to the insects’ mouthparts and render them unable to eat.<br/><br/>If your grasshopper numbers are still out of control, you can try Chlorpyrifos + Bifenthrin, or Chlorpyrifos + Zeta-cypermethrin.</span></p></body></html>"))
from clickablelabel import ClickableLabel