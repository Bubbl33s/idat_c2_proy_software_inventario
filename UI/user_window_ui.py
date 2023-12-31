# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\STUFF\IDAT\Ciclo II\PROYECTO_FINAL\ui\user_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\STUFF\\IDAT\\Ciclo II\\PROYECTO_FINAL\\ui\\../assets/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    font-family: century-ghotic;\n"
"}\n"
"\n"
"QWidget#background{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(20, 20, 20), stop:1 rgb(80, 80, 80));\n"
"}\n"
"\n"
"QFrame#frame_main{\n"
"    background-color: rgb(20, 20, 20);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame#edit_stock_frame {\n"
"    background-color: rgb(120, 120, 120);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(152, 152, 152);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QMessageBox{\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"    color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    color: rgb(230, 230, 230);\n"
"    gridline-color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border-right: 8px solid rgb(20, 20, 20);\n"
"    border-left: 8px solid rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTableWidget QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(152, 152, 152);\n"
"    width: 15px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-page:vertical, QTableWidget QScrollBar::sub-page:vertical {\n"
"    background: rgb(152, 152, 152);\n"
"}\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgb(44, 44, 44);\n"
"    margin: 2px 2.5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::sub-line:vertical, QTableWidget QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QFrame#edit_stock_frame QLabel {\n"
"    color: black;\n"
"}\n"
"\n"
"QLabel#lbl_id_nombre {\n"
"    font-family: century-ghotic;\n"
"    font-size: 18px;\n"
"    color: black;\n"
"}\n"
"\n"
"QLabel#lbl_id_user {\n"
"    font-family: century-ghotic;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_apply{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    border:none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_apply:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton#btn_apply:pressed {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QSpinBox {\n"
"    font-size: 18px;\n"
"    background-color: rgb(120, 120, 120);\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a3a3a;\n"
"    color: white;\n"
"}")
        self.background = QtWidgets.QWidget(MainWindow)
        self.background.setStyleSheet("")
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_producto = QtWidgets.QFrame(self.background)
        self.frame_producto.setMinimumSize(QtCore.QSize(1366, 768))
        self.frame_producto.setMaximumSize(QtCore.QSize(1633, 768))
        self.frame_producto.setStyleSheet("")
        self.frame_producto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_producto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_producto.setObjectName("frame_producto")
        self.frame_main = QtWidgets.QFrame(self.frame_producto)
        self.frame_main.setGeometry(QtCore.QRect(20, 20, 1331, 731))
        self.frame_main.setStyleSheet("QTableWidget QScrollBar::sub-line:vertical, QTableWidget QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::up-arrow:vertical, QTableWidget QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.tblProducto = QtWidgets.QTableWidget(self.frame_main)
        self.tblProducto.setEnabled(True)
        self.tblProducto.setGeometry(QtCore.QRect(40, 190, 1261, 521))
        self.tblProducto.setStyleSheet("")
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
        self.tblProducto.verticalHeader().setCascadingSectionResizes(False)
        self.txtBuscarProducto = QtWidgets.QLineEdit(self.frame_main)
        self.txtBuscarProducto.setGeometry(QtCore.QRect(60, 90, 281, 41))
        self.txtBuscarProducto.setObjectName("txtBuscarProducto")
        self.lbl_title = QtWidgets.QLabel(self.frame_main)
        self.lbl_title.setGeometry(QtCore.QRect(30, 10, 321, 51))
        self.lbl_title.setObjectName("lbl_title")
        self.edit_stock_frame = QtWidgets.QFrame(self.frame_main)
        self.edit_stock_frame.setGeometry(QtCore.QRect(430, 80, 841, 71))
        self.edit_stock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_stock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_stock_frame.setObjectName("edit_stock_frame")
        self.lbl_id_nombre = QtWidgets.QLabel(self.edit_stock_frame)
        self.lbl_id_nombre.setGeometry(QtCore.QRect(20, 0, 531, 71))
        self.lbl_id_nombre.setObjectName("lbl_id_nombre")
        self.lbl_stock = QtWidgets.QLabel(self.edit_stock_frame)
        self.lbl_stock.setGeometry(QtCore.QRect(550, 0, 61, 71))
        self.lbl_stock.setObjectName("lbl_stock")
        self.spx_stock = QtWidgets.QSpinBox(self.edit_stock_frame)
        self.spx_stock.setGeometry(QtCore.QRect(600, 20, 61, 31))
        self.spx_stock.setMaximum(300)
        self.spx_stock.setSingleStep(10)
        self.spx_stock.setObjectName("spx_stock")
        self.btn_apply = QtWidgets.QPushButton(self.edit_stock_frame)
        self.btn_apply.setGeometry(QtCore.QRect(690, 20, 121, 31))
        self.btn_apply.setObjectName("btn_apply")
        self.lbl_id_user = QtWidgets.QLabel(self.frame_main)
        self.lbl_id_user.setGeometry(QtCore.QRect(590, -10, 651, 91))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(-1)
        self.lbl_id_user.setFont(font)
        self.lbl_id_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_id_user.setObjectName("lbl_id_user")
        self.btn_to_login = QtWidgets.QPushButton(self.frame_main)
        self.btn_to_login.setGeometry(QtCore.QRect(1280, 0, 50, 50))
        self.btn_to_login.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\STUFF\\IDAT\\Ciclo II\\PROYECTO_FINAL\\ui\\../assets/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_to_login.setIcon(icon1)
        self.btn_to_login.setIconSize(QtCore.QSize(30, 30))
        self.btn_to_login.setObjectName("btn_to_login")
        self.verticalLayout.addWidget(self.frame_producto)
        MainWindow.setCentralWidget(self.background)

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
        self.txtBuscarProducto.setPlaceholderText(_translate("MainWindow", "Buscar..."))
        self.lbl_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Inventiva Stock</span></p></body></html>"))
        self.lbl_id_nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">ID1234: NOMBRE PRODUCTO</span></p></body></html>"))
        self.lbl_stock.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Stock:</span></p></body></html>"))
        self.btn_apply.setText(_translate("MainWindow", "Aplicar"))
        self.lbl_id_user.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ID1234: Jimenez Rodriguez Mireya Antonela</span></p></body></html>"))
