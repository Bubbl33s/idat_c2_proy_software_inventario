import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from querys import crear_lista_producto, cerrar_conexion


class SoftwareInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/software_inventario.ui', self)
        
        self.mostrar_tabla()

    def mostrar_tabla(self):
        lista_productos = crear_lista_producto()
        
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
    sys.exit(app.exec_())
    cerrar_conexion()
