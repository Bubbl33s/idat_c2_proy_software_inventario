from PyQt5 import uic, QtWidgets

from view.inventarista_window import IventaristaWindow
from controller.querys import get_users_dict
from view.warning_message_box import setted_message_box


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        uic.loadUi("ui/login_window.ui", self)
        self.show()

        # Contador de intentos
        self.tries = 0
        # Diccionario con las cuentas de adminstrador
        self.admins_dict = {'admx99': 'admx99', 'admz88': 'admz88'}
        self.users_dict = get_users_dict()

        self.btn_login.clicked.connect(self.verify_null_inputs)

    # Método para verificar que no haya campos vacíos
    def verify_null_inputs(self):
        # Acepta lower debido a que solo son dos letras
        self.login_user = self.txt_user.text().lower()
        self.login_password = self.txt_password.text()

        if self.login_user == "" or self.login_password == "":
            # Ventana de advertencia
            title = "Campos vacíos"
            text = "Llene ambos campos"

            setted_message_box(self, title, text)
        else:
            # Si no hay campos vacíos se procede a la comparación de datos
            self.check_login()

    # Método para cambiar a la ventana de inventaristas
    def switch_to_inv_window(self):
        self.window = IventaristaWindow()
        self.window.show()
        self.close()

    # Verificación de usuario y contraseña
    def check_login(self):
        # Administrador
        if self.admins_dict.get(self.login_user) == self.login_password:
            # TODO
            # CAMBIAR A VENTANA DE ADMIN
            pass
        # Inventarista
        elif self.users_dict.get(self.login_user) == self.login_password:
            self.switch_to_inv_window()
        # Sin coincidencia
        else:
            if self.tries < 2:
                self.tries += 1

                title = "Datos incorrectos"
                text = f"Intentos restantes: {3 - self.tries}"

                setted_message_box(self, title, text)
            # Cuando no hay intentos se cierra toda la ventana
            else:
                title = "Intentos agotados"
                text = f"Inicio de sesión fallido"

                response, custom_button = setted_message_box(self, title, text)

                if response == QtWidgets.QMessageBox.AcceptRole:
                    self.close()
