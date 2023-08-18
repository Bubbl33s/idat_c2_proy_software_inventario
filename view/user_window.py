import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from controller.querys import get_products_list, close_connection, update_stock_for_user


# TODO: CORREGIR LA BÚSQUEDA CON ESPACIOS
class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/user_window.ui', self)

        self.close_to_switch = False
        self.set_product_table()
        self.products_list = get_products_list()
        self.fill_product_table(self.products_list)
        self.txtBuscarProducto.textChanged.connect(
            self.search_product)
        self.tblProducto.cellClicked.connect(self.display_product_name)
        self.btn_apply.clicked.connect(self.update_stock)
        self.btn_to_login.clicked.connect(self.back_to_login_window)

    def set_product_table(self):
        # Ancho de las columnas como se necesita
        columns_width = [77, 360, 80, 70, 50, 60, 100, 140, 165, 110]

        for i, width in enumerate(columns_width):
            self.tblProducto.setColumnWidth(i, width)

        self.tblProducto.verticalHeader().setFixedWidth(32)
        self.tblProducto.verticalHeader().setDefaultAlignment(
            Qt.AlignRight | Qt.AlignVCenter)
        self.tblProducto.horizontalHeader().setFixedHeight(40)
        self.tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tblProducto.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    # Se llama al inicio y cada vez que se realiza una búsqueda
    def fill_product_table(self, products_list_to_fill):
        for single_list in products_list_to_fill:
            row_position = self.tblProducto.rowCount()
            self.tblProducto.insertRow(row_position)
            # Settea la columna de precio a dos decimales
            single_list[2] = round(single_list[2], 2)

            # Rellena la tabla en base a las listas de productos
            for i, value in enumerate(single_list):
                self.tblProducto.setItem(
                    row_position, i, QTableWidgetItem(str(value)))

            # Llama a set cells para la corrección de las celdas
            self.set_cells()

    # Settea las celdas de la tabla
    def set_cells(self):
        # Bloquear edición de campos
        for row in range(self.tblProducto.rowCount()):
            for column in range(self.tblProducto.columnCount()):
                item = self.tblProducto.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Columnas para alinear a la izquierda
        collumns_to_align = [2, 4, 5]

        for i in collumns_to_align:
            for row_index in range(self.tblProducto.rowCount()):
                item = self.tblProducto.item(row_index, i)
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

    # La lógica de la búsqueda de productos
    def search_product(self):
        search = self.txtBuscarProducto.text().lower().replace(" ", "")
        filtered_products = [prod for prod in self.products_list if search in prod[0].lower()
                             .replace(" ", "") or search in prod[1].lower().replace(" ", "")]

        self.update_table_content(filtered_products)

    def update_table_content(self, updated_list):
        # Limpiar tabla
        while self.tblProducto.rowCount() > 0:
            self.tblProducto.removeRow(0)

        # Rellenar tabla con los productos filtrados
        self.fill_product_table(updated_list)

    def display_product_name(self, row, _):
        product_id = self.tblProducto.item(row, 0).text()
        product_name = self.tblProducto.item(row, 1).text()
        product_stock = int(self.tblProducto.item(row, 4).text())
        self.lbl_id_nombre.setText(f"{product_id}: {product_name}")
        self.spx_stock.setValue(product_stock)

    def update_stock(self):
        product_id = self.lbl_id_nombre.text()[:6]
        update_stock_for_user(self.spx_stock.value(), product_id)
        self.products_list = get_products_list()

        self.update_table_content(self.products_list)
        self.search_product()

    def set_user_label(self, user_id, user_name):
        self.lbl_id_user.setText(f"Usuario {user_id}: {user_name}")
        
    def back_to_login_window(self):
        from view.login_window import LoginWindow
        
        self.login_window = LoginWindow()
        self.close_to_switch = True
        self.close()

    def closeEvent(self, event):
        if not self.close_to_switch:
            close_connection()
        event.accept()
