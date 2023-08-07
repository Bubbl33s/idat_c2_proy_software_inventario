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
        
        self.set_table()
        self.mostrar_tabla()

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

    def mostrar_tabla(self):
        lista_productos = qr.crear_lista_producto()
        
        for listas in lista_productos:
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

"""
        # Convierte los campos Decimal y datetime.date a float y str, respectivamente.
        id_producto = row[0]
        descripcion_producto = row[1]
        precio = float(row[2])
        estado_producto = row[3]
        stock_producto = row[4]
        peso_producto = float(row[5])
        fecha_de_ingreso = str(row[6])
        descripcion_subfamilia = row[7]
        descripcion_familia = row[8]
        descripcion_linea = row[9]
        
        # Imprime los datos.
        print(id_producto, descripcion_producto, precio, estado_producto, stock_producto,
            peso_producto, fecha_de_ingreso, descripcion_subfamilia, descripcion_familia, descripcion_linea)
"""      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SoftwareInventario()
    gui.show()
    qr.cerrar_conexion()
    sys.exit(app.exec_())
