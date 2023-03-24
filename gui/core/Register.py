from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import QUrl, QDesktopServices
from core import PageWindow
import os
import sys
import re
import sqlite3

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
SIGNUP_URL = "http://192.168.100.43:8000/create-account/"

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CURRENT_DIR)
DB_PATH = os.path.join(CURRENT_DIR, "db.sqlite3")
sys.path.insert(0, BASE_DIR)

from ui import Register

class WindowRegister(PageWindow.PageWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Register.Ui_Dialog()
        self.ui.setupUi(self)
        self.sidebar()

        self.con = sqlite3.connect(DB_PATH)

        self.ui.sidebar_home.setEnabled(False)
        self.ui.sidebar_record.setEnabled(False)
        self.ui.sidebar_logout.setEnabled(False)

        self.view_icon = QtGui.QPixmap("Image\Register\\view.png")
        self.hidden_icon = QtGui.QPixmap("Image\Register\\hidden.png")

        self.ui.login_btn.clicked.connect(self.login)
        self.ui.login_password_text.returnPressed.connect(self.login)
        self.ui.signup_link.clicked.connect(self.signup)
        self.ui.show_password.clicked.connect(self.showPassword)

    def login(self):
        cur = self.con.cursor()

        user = self.ui.login_email_text.text()
        password = self.ui.login_password_text.text()

        if re.match(EMAIL_REGEX, user):
            password_from_db = cur.execute(f"SELECT password1 FROM web_user WHERE email='{user}'").fetchone()
        else:
            password_from_db = cur.execute(f"SELECT password1 FROM web_user WHERE username='{user}'").fetchone()

        if password_from_db and password == password_from_db[0]:
            self.homeClicked()
        else:
            pass

    def signup(self):
        url = QUrl(SIGNUP_URL)
        QDesktopServices.openUrl(url)

    def showPassword(self):
        if self.ui.show_password.pixmap().cacheKey() == self.hidden_icon.cacheKey():
            self.ui.show_password.setPixmap(self.view_icon)
            self.ui.login_password_text.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.show_password.setPixmap(self.hidden_icon)
            self.ui.login_password_text.setEchoMode(QtWidgets.QLineEdit.Password)