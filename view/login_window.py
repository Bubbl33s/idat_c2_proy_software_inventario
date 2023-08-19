from PyQt5 import uic, QtWidgets

from view.user_window import UserWindow
from view.admin_window import AdminWindow
from controller.querys import Database
from view.message_box import setted_message_box

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        uic.loadUi("ui/login_window.ui", self)
        self.show()

        self.db = Database()

        # Contador de intentos
        self.tries = 0
        # Diccionario con las cuentas de adminstrador
        self.admins_dict = {'IN0001': '34593301','ADMX99': 'ADMX99', 'ADMX88': 'ADMX88'}
        self.users_dict = self.db.get_users_dict()
        
        self.user_id = self.user_full_name = ""

        self.btn_login.clicked.connect(self.verify_null_inputs)

    # Método para verificar que no haya campos vacíos
    def verify_null_inputs(self):
        # Acepta lower debido a que solo son dos letras
        self.login_user = self.txt_user.text().upper()
        self.login_password = self.txt_password.text()

        if not self.login_user or not self.login_password:
            # Ventana de advertencia
            title = "Campos vacíos"
            text = "Llene ambos campos"
            setted_message_box(self, title, text)
        else:
            # Si no hay campos vacíos se procede a la comparación de datos
            self.check_login()

    def switch_to_inv_window(self):
        self.user_window = UserWindow()
        self.user_window.set_user_label(self.login_user, self.user_full_name)
        self.user_window.session_id = self.session_id
        self.user_window.show()
        self.hide()
        
    def switch_to_admin_window(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.hide()

    def check_login(self):
        if self.admins_dict.get(self.login_user) == self.login_password:
            self.switch_to_admin_window()
            
        elif self.users_dict.get(self.login_user, (None, None))[0] == self.login_password:
            self.user_full_name = self.users_dict[self.login_user][1]
            self.session_id = self.db.start_session(self.login_user)  # Aquí llamamos al método para iniciar la sesión y obtener el session_id
            self.switch_to_inv_window()
            
        else:
            self.tries += 1
            title = "Datos incorrectos"
            text = f"Intentos restantes: {3 - self.tries}" if self.tries < 3 else "Intentos agotados. Inicio de sesión fallido."
            response, custom_button = setted_message_box(self, title, text)
            if self.tries >= 3:
                self.close()

    def closeEvent(self, event):
        self.db.close_connection()
        event.accept()
