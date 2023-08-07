import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import querys as qr
# from querys import crear_lista_producto, cerrar_conexion


class SoftwareInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/software_inventario.ui', self)
       
        self.lista_productos = qr.crear_lista_producto()
        self.txtBuscarProducto.textChanged.connect(self.realizar_busqueda)
         
        self.set_table()
        self.rellenar_tabla(self.lista_productos)

    # MÉTODO PARA SETTEAR LA TABLA DE PRODUCTOS
    def set_table(self):
        # CONFIGURAR EL ANCHO DE CADA COLUMNA
        self.tblProducto.setColumnWidth(0, 60)
        self.tblProducto.setColumnWidth(1, 350)
        self.tblProducto.setColumnWidth(2, 80)
        self.tblProducto.setColumnWidth(3, 80)
        self.tblProducto.setColumnWidth(4, 40)
        self.tblProducto.setColumnWidth(5, 60)
        self.tblProducto.setColumnWidth(6, 100)
        self.tblProducto.setColumnWidth(7, 150)
        self.tblProducto.setColumnWidth(8, 150)
        self.tblProducto.setColumnWidth(9, 110)
        
        # BLOQUEAR LA FUNCIÓN DE CAMBIAR EL ANCHO DE LAS COLUMNAS
        self.tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def rellenar_tabla(self, lista_busqueda):
        for listas in lista_busqueda:
            row_position = self.tblProducto.rowCount()
            self.tblProducto.insertRow(row_position)
            
            self.tblProducto.setItem(row_position, 0, QTableWidgetItem(str(listas[0])))
            self.tblProducto.setItem(row_position, 1, QTableWidgetItem(str(listas[1])))
            self.tblProducto.setItem(row_position, 2, QTableWidgetItem(str(round(listas[2], 2))))
            self.tblProducto.setItem(row_position, 3, QTableWidgetItem(str(listas[3])))
            self.tblProducto.setItem(row_position, 4, QTableWidgetItem(str(listas[4])))
            self.tblProducto.setItem(row_position, 5, QTableWidgetItem(str(listas[5])))
            self.tblProducto.setItem(row_position, 6, QTableWidgetItem(str(listas[6])))
            self.tblProducto.setItem(row_position, 7, QTableWidgetItem(str(listas[7])))
            self.tblProducto.setItem(row_position, 8, QTableWidgetItem(str(listas[8])))
            self.tblProducto.setItem(row_position, 9, QTableWidgetItem(str(listas[9])))
            
            # Bloquear edición de campos
            for row in range(self.tblProducto.rowCount()):
                for column in range(self.tblProducto.columnCount()):
                    item = self.tblProducto.item(row, column)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def realizar_busqueda(self):
        busqueda = self.txtBuscarProducto.text().lower()
        productos_filtrados = self.buscar_producto(busqueda)
        
        # Limpiar tabla
        self.tblProducto.clear()
        self.tblProducto.setRowCount(0)
        
        # Rellenar tabla
        self.rellenar_tabla(productos_filtrados)

    def buscar_producto(self, busqueda):
        productos_filtrados = [prod for prod in self.lista_productos if busqueda in prod[0].lower().replace(" ", "") or busqueda in prod[1].lower().replace(" ", "")]

        return productos_filtrados


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SoftwareInventario()
    gui.show()
    qr.cerrar_conexion()
    sys.exit(app.exec_())
