# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Alice_image = QtWidgets.QLabel(self.centralwidget)
        self.Alice_image.setGeometry(QtCore.QRect(30, 100, 141, 141))
        self.Alice_image.setText("")
        self.Alice_image.setPixmap(QtGui.QPixmap("Image/coding (1).png"))
        self.Alice_image.setScaledContents(True)
        self.Alice_image.setObjectName("Alice_image")
        self.Bob_image = QtWidgets.QLabel(self.centralwidget)
        self.Bob_image.setGeometry(QtCore.QRect(620, 100, 141, 141))
        self.Bob_image.setText("")
        self.Bob_image.setPixmap(QtGui.QPixmap("Image/coding.png"))
        self.Bob_image.setScaledContents(True)
        self.Bob_image.setObjectName("Bob_image")
        self.message_image = QtWidgets.QLabel(self.centralwidget)
        self.message_image.setGeometry(QtCore.QRect(150, 190, 41, 41))
        self.message_image.setText("")
        self.message_image.setPixmap(QtGui.QPixmap("Image/envelope.png"))
        self.message_image.setScaledContents(True)
        self.message_image.setObjectName("message_image")
        self.Alice_name = QtWidgets.QLabel(self.centralwidget)
        self.Alice_name.setGeometry(QtCore.QRect(70, 80, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Alice_name.setFont(font)
        self.Alice_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Alice_name.setObjectName("Alice_name")
        self.Bob_name = QtWidgets.QLabel(self.centralwidget)
        self.Bob_name.setGeometry(QtCore.QRect(660, 80, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Bob_name.setFont(font)
        self.Bob_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Bob_name.setObjectName("Bob_name")
        self.ChangeWindow1 = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeWindow1.setGeometry(QtCore.QRect(40, 350, 171, 51))
        self.ChangeWindow1.setObjectName("ChangeWindow1")
        self.ChangeWindow2 = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeWindow2.setGeometry(QtCore.QRect(590, 350, 171, 51))
        self.ChangeWindow2.setObjectName("ChangeWindow2")
        self.ChangeWindow3 = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeWindow3.setGeometry(QtCore.QRect(320, 350, 171, 51))
        self.ChangeWindow3.setObjectName("ChangeWindow3")
        self.message_image.raise_()
        self.label.raise_()
        self.Alice_image.raise_()
        self.Bob_image.raise_()
        self.Alice_name.raise_()
        self.Bob_name.raise_()
        self.ChangeWindow1.raise_()
        self.ChangeWindow2.raise_()
        self.ChangeWindow3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Diffie-Hellman Visualization"))
        self.Alice_name.setText(_translate("MainWindow", "Alice"))
        self.Bob_name.setText(_translate("MainWindow", "Bob"))
        self.ChangeWindow1.setText(_translate("MainWindow", "Standard Diffie-Hellman"))
        self.ChangeWindow2.setText(_translate("MainWindow", "Diffie-Hellman Integrated RSA"))
        self.ChangeWindow3.setText(_translate("MainWindow", "Man-in-the-middle Attack"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())