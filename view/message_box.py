from PyQt5 import QtWidgets, QtGui, QtCore


# Crear una Warning Message Box personalizada
def setted_message_box(window, title, text):
    # Accede al archivo qss
    qss = open("assets/warning_message_box.css", 'r')

    # Instancia una QMessageBox
    msgBox = QtWidgets.QMessageBox(window)
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)

    # Anula los botones por defecto para crear uno personalizado
    msgBox.setStandardButtons(QtWidgets.QMessageBox.NoButton)
    custom_button = msgBox.addButton(
        "Ok", QtWidgets.QMessageBox.RejectRole)
    custom_button.setFixedSize(50, 30)
    custom_button.clicked.connect(msgBox.reject)
    msgBox.addButton(custom_button, QtWidgets.QMessageBox.AcceptRole)

    # Icono personalizado
    warning_icon = QtGui.QPixmap("assets/warning-icon.png")
    scaled_warning_icon = warning_icon.scaled(
        42, 42, QtCore.Qt.KeepAspectRatio)
    msgBox.setIconPixmap(scaled_warning_icon)

    # Aplica el qss
    msgBox.setStyleSheet(qss.read())
    msgBox.show()

    return msgBox.exec_(), custom_button


def setted_question_box(window, title, text):
    # Accede al archivo qss
    qss = open("assets/warning_message_box.css", 'r')  # Asumiendo que tienes un css diferente para question

    # Instancia una QMessageBox
    msgBox = QtWidgets.QMessageBox(window)
    msgBox.setIcon(QtWidgets.QMessageBox.Question)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)

    # Anula los botones por defecto para crear uno personalizado
    msgBox.setStandardButtons(QtWidgets.QMessageBox.NoButton)
    
    # Botón personalizado de Aceptar
    accept_button = msgBox.addButton(
        "Aceptar", QtWidgets.QMessageBox.AcceptRole)
    accept_button.setStyleSheet("font-size: 14px;")
    accept_button.setFixedSize(70, 30)
    accept_button.clicked.connect(msgBox.accept)
    
    # Botón personalizado de Cancelar
    cancel_button = msgBox.addButton(
        "Cancelar", QtWidgets.QMessageBox.RejectRole)
    cancel_button.setStyleSheet("font-size: 14px;")
    cancel_button.setFixedSize(70, 30)
    cancel_button.clicked.connect(msgBox.reject)

    # Aplica el qss
    msgBox.setStyleSheet(qss.read())
    msgBox.show()
    result = msgBox.exec_()

    if msgBox.clickedButton() == accept_button:
        return QtWidgets.QMessageBox.Yes, accept_button, cancel_button
    
    elif msgBox.clickedButton() == cancel_button:
        return QtWidgets.QMessageBox.No, accept_button, cancel_button
