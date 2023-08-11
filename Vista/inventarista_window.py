from PyQt5 import uic, QtWidgets


class IventaristaWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(IventaristaWindow, self).__init__(parent)
        uic.loadUi("ui/inventarista_window.ui", self)
