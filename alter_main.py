import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import *

from controller.querys import Database
# TODO: LLENAR TABLAS SESIÓN Y DETALLESESION
class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/admin_window.ui', self)
        
        self.db = Database()
        self.close_to_switch = False
        
        self.rb_inven.toggled.connect(self.show_inven_table)
        self.rb_producto.toggled.connect(self.show_product_table)
        self.rb_inven.setChecked(True)
        
        self.set_frames()
        self.set_product_table()
        self.set_inve_table()
        self.products_list = self.db.get_products_list()
        self.inven_list = self.db.get_inven_list()
        self.fill_product_table(self.products_list)
        self.fill_inve_table(self.inven_list)
        
        self.txtBuscar.textChanged.connect(self.search_product)
        self.tblProducto.cellClicked.connect(self.display_product_name)
        self.tblInventarista.cellClicked.connect(self.display_inve_name)
        
        self.btn_to_login.clicked.connect(self.back_to_login_window)
        self.btn_edit.clicked.connect(self.update_inv_btn)
        self.btn_add.clicked.connect(self.create_inv_btn)
        self.btn_canc_inv.clicked.connect(self.hide_frame)
        self.btn_acep_inv.clicked.connect(self.create_inv_db)
        
# TABLA PRODUCTO ---------------------------------------------------------------------------------------
    def show_product_table(self, isChecked):
        if isChecked:
            self.lbl_id_nombre.setText("ID12345: NOMBRE")
            self.tblProducto.show()
            self.tblInventarista.hide()

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
            self.set_product_cells()

    # Settea las celdas de la tabla
    def set_product_cells(self):
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
        search = self.txtBuscar.text().lower().replace(" ", "")
        filtered_products = [prod for prod in self.products_list if search in prod[0].lower()
                             or search in prod[1].lower().replace(" ", "")]

        self.update_product_table_content(filtered_products)

    def update_product_table_content(self, updated_list):
        # Limpiar tabla
        while self.tblProducto.rowCount() > 0:
            self.tblProducto.removeRow(0)

        # Rellenar tabla con los productos filtrados
        self.fill_product_table(updated_list)

    def display_product_name(self, row, _):
        product_id = self.tblProducto.item(row, 0).text()
        product_name = self.tblProducto.item(row, 1).text()
        self.lbl_id_nombre.setText(f"{product_id}: {product_name}")
    
# TABLA INVENTARISTA ------------------------------------------------------------------------------------  
    def show_inven_table(self, isChecked):
        if isChecked:
            self.lbl_id_nombre.setText("ID12345: NOMBRE")
            self.tblInventarista.show()
            self.tblProducto.hide()
    
    def set_inve_table(self):
        # Ancho de las columnas como se necesita
        columns_width = [70, 80, 150, 150, 80, 90, 200, 65, 110, 180, 90, 40, 70, 70]

        for i, width in enumerate(columns_width):
            self.tblInventarista.setColumnWidth(i, width)

        self.tblInventarista.verticalHeader().setFixedWidth(32)
        self.tblInventarista.verticalHeader().setDefaultAlignment(
            Qt.AlignRight | Qt.AlignVCenter)
        self.tblInventarista.horizontalHeader().setFixedHeight(40)
        self.tblInventarista.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tblInventarista.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def fill_inve_table(self, inve_list_to_fill):
        for single_list in inve_list_to_fill:
            row_position = self.tblInventarista.rowCount()
            self.tblInventarista.insertRow(row_position)
            # Settea la columna de sueldo a dos decimales
            single_list[12] = round(single_list[12], 2)

            # Rellena la tabla en base a las listas de inventaristas
            for i, value in enumerate(single_list):
                self.tblInventarista.setItem(
                    row_position, i, QTableWidgetItem(str(value)))

            # Llama a set cells para la corrección de las celdas
            self.set_inve_cells()
            
    def set_inve_cells(self):
        # Bloquear edición de campos
        for row in range(self.tblInventarista.rowCount()):
            for column in range(self.tblInventarista.columnCount()):
                item = self.tblInventarista.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Columnas para alinear a la izquierda
        collumns_to_align = [5, 7, 8, 10, 12]

        for i in collumns_to_align:
            for row_index in range(self.tblInventarista.rowCount()):
                item = self.tblInventarista.item(row_index, i)
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    
    def search_product(self):
        search = self.txtBuscar.text().lower().replace(" ", "")
        filtered_inve = [inve for inve in self.inven_list if search in inve[0].lower()
                         or search in inve[2].lower().replace(" ", "") +
                         inve[3].lower().replace(" ", "") or search in inve[5]]

        self.update_inve_table_content(filtered_inve)

    def update_inve_table_content(self, updated_list):
        # Limpiar tabla
        while self.tblInventarista.rowCount() > 0:
            self.tblInventarista.removeRow(0)

        # Rellenar tabla con los inventaristas filtrados
        self.fill_inve_table(updated_list)

    def display_inve_name(self, row, _):
        inve_id = self.tblInventarista.item(row, 0).text()
        inve_name = (self.tblInventarista.item(row, 2).text() + " " +
                     self.tblInventarista.item(row, 3).text())
        self.lbl_id_nombre.setText(f"{inve_id}: {inve_name}")
        
# FRAMES -------------------------------------------------------------------------------------------
    def set_frames(self):
        self.frame_inve.setGeometry((self.width() - self.frame_inve.width()) // 2,
                                (self.height() - self.frame_inve.height()) // 2,
                                self.frame_inve.width(), self.frame_inve.height())
        self.frame_prod.setGeometry((self.width() - self.frame_prod.width()) // 2,
                                (self.height() - self.frame_prod.height()) // 2,
                                self.frame_prod.width(), self.frame_prod.height())
        self.frame_inve.hide()
        self.frame_prod.hide()
        
        self.overlay = QWidget(self.frame_main)
        self.overlay.setGeometry(QRect(0, 0, 1366, 768))
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);")
        self.overlay.hide()

    def show_frame(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(10)
        self.frame_main.setGraphicsEffect(self.blur_effect)
        self.overlay.show()
        self.overlay.raise_()
        self.overlay.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        
        if self.rb_inven.isChecked():
            self.frame_inve.show()
            self.frame_inve.raise_()     
        
        elif self.rb_producto.isChecked():
            self.frame_prod.show()
            self.frame_prod.raise_()

    def hide_frame(self):
        if self.rb_inven.isChecked():
            self.frame_inve.hide()  
        
        elif self.rb_producto.isChecked():
            self.frame_prod.hide()
        
        self.overlay.hide()
        self.frame_main.setGraphicsEffect(None)
        
# CRUD
# PRODUCTO ----------------------------------------------------------------------------------------

# INVENTARISTA ------------------------------------------------------------------------------------
    def collect_inv_data(self):
        # Aquí recolectamos los datos de los widgets
        data = (
            self.txt_id_inv.text(),
            self.txt_ape_inv.text(),
            self.txt_nom_inv.text(),
            self.txt_dir_inv.text(),
            1 if self.cbo_doc.currentText() == "DNI" else 2,
            self.txt_doc_inv.text(),
            self.date_nac.date().toString("yyyy-MM-dd"),  # asumiendo formato de fecha yyyy-MM-dd
            'F' if self.cbo_sexo.currentText() == "Femenino" else 'M',
            self.spb_sueldo.value(),
            'M' if self.cbo_turno.currentText() == "Mañana" else ('T' if self.cbo_turno.currentText() == "Tarde" else 'N'),
            self.txt_ubi_inv.text(),
            self.txt_tel_inv.text(),
            self.txt_mail_inv.text(),
            self.txt_pass_inv.text()
        )
        return data

    def create_inv_db(self):
        data = self.collect_inv_data()
        success = self.db.create_inventarista(data)  # Asume que tienes una instancia de Database en self.database

        if success:
            # TODO: STYLESHEET QMESSAGEBOX, CLEAR DATA FIELDS
            QMessageBox.information(self, "Éxito", "Inventarista agregado con éxito.")
            # Suponiendo que tu frame se llama frame_main, lo ocultamos
            self.hide_frame()
        else:
            QMessageBox.warning(self, "Error", "Hubo un error al agregar el inventarista. Inténtalo de nuevo.")
            
    def create_inv_btn(self):
        self.lbl_titulo.setText("AGREGAR USUARIO")
        self.txt_id_inv.setReadOnly(False)
        self.show_frame()
        
    def update_inv_btn(self):
        self.lbl_titulo.setText("EDITAR USUARIO")
        self.txt_id_inv.setReadOnly(True)
        self.show_frame()
        
# WINDOW ------------------------------------------------------------------------------------------
    def back_to_login_window(self):
        from view.login_window import LoginWindow
        
        self.login_window = LoginWindow()
        self.close_to_switch = True
        self.close()

    def closeEvent(self, event):
        if not self.close_to_switch:
            self.db.close_connection()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
