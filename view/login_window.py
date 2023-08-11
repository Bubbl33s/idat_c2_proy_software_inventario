from PyQt5 import uic, QtWidgets, QtGui, QtCore
from view.inventarista_window import IventaristaWindow
from controller.querys import get_users_dict
from view.warning_message_box import setted_message_box


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        uic.loadUi("ui/login_window.ui", self)
        self.show()

        self.conteo = 0
        self.admins_dict = {'admx99': 'admx99', 'admz88': 'admz88'}
        self.users_dict = get_users_dict()

        self.btn_login.clicked.connect(self.check_login)

    def switch_to_inv_window(self):
        self.window = IventaristaWindow()
        self.window.show()
        self.close()

    def check_login(self):
        self.login_user = self.txt_user.text().lower()
        self.login_password = self.txt_password.text().lower()

        if self.admins_dict.get(self.login_user) == self.login_password:
            # TODO
            # CAMBIAR A VENTANA DE ADMIN
            pass

        elif self.users_dict.get(self.login_user) == self.login_password:
            self.switch_to_inv_window()

        else:
            # TODO
            # VENTANAS DE ADVERTENCIA
            title = "Datos incorrectos"
            text = f"Intentos restantes: {3 - self.conteo}"

            setted_message_box(self, title, text)

            self.conteo += 1
