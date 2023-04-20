from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QImage
from core import PageWindow
import os
import sys
from core.clickableLabel import ClickableLabel

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, BASE_DIR)

from ui import Record

class WindowRecord(PageWindow.PageWindow):
    def __init__(self, con, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Record.Ui_Dialog()
        self.ui.setupUi(self)
        self.sidebar()

        self.setupLogoutMsgBox()
        self.con = con
        self.current_table = 0

        self.ui.sidebar_logout.clicked.connect(self.logout)
        self.ui.sidebar_logout.clicked.connect(self.logout)
        self.ui.record_search_btn.clicked.connect(self.search)
        self.ui.record_search.returnPressed.connect(self.search)
        self.ui.table_combobox.currentIndexChanged.connect(self.changeTable)

        self.data = self.con.execute("SELECT * FROM web_pest").fetchall()

        self.ui.table.setColumnWidth(0, 200)
        self.ui.table.setColumnWidth(1, 200)
        self.ui.table.setColumnWidth(2, 200)
        self.ui.table.setColumnWidth(3, 200)

        self.updateTable()
        self.startTimer()

    def updateTable(self):
        self.ui.table.setRowCount(len(self.data))

        for n, i in enumerate(self.data):
            image_item = self.getImageLabel(i[-3])
            time_item = QtWidgets.QTableWidgetItem(f"{i[-2]}\n{i[-1][:-7]}")
            item = QtWidgets.QTableWidgetItem(i[1].replace(",", "\n"))
            location_item = QtWidgets.QTableWidgetItem(i[2])

            self.ui.table.setCellWidget(n, 0, image_item)
            self.ui.table.setItem(n, 1, time_item)
            self.ui.table.setItem(n, 2, item)
            self.ui.table.setItem(n, 3, location_item)

        self.ui.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.table.resizeRowsToContents()

    def getImageLabel(self, image):
        image_label = ClickableLabel(self)
        image_label.setText("")
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        pixmap = pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        image_label.clicked.connect(lambda: self.showFullImage(image))
        return image_label

    def showFullImage(self, image):
        dialog = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        label.setPixmap(pixmap)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.setWindowTitle("image")
        dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        dialog.exec_()

    def checkUpdate(self):
        if self.current_table == 0:
            updated_data = self.con.execute("SELECT * FROM web_pest").fetchall()
        elif self.current_table == 1:
            updated_data = self.con.execute("SELECT * FROM web_disease").fetchall()
        if updated_data != self.data:
            self.data = updated_data
            self.updateTable()

    def startTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkUpdate)
        self.timer.start(2000)

    def stopTimer(self):
        self.timer.stop()

    def search(self):
        search_text = self.ui.record_search.text()
        results = list(filter(lambda x: search_text in x[1], self.data))
        self.updateTable(results)

    def changeTable(self, index):
        self.current_table = index
        if index == 0:
            self.ui.record_title.setText("Pest Record")
            self.data = self.con.execute("SELECT * FROM web_pest").fetchall()
        elif index == 1:
            self.ui.record_title.setText("Disease Record")
            self.data = self.con.execute("SELECT * FROM web_disease").fetchall()
        self.updateTable()
