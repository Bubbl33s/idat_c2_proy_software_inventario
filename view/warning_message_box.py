from PyQt5 import QtWidgets, QtGui, QtCore


# Crear una Warning Message Box personalizada
def setted_message_box(window, title, text):
    # Accede al archivo qss
    qss = open("assets/warning_message_box.qss", 'r')

    msgBox = QtWidgets.QMessageBox(window)
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
    # Anula los botones por defecto para crear uno personalizado
    msgBox.setStandardButtons(QtWidgets.QMessageBox.NoButton)
    custom_button = msgBox.addButton(
        "Ok", QtWidgets.QMessageBox.RejectRole)
    custom_button.setFixedSize(50, 30)
    # Icono personalizado
    warning_icon = QtGui.QPixmap("assets/warning-icon.png")
    scaled_warning_icon = warning_icon.scaled(
        42, 42, QtCore.Qt.KeepAspectRatio)
    msgBox.setIconPixmap(scaled_warning_icon)
    custom_button.clicked.connect(msgBox.reject)
    msgBox.addButton(custom_button, QtWidgets.QMessageBox.AcceptRole)
    # Aplica el qss
    msgBox.setStyleSheet(qss.read())

    msgBox.show()

    return msgBox.exec_(), custom_button
