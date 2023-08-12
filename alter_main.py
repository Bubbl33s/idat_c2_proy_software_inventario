import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from controller.querys import get_products_list, close_connection
from view.items_margin import TableItemDelegate


class SoftwareInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/inventarista_window.ui', self)

        self.products_list = get_products_list()
        self.txtBuscarProducto.textChanged.connect(
            self.search_product)

        self.set_product_table()
        self.fill_product_table(self.products_list)

    # MÉTODO PARA SETTEAR LA TABLA DE PRODUCTOS
    def set_product_table(self):
        # CONFIGURAR EL ANCHO DE CADA COLUMNA
        self.tblProducto.setColumnWidth(0, 77)
        self.tblProducto.setColumnWidth(1, 360)
        self.tblProducto.setColumnWidth(2, 80)
        self.tblProducto.setColumnWidth(3, 80)
        self.tblProducto.setColumnWidth(4, 40)
        self.tblProducto.setColumnWidth(5, 60)
        self.tblProducto.setColumnWidth(6, 100)
        self.tblProducto.setColumnWidth(7, 150)
        self.tblProducto.setColumnWidth(8, 160)
        self.tblProducto.setColumnWidth(9, 110)

        # Configurar headers
        self.tblProducto.verticalHeader().setFixedWidth(32)
        self.tblProducto.verticalHeader().setDefaultAlignment(
            Qt.AlignRight | Qt.AlignVCenter)

        self.tblProducto.horizontalHeader().setFixedHeight(40)
        self.tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.tblProducto.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def fill_product_table(self, single_lists_to_search):
        for single_list in single_lists_to_search:
            row_position = self.tblProducto.rowCount()
            self.tblProducto.insertRow(row_position)

            self.tblProducto.setItem(
                row_position, 0, QTableWidgetItem(str(single_list[0])))
            self.tblProducto.setItem(
                row_position, 1, QTableWidgetItem(str(single_list[1])))
            self.tblProducto.setItem(
                row_position, 2, QTableWidgetItem(str(round(single_list[2], 2))))
            self.tblProducto.setItem(
                row_position, 3, QTableWidgetItem(str(single_list[3])))
            self.tblProducto.setItem(
                row_position, 4, QTableWidgetItem(str(single_list[4])))
            self.tblProducto.setItem(
                row_position, 5, QTableWidgetItem(str(single_list[5])))
            self.tblProducto.setItem(
                row_position, 6, QTableWidgetItem(str(single_list[6])))
            self.tblProducto.setItem(
                row_position, 7, QTableWidgetItem(str(single_list[7])))
            self.tblProducto.setItem(
                row_position, 8, QTableWidgetItem(str(single_list[8])))
            self.tblProducto.setItem(
                row_position, 9, QTableWidgetItem(str(single_list[9])))

            self.fix_cells()

    def fix_cells(self):
        # Bloquear edición de campos
        for row in range(self.tblProducto.rowCount()):
            for column in range(self.tblProducto.columnCount()):
                item = self.tblProducto.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Alineación columna 3
        index_nums_align = [2, 4, 5]

        for i in index_nums_align:
            for row_index in range(self.tblProducto.rowCount()):
                item = self.tblProducto.item(row_index, i)
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

    def search_product(self):
        search = self.txtBuscarProducto.text().lower()
        filtered_products = self.search_list_products(search)

        # Limpiar tabla
        while self.tblProducto.rowCount() > 0:
            self.tblProducto.removeRow(0)

        # Rellenar tabla
        self.fill_product_table(filtered_products)

    def search_list_products(self, search):
        filtered_products = [prod for prod in self.products_list if search in prod[0].lower()
                             .replace(" ", "") or search in prod[1].lower().replace(" ", "")]

        return filtered_products


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SoftwareInventario()
    gui.show()
    close_connection()
    sys.exit(app.exec_())
