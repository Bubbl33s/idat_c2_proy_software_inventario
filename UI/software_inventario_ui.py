# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maste\OneDrive\Escritorio\STUFF\IDAT\Ciclo II\PROYECTO_FINAL\ui\software_inventario.ui'
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
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\maste\\OneDrive\\Escritorio\\STUFF\\IDAT\\Ciclo II\\PROYECTO_FINAL\\ui\\../assets/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.frame_producto.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_producto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_producto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_producto.setObjectName("frame_producto")
        self.verticalLayout.addWidget(self.frame_producto)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INVENTIVA STOCK"))
