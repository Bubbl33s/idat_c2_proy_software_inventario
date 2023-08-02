import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class SoftwareInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/software_inventario.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SoftwareInventario()
    gui.show()
    sys.exit(app.exec_())