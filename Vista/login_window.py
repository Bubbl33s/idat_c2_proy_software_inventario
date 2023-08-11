from PyQt5 import uic, QtWidgets
from vista.inventarista_window import IventaristaWindow


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        uic.loadUi("ui/login_window.ui", self)
        self.show()

        self.btn_login.clicked.connect(self.switch_to_inv_window)

    def switch_to_inv_window(self):
        self.window = IventaristaWindow()
        self.window.show()
        self.close()
