# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\STUFF\IDAT\Ciclo II\PROYECTO_FINAL\ui\login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\STUFF\\IDAT\\Ciclo II\\PROYECTO_FINAL\\ui\\../assets/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"font-family: century-ghotic;\n"
"}\n"
"\n"
"QWidget#background{\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(20, 20, 20), stop:1 rgb(80, 80, 80));\n"
"}\n"
"\n"
"QFrame#container{\n"
"background-color: rgb(20, 20, 20);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"color: white;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(152, 152, 152);\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"border:none;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"")
        self.background = QtWidgets.QWidget(MainWindow)
        self.background.setObjectName("background")
        self.container = QtWidgets.QFrame(self.background)
        self.container.setGeometry(QtCore.QRect(20, 20, 361, 401))
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.label = QtWidgets.QLabel(self.container)
        self.label.setGeometry(QtCore.QRect(0, 10, 361, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_user = QtWidgets.QLineEdit(self.container)
        self.txt_user.setGeometry(QtCore.QRect(40, 140, 281, 31))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(-1)
        self.txt_user.setFont(font)
        self.txt_user.setText("")
        self.txt_user.setObjectName("txt_user")
        self.label_5 = QtWidgets.QLabel(self.container)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_password = QtWidgets.QLineEdit(self.container)
        self.txt_password.setGeometry(QtCore.QRect(40, 240, 281, 31))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(-1)
        self.txt_password.setFont(font)
        self.txt_password.setText("")
        self.txt_password.setObjectName("txt_password")
        self.btn_login = QtWidgets.QPushButton(self.container)
        self.btn_login.setGeometry(QtCore.QRect(90, 320, 191, 41))
        font = QtGui.QFont()
        font.setFamily("century-ghotic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        MainWindow.setCentralWidget(self.background)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iniciar sesión"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">InventivaStock</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usuario:</span></p></body></html>"))
        self.txt_user.setPlaceholderText(_translate("MainWindow", "USER1234"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contraseña:</span></p></body></html>"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "••••••••••••"))
        self.btn_login.setText(_translate("MainWindow", "Ingresar"))