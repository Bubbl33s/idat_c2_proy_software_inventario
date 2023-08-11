from PyQt5 import uic, QtWidgets, QtGui, QtCore
from vista.inventarista_window import IventaristaWindow
from controller.querys import get_users_dict


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
            stylesheet = """
/* Cambiar la fuente y el color de fondo de QMessageBox */
QMessageBox {
    background-color: #111111;
    font-family: "Century Gothic";
}

/* Cambiar el color del texto de "Intentos restantes" */
QMessageBox QLabel[text^="Intentos"] {
    color: #FFFFFF;
}


"""

            msgBox = QtWidgets.QMessageBox(self)
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Datos incorrectos")
            msgBox.setText(f"Intentos restantes: {3 - self.conteo}")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.NoButton)
            cancel_button = msgBox.addButton(
                "Ok", QtWidgets.QMessageBox.RejectRole)
            cancel_button.setFixedSize(50, 30)
            warning_icon = QtGui.QPixmap("assets/warning-icon.png")
            scaled_warning_icon = warning_icon.scaled(
                42, 42, QtCore.Qt.KeepAspectRatio)
            msgBox.setIconPixmap(scaled_warning_icon)
            cancel_button.clicked.connect(msgBox.reject)

            # Aplicar el QSS
            msgBox.setStyleSheet(stylesheet)

            msgBox.show()

            self.conteo += 1
