# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\STUFF\IDAT\Ciclo II\PROYECTO_FINAL\ui\software_inventario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\STUFF\\IDAT\\Ciclo II\\PROYECTO_FINAL\\ui\\../assets/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_producto = QtWidgets.QFrame(self.centralwidget)
        self.frame_producto.setMinimumSize(QtCore.QSize(1280, 720))
        self.frame_producto.setMaximumSize(QtCore.QSize(1280, 16777215))
        self.frame_producto.setStyleSheet("")
        self.frame_producto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_producto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_producto.setObjectName("frame_producto")
        self.tblProducto = QtWidgets.QTableWidget(self.frame_producto)
        self.tblProducto.setEnabled(True)
        self.tblProducto.setGeometry(QtCore.QRect(40, 260, 1240, 361))
        self.tblProducto.setStyleSheet("QHeaderView::section {\n"
"    color: rgb(170, 0, 127)\n"
"}")
        self.tblProducto.setObjectName("tblProducto")
        self.tblProducto.setColumnCount(10)
        self.tblProducto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProducto.setHorizontalHeaderItem(9, item)
        self.txtBuscarProducto = QtWidgets.QLineEdit(self.frame_producto)
        self.txtBuscarProducto.setGeometry(QtCore.QRect(200, 150, 231, 41))
        self.txtBuscarProducto.setObjectName("txtBuscarProducto")
        self.btnBuscar = QtWidgets.QPushButton(self.frame_producto)
        self.btnBuscar.setGeometry(QtCore.QRect(580, 150, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.verticalLayout.addWidget(self.frame_producto)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INVENTIVA STOCK"))
        item = self.tblProducto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tblProducto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblProducto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tblProducto.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tblProducto.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.tblProducto.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.tblProducto.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ingreso"))
        item = self.tblProducto.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Subfamilia"))
        item = self.tblProducto.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Familia"))
        item = self.tblProducto.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Línea"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
