import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect, QDate
from PyQt5.QtWidgets import *

from view.message_box import setted_message_box, setted_question_box

from controller.querys import Database
# TODO: MOSTRAR TABLAS SESIÓN Y DETALLESESION
class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/admin_window.ui', self)
        
        self.db = Database()
        self.close_to_switch = False
        
        self.rb_inven.toggled.connect(self.show_inven_table)
        self.rb_producto.toggled.connect(self.show_product_table)
        self.rb_sesion.toggled.connect(self.show_sesion_tables)
        self.rb_inven.setChecked(True)
        # TRUE CREATE, FALSE UPDATE
        self.create_or_update = None

        
        self.set_frames()
        self.set_product_table()
        self.set_inve_table()
        self.set_sesion_table()
        self.set_cambio_table()
        self.products_list = self.db.get_products_list()
        self.inven_list = self.db.get_inven_list()
        self.fill_product_table(self.products_list)
        self.fill_inve_table(self.inven_list)
        self.fill_sesion_table(self.db.get_sesion_list())
        self.fill_cambio_table(self.db.get_cambio_list())
        
        self.txtBuscar.textChanged.connect(self.search_inven)
        self.txtBuscar.textChanged.connect(self.search_product)
        self.txtBuscar.textChanged.connect(self.search_sesion_and_cambio)
        self.tblProducto.cellClicked.connect(self.display_product_name)
        self.tblInventarista.cellClicked.connect(self.display_inve_name)
        
        self.btn_to_login.clicked.connect(self.back_to_login_window)
        self.btn_canc_inv.clicked.connect(self.hide_frame)
        self.btn_canc_prod.clicked.connect(self.hide_frame)
        self.btn_add.clicked.connect(self.add_button_clicked)
        self.btn_edit.clicked.connect(self.edit_button_clicked)
        self.btn_delete.clicked.connect(self.delete_button_clicked)

# LÓGICA DE BOTONES ---------------------------------------------------------------------
    def add_button_clicked(self):
        if self.rb_inven.isChecked():
            self.create_inv_btn()
            self.clear_inv_frame_fields()
        elif self.rb_producto.isChecked():
            self.create_prod_btn()
            self.clear_prod_frame_fields()

    def edit_button_clicked(self):
        if self.rb_inven.isChecked():
            self.update_inv_btn()
        elif self.rb_producto.isChecked():
            self.update_prod_btn()

    def delete_button_clicked(self):
        if self.rb_inven.isChecked():
            self.delete_inv_db()
        elif self.rb_producto.isChecked():
            self.delete_prod_db()
            
# TABLA PRODUCTO ---------------------------------------------------------------------------------------
    def show_product_table(self, isChecked):
        if isChecked:
            self.lbl_id_nombre.setText("ID1234: NOMBRE")
            self.txtBuscar.clear()
            self.txtBuscar.setFocus()
            self.tblProducto.show()
            self.tblInventarista.hide()
            self.tblSesion.hide()
            self.tblCambios.hide()

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

    def search_product(self):
        search = self.txtBuscar.text().lower().replace(" ", "")
        filtered_products = [prod for prod in self.products_list if search in prod[0].lower()
                             or search in prod[1].lower().replace(" ", "")]

        self.update_product_table_content(filtered_products)

    def update_product_table_content(self, updated_list):
        while self.tblProducto.rowCount() > 0:
            self.tblProducto.removeRow(0)

        self.fill_product_table(updated_list)

    def display_product_name(self, row, _):
        product_id = self.tblProducto.item(row, 0).text()
        product_name = self.tblProducto.item(row, 1).text()
        self.lbl_id_nombre.setText(f"{product_id}: {product_name}")
    
# TABLA INVENTARISTA ------------------------------------------------------------------------------------  
    def show_inven_table(self, isChecked):
        if isChecked:
            self.lbl_id_nombre.setText("ID1234: NOMBRE")
            self.txtBuscar.clear()
            self.txtBuscar.setFocus()
            self.tblInventarista.show()
            self.tblProducto.hide()
            self.tblSesion.hide()
            self.tblCambios.hide()
    
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

            for i, value in enumerate(single_list):
                self.tblInventarista.setItem(
                    row_position, i, QTableWidgetItem(str(value)))

            self.set_inve_cells()
            
    def set_inve_cells(self):
        # Bloquear edición de campos
        for row in range(self.tblInventarista.rowCount()):
            for column in range(self.tblInventarista.columnCount()):
                item = self.tblInventarista.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        collumns_to_align = [5, 7, 8, 10, 12]

        for i in collumns_to_align:
            for row_index in range(self.tblInventarista.rowCount()):
                item = self.tblInventarista.item(row_index, i)
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    
    def search_inven(self):
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

# TABLAS SESIÓN Y CAMBIOS SESIÓN -------------------------------------------------------------------
    def show_sesion_tables(self, isChecked):
        if isChecked:
            self.lbl_id_nombre.setText("TABLAS DE SOLO LECTURA")
            self.txtBuscar.clear()
            self.txtBuscar.setFocus()
            self.tblInventarista.hide()
            self.tblProducto.hide()
            self.tblSesion.show()
            self.tblCambios.show()
                
    def set_sesion_table(self):
        # Ajusta el ancho de las columnas según tus necesidades
        columns_width = [80, 80, 70, 100, 80, 80]

        for i, width in enumerate(columns_width):
            self.tblSesion.setColumnWidth(i, width)

        self.tblSesion.verticalHeader().setFixedWidth(32)
        self.tblSesion.verticalHeader().setDefaultAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tblSesion.horizontalHeader().setFixedHeight(40)
        self.tblSesion.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tblSesion.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def fill_sesion_table(self, sesion_list_to_fill):
        for sesion in sesion_list_to_fill:
            row_position = self.tblSesion.rowCount()
            self.tblSesion.insertRow(row_position)
            
            for i, value in enumerate(sesion):
                self.tblSesion.setItem(row_position, i, QTableWidgetItem(str(value)))

    def update_sesion_table_content(self, updated_list):
        while self.tblSesion.rowCount() > 0:
            self.tblSesion.removeRow(0)

        self.fill_sesion_table(updated_list)

    def set_cambio_table(self):
        # Ajusta el ancho de las columnas según tus necesidades
        columns_width = [110, 67, 80, 340, 75]

        for i, width in enumerate(columns_width):
            self.tblCambios.setColumnWidth(i, width)

        self.tblCambios.verticalHeader().setFixedWidth(32)
        self.tblCambios.verticalHeader().setDefaultAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tblCambios.horizontalHeader().setFixedHeight(40)
        self.tblCambios.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tblCambios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def fill_cambio_table(self, cambio_list_to_fill):
        for cambio in cambio_list_to_fill:
            row_position = self.tblCambios.rowCount()
            self.tblCambios.insertRow(row_position)
            
            for i, value in enumerate(cambio):
                self.tblCambios.setItem(row_position, i, QTableWidgetItem(str(value)))
        
        for row in range(self.tblCambios.rowCount()):
            item = self.tblCambios.item(row, 3)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            
            item = self.tblCambios.item(row, 4)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    def update_cambio_table_content(self, updated_list):
        while self.tblCambios.rowCount() > 0:
            self.tblCambios.removeRow(0)

        self.fill_cambio_table(updated_list)

    def search_sesion_and_cambio(self):
        search = self.txtBuscar.text().lower().replace(" ", "")

        filtered_sesiones = [sesion for sesion in self.db.get_sesion_list() if
                            any(search in str(sesion[i]).lower().replace(" ", "") for i in [0, 1, 2])]
        filtered_cambios = [cambio for cambio in self.db.get_cambio_list() if
                            any(search in str(cambio[i]).lower().replace(" ", "") for i in [0, 1, 2, 3])]

        self.update_sesion_table_content(filtered_sesiones)
        self.update_cambio_table_content(filtered_cambios)

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
    def collect_prod_data(self):
        # Aquí recolectamos los datos de los widgets
        estado = 1 if self.cbo_estado_prod.currentText() == 'Activo' else 0
        
        # Obtener el ID de subfamilia a partir del nombre seleccionado en el combobox
        subfamilia_name = self.cbo_subfam_prod.currentText()
        subfamilia_id = self.db.get_subfamilia_id_by_name(subfamilia_name)

        data = (
            self.txt_desc_prod.text(),
            self.spb_precio_prod.value(),
            estado,
            self.spb_stock.value(),
            self.spb_peso_prod.value(),
            self.date_ing.date().toString("yyyy-MM-dd"),
            subfamilia_id
        )
        return data

    def fill_prod_frame_fields(self):
        current_row = self.tblProducto.currentRow()

        # Obtenemos los datos de la fila seleccionada
        data = []
        for column in range(self.tblProducto.columnCount()):
            item = self.tblProducto.item(current_row, column)
            data.append(item.text() if item else "")

        self.txt_id_prod.setText(data[0])
        self.txt_desc_prod.setText(data[1])
        self.spb_precio_prod.setValue(float(data[2]))
        self.cbo_estado_prod.setCurrentText(data[3])
        self.spb_stock.setValue(int(data[4]))
        self.spb_peso_prod.setValue(float(data[5]))
        self.date_ing.setDate(QDate.fromString(data[6], "yyyy-MM-dd"))
        self.cbo_subfam_prod.setCurrentText(data[7])

    def clear_prod_frame_fields(self):
        # Limpiar los LineEdits y SpinBoxes
        line_edits = [self.txt_id_prod, self.txt_desc_prod]
        spin_boxes = [self.spb_precio_prod, self.spb_stock, self.spb_peso_prod]

        for line_edit in line_edits:
            line_edit.clear()

        for spin_box in spin_boxes:
            spin_box.clear()

        self.cbo_estado_prod.setCurrentIndex(0)
        self.cbo_subfam_prod.setCurrentIndex(0)

        # Resetear DateEdit
        self.date_ing.setDate(QDate.currentDate())

    def create_prod_db(self):
        # Obtiene el siguiente ID de producto
        new_id = self.db.get_next_producto_id()
        data = (new_id,) + self.collect_prod_data()

        success = self.db.create_producto(data)

        if success:
            title = "Éxito"
            text = "Producto agregado con éxito."
            setted_message_box(self, title, text)
            self.clear_prod_frame_fields()
            self.update_product_table_content(self.db.get_products_list())
            self.lbl_id_nombre.setText("ID1234: NOMBRE")
            self.hide_frame()
        else:
            title = "Error"
            text = "Hubo un error al agregar el producto. Inténtalo de nuevo."
            setted_message_box(self, title, text)

    def update_prod_db(self):
        data_collected = self.collect_prod_data()
        # Añadir el ID al principio de los datos recolectados
        data = (self.txt_id_prod.text(),) + data_collected

        success = self.db.update_producto(data)

        if success:
            title = "Éxito"
            text = "Producto actualizado con éxito."
            setted_message_box(self, title, text)
            self.clear_prod_frame_fields()
            self.update_product_table_content(self.db.get_products_list())
            self.hide_frame()
        else:
            title = "Error"
            text = "Hubo un error al actualizar el producto o no se encontró el ID especificado. Inténtalo de nuevo."
            setted_message_box(self, title, text)

    def delete_prod_db(self):
        print("Intentando eliminar producto...")
        current_row = self.tblProducto.currentRow()
        
        if current_row == -1:
            title = "Selección requerida"
            text = "Por favor, selecciona un producto para eliminar."
            setted_message_box(self, title, text)
            return

        id_item = self.tblProducto.item(current_row, 0).text()
        producto_id = id_item if id_item else None

        title = "Confirmar eliminación"
        text = "¿Estás seguro de que quieres eliminar este producto?"
        response, _, _ = setted_question_box(self, title, text)

        if response == QMessageBox.Yes:
            print("BOTÓN ACEPTAR")
            success = self.db.delete_producto(producto_id)

            if success:
                title = "Éxito"
                text = "Producto eliminado con éxito."
                setted_message_box(self, title, text)
                self.clear_prod_frame_fields()
                self.update_product_table_content(self.db.get_products_list())
                self.lbl_id_nombre.setText("ID1234: NOMBRE")
                self.hide_frame()
            else:
                title = "Error"
                text = "Hubo un error al eliminar el producto o no se encontró el ID especificado. Inténtalo de nuevo."
                setted_message_box(self, title, text)

    def create_prod_btn(self):
        self.create_or_update = True
        
        try:
            self.btn_acep_prod.clicked.disconnect()
        except TypeError:
            pass
        
        self.btn_acep_prod.clicked.connect(self.create_prod_db)
        self.lbl_titulo_prod.setText("AGREGAR PRODUCTO")
        self.txt_id_prod.setReadOnly(True)
        self.show_frame()
    
    def update_prod_btn(self):
        current_row = self.tblProducto.currentRow()
        
        # Verificar si hay una fila seleccionada
        if current_row == -1:
            title = "Selección requerida"
            text = "Por favor, selecciona un producto para actualizar."
            setted_message_box(self, title, text)
            return

        self.create_or_update = False
        
        try:
            self.btn_acep_prod.clicked.disconnect()
        except TypeError:  # Ignorar si no hay ninguna función conectada al botón
            pass
        
        self.btn_acep_prod.clicked.connect(self.update_prod_db)
        self.lbl_titulo_prod.setText("EDITAR PRODUCTO")
        self.btn_acep_prod.clicked.connect(self.update_prod_db)
        self.fill_prod_frame_fields()
        self.txt_id_prod.setReadOnly(True)  # El ID no debe ser editable al actualizar
        self.show_frame()

# INVENTARISTA ------------------------------------------------------------------------------------
    def collect_inv_data(self):
        # Aquí recolectamos los datos de los widgets
        data = (
            self.txt_id_inv.text().upper(),
            self.txt_ape_inv.text().title(),
            self.txt_nom_inv.text().title(),
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
    
    def fill_inv_frame_fields(self):
        current_row = self.tblInventarista.currentRow()

        # Obtenemos los datos de la fila seleccionada
        data = []
        for column in range(self.tblInventarista.columnCount()):
            item = self.tblInventarista.item(current_row, column)
            data.append(item.text() if item else "")

        self.txt_id_inv.setText(data[0])
        self.txt_ape_inv.setText(data[2])
        self.txt_nom_inv.setText(data[3])
        self.txt_dir_inv.setText(data[6])
        self.cbo_doc.setCurrentIndex(self.cbo_doc.findText(data[4]))
        self.txt_doc_inv.setText(data[5])
        self.date_nac.setDate(QDate.fromString(data[10], "yyyy-MM-dd"))
        self.cbo_sexo.setCurrentIndex(self.cbo_sexo.findText(data[11]))
        self.spb_sueldo.setValue(float(data[12]))
        self.cbo_turno.setCurrentIndex(self.cbo_turno.findText(data[13]))
        self.txt_ubi_inv.setText(data[7])
        self.txt_tel_inv.setText(data[8])
        self.txt_mail_inv.setText(data[9])
        self.txt_pass_inv.setText(data[1])
    
    def clear_inv_frame_fields(self):
        line_edits = [self.txt_id_inv, self.txt_ape_inv, self.txt_nom_inv,
                      self.txt_dir_inv, self.txt_doc_inv, self.txt_ubi_inv,
                      self.txt_tel_inv, self.txt_mail_inv, self.txt_pass_inv]
        
        for line_edit in line_edits:
            line_edit.clear()

        self.cbo_doc.setCurrentIndex(0)
        self.cbo_sexo.setCurrentIndex(0)
        self.cbo_turno.setCurrentIndex(0)
        self.spb_sueldo.setValue(1000.00)
        self.date_nac.setDate(QDate(2000, 1, 1))

    def create_inv_db(self):
        # Generar ID automáticamente
        new_id = self.db.get_next_inventarista_id()
        data = self.collect_inv_data()
        # Reemplazar el ID que se recogió de los widgets con el nuevo ID generado automáticamente
        data = (new_id,) + data[1:]
        success = self.db.create_inventarista(data)

        if success:
            title = "Éxito"
            text = "Inventarista agregado con éxito."
            setted_message_box(self, title, text)
            self.clear_inv_frame_fields()
            self.update_inve_table_content(self.db.get_inven_list())
            self.lbl_id_nombre.setText("ID1234: NOMBRE")
            self.hide_frame()
        else:
            title = "Error"
            text = "Hubo un error al agregar el inventarista. Inténtalo de nuevo."
            setted_message_box(self, title, text)

    def update_inv_db(self):
        data = self.collect_inv_data()
        success = self.db.update_inventarista(data)

        if success:
            title = "Éxito"
            text = "Inventarista actualizado con éxito."
            setted_message_box(self, title, text)
            self.clear_inv_frame_fields()
            self.update_inve_table_content(self.db.get_inven_list())
            self.hide_frame()
        else:
            title = "Error"
            text = ("Hubo un error al actualizar el inventarista o "
                    "no se encontró el ID especificado. Inténtalo de nuevo.")
            setted_message_box(self, title, text)

    def delete_inv_db(self):
        current_row = self.tblInventarista.currentRow()
        
        if current_row == -1:
            title = "Selección requerida"
            text = "Por favor, selecciona un inventarista para eliminar."
            setted_message_box(self, title, text)
            return

        id_item = self.tblInventarista.item(current_row, 0).text()
        inventarista_id = id_item if id_item else None

        # Ahora sí, pedimos confirmación al usuario
        title = "Confirmar eliminación"
        text = "¿Estás seguro de que quieres eliminar este inventarista?"
        response, _, _ = setted_question_box(self, title, text)

        if response == QMessageBox.Yes:
            success = self.db.delete_inventarista(inventarista_id)

            if success:
                title = "Éxito"
                text = "Inventarista eliminado con éxito."
                setted_message_box(self, title, text)
                self.clear_inv_frame_fields()
                self.update_inve_table_content(self.db.get_inven_list())
                self.lbl_id_nombre.setText("ID1234: NOMBRE")
                self.hide_frame()
            else:
                title = "Error"
                text = ("Hubo un error al eliminar el inventarista o "
                        "no se encontró el ID especificado. Inténtalo de nuevo.")
                setted_message_box(self, title, text)

    def create_inv_btn(self):
        self.create_or_update = True
        
        try:
            self.btn_acep_inv.clicked.disconnect()
        except TypeError:  # Ignorar si no hay ninguna función conectada al botón
            pass
        
        self.btn_acep_inv.clicked.connect(self.create_inv_db)
        self.lbl_titulo_inv.setText("AGREGAR USUARIO")
        self.txt_id_inv.setReadOnly(True)
        self.show_frame()

    def update_inv_btn(self):
        current_row = self.tblInventarista.currentRow()
        
        # Verificar si hay una fila seleccionada
        if current_row == -1:
            title = "Selección requerida"
            text = "Por favor, selecciona un inventarista para actualizar."
            setted_message_box(self, title, text)
            return
        
        self.create_or_update = False
        
        try:
            self.btn_acep_inv.clicked.disconnect()
        except TypeError:  # Ignorar si no hay ninguna función conectada al botón
            pass
        
        self.btn_acep_inv.clicked.connect(self.update_inv_db)
        self.lbl_titulo_inv.setText("EDITAR USUARIO")
        self.fill_inv_frame_fields()
        self.txt_id_inv.setReadOnly(True)
        self.show_frame()
        
# WINDOW ------------------------------------------------------------------------------------------
    def back_to_login_window(self):
        from view.login_window import LoginWindow
        
        self.login_window = LoginWindow()
        self.close_to_switch = True
        self.hide()

    def closeEvent(self, event):
        if not self.close_to_switch:
            self.db.close_connection()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
