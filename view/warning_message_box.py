from PyQt5 import QtWidgets, QtGui, QtCore


def setted_message_box(window, title, text):
    qss = open("assets/warning_message_box.qss", 'r')

    msgBox = QtWidgets.QMessageBox(window)
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
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
    msgBox.setStyleSheet(qss.read())

    msgBox.show()
