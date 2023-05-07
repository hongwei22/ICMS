# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1221, 855)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = ClickableLabel(Form)
        self.logo.setEnabled(True)
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("./src/img/register/ICMS.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.sidebar_home = ClickableLabel(Form)
        self.sidebar_home.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar_home.setMouseTracking(False)
        self.sidebar_home.setAutoFillBackground(False)
        self.sidebar_home.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar_home.setText("")
        self.sidebar_home.setPixmap(QtGui.QPixmap("./src/img/register/home.png"))
        self.sidebar_home.setScaledContents(False)
        self.sidebar_home.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_home.setObjectName("sidebar_home")
        self.verticalLayout_2.addWidget(self.sidebar_home)
        self.sidebar_camera = ClickableLabel(Form)
        self.sidebar_camera.setStyleSheet("background-color: rgb(0,0,0)")
        self.sidebar_camera.setText("")
        self.sidebar_camera.setPixmap(QtGui.QPixmap("./src/img/register/camera.png"))
        self.sidebar_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_camera.setObjectName("sidebar_camera")
        self.verticalLayout_2.addWidget(self.sidebar_camera)
        self.sidebar_record = ClickableLabel(Form)
        self.sidebar_record.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_record.setText("")
        self.sidebar_record.setPixmap(QtGui.QPixmap("./src/img/register/search.png"))
        self.sidebar_record.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_record.setObjectName("sidebar_record")
        self.verticalLayout_2.addWidget(self.sidebar_record)
        self.sidebar_logout = ClickableLabel(Form)
        self.sidebar_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sidebar_logout.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sidebar_logout.setText("")
        self.sidebar_logout.setPixmap(QtGui.QPixmap("./src/img/register/exit.png"))
        self.sidebar_logout.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_logout.setObjectName("sidebar_logout")
        self.verticalLayout_2.addWidget(self.sidebar_logout)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 10, 10, 10)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_label.setWordWrap(True)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_3.addWidget(self.title_label)
        self.description_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.verticalLayout_3.addWidget(self.description_label)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet("border: none; background-color: white; border-radius: 5px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pest_num_label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pest_num_label.setFont(font)
        self.pest_num_label.setScaledContents(True)
        self.pest_num_label.setWordWrap(True)
        self.pest_num_label.setObjectName("pest_num_label")
        self.horizontalLayout_6.addWidget(self.pest_num_label)
        self.pest_image = QtWidgets.QLabel(self.widget_5)
        self.pest_image.setText("")
        self.pest_image.setPixmap(QtGui.QPixmap("./src/img/home/bug.png"))
        self.pest_image.setObjectName("pest_image")
        self.horizontalLayout_6.addWidget(self.pest_image)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.pest_number = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pest_number.setFont(font)
        self.pest_number.setStyleSheet("border: none;")
        self.pest_number.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pest_number.setObjectName("pest_number")
        self.verticalLayout_5.addWidget(self.pest_number)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("border: none; background-color: white; border-radius: 5px;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.disease_num_label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.disease_num_label.setFont(font)
        self.disease_num_label.setScaledContents(True)
        self.disease_num_label.setWordWrap(True)
        self.disease_num_label.setObjectName("disease_num_label")
        self.horizontalLayout_7.addWidget(self.disease_num_label)
        self.disease_image = QtWidgets.QLabel(self.widget_6)
        self.disease_image.setText("")
        self.disease_image.setPixmap(QtGui.QPixmap("./src/img/home/virus.png"))
        self.disease_image.setObjectName("disease_image")
        self.horizontalLayout_7.addWidget(self.disease_image)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.disease_number = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.disease_number.setFont(font)
        self.disease_number.setStyleSheet("border: none;")
        self.disease_number.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.disease_number.setObjectName("disease_number")
        self.verticalLayout_7.addWidget(self.disease_number)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 2)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.today_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.today_button.setFont(font)
        self.today_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.today_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #c5c5c5;\n"
"}")
        self.today_button.setCheckable(True)
        self.today_button.setChecked(True)
        self.today_button.setObjectName("today_button")
        self.horizontalLayout_2.addWidget(self.today_button)
        self.week_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.week_button.setFont(font)
        self.week_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.week_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #c5c5c5;\n"
"}")
        self.week_button.setCheckable(True)
        self.week_button.setObjectName("week_button")
        self.horizontalLayout_2.addWidget(self.week_button)
        self.month_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.month_button.setFont(font)
        self.month_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.month_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #c5c5c5;\n"
"}")
        self.month_button.setCheckable(True)
        self.month_button.setChecked(False)
        self.month_button.setObjectName("month_button")
        self.horizontalLayout_2.addWidget(self.month_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.frame_5 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("border:none; background-color: white; border-radius: 5px")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        self.date_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout.addWidget(self.date_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.location_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.location_label.setFont(font)
        self.location_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.location_label.setObjectName("location_label")
        self.verticalLayout_4.addWidget(self.location_label)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.detected_pest_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detected_pest_label.setFont(font)
        self.detected_pest_label.setObjectName("detected_pest_label")
        self.verticalLayout.addWidget(self.detected_pest_label)
        self.pest_chart = QChartView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pest_chart.sizePolicy().hasHeightForWidth())
        self.pest_chart.setSizePolicy(sizePolicy)
        self.pest_chart.setStyleSheet("border: none; border-radius: 5px")
        self.pest_chart.setObjectName("pest_chart")
        self.verticalLayout.addWidget(self.pest_chart)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.detected_disease_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detected_disease_label.setFont(font)
        self.detected_disease_label.setObjectName("detected_disease_label")
        self.verticalLayout_6.addWidget(self.detected_disease_label)
        self.disease_chart = QChartView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disease_chart.sizePolicy().hasHeightForWidth())
        self.disease_chart.setSizePolicy(sizePolicy)
        self.disease_chart.setStyleSheet("border: none; border-radius: 5px")
        self.disease_chart.setObjectName("disease_chart")
        self.verticalLayout_6.addWidget(self.disease_chart)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Home"))
        self.title_label.setText(_translate("Form", "Monitor Your Crops"))
        self.description_label.setText(_translate("Form", "Observe and analyse your crop health"))
        self.pest_num_label.setText(_translate("Form", "Number of Pests"))
        self.pest_number.setText(_translate("Form", "0"))
        self.disease_num_label.setText(_translate("Form", "Number of Disease"))
        self.disease_number.setText(_translate("Form", "0"))
        self.today_button.setText(_translate("Form", "Today"))
        self.week_button.setText(_translate("Form", "Week"))
        self.month_button.setText(_translate("Form", "Month"))
        self.time_label.setText(_translate("Form", "11:11:11"))
        self.date_label.setText(_translate("Form", "11/11/11"))
        self.location_label.setText(_translate("Form", "Location"))
        self.detected_pest_label.setText(_translate("Form", "Detected Pests"))
        self.detected_disease_label.setText(_translate("Form", "Detected Disease"))
from core.clickableLabel import ClickableLabel
