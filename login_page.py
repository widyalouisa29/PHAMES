from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from daftar_page import Ui_DaftarWindow

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)

        app = QApplication.instance()
        app.setStyle("Fusion")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 600))#frame kiri ukuran 
        pixmapLoginImage = QtGui.QPixmap("login_bg.png")#input Image
        self.frame.setPixmap(pixmapLoginImage)
        self.frame.setScaledContents(True) #frame kiri 
       
        self.frame.setObjectName("frame")#frame kanan
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(399, 0, 401, 600))#x,y,weight,height
        self.frame_2.setStyleSheet("background-color: #8c7bff;")#frame kanan Bg
        self.frame_2.setObjectName("frame_2")
        #frame kanan Label Pharmacy
        self.appNameLabel = QtWidgets.QLabel(self.frame_2)
        self.appNameLabel.setGeometry(QtCore.QRect(60, 80, 301, 81))#frame kanan tata letak label
        self.appNameLabel.setStyleSheet("font-family: Arial; font-size: 15pt; font-weight: bold;")#font Label pharmacy
        self.appNameLabel.setObjectName("appNameLabel")
        self.appNameLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        #Unsername 
        self.namaField = QtWidgets.QTextEdit(self.frame_2)
        self.namaField.setGeometry(QtCore.QRect(60, 230, 291, 45))#tata letak(x,y,weight,height)
        self.namaField.setStyleSheet("font-family: Arial; font-size: 12pt; background-color: #FFFFFF; color: #000000; border: 1px solid #000000; padding-top: 10px; padding-left: 20px;")
        self.namaField.setObjectName("namaField")
        #Password
        self.sandiField = QtWidgets.QTextEdit(self.frame_2)
        self.sandiField.setGeometry(QtCore.QRect(60, 290, 291, 45))
        self.sandiField.setStyleSheet("font-family: Arial; font-size: 10pt; background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 50%; padding-top: 10px; padding-left: 20px;")
        self.sandiField.setObjectName("sandiField")
        #Masuk
        self.masukButton = QtWidgets.QPushButton(self.frame_2)
        self.masukButton.setGeometry(QtCore.QRect(60, 360, 291, 41))
        self.masukButton.setStyleSheet("font-family: Arial; font-size: 10pt; font-weight: bold; border: 1px solid #000000; background-color: #fed100; color: #000000; border-radius: 50%; ")
        self.masukButton.setObjectName("masukButton")
        self.daftarButton = QtWidgets.QLabel(self.frame_2)
        self.daftarButton.setGeometry(QtCore.QRect(60, 410, 291, 40))
        self.daftarButton.setStyleSheet("font-family: Arial; font-size: 10pt;")
        #daftar
        self.daftarButton.setObjectName("daftarButton")
        self.daftarButton.clicakble = True
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login", "Login"))
        self.appNameLabel.setText(_translate("MainWindow", "Pharmacy Inventory <br> Management System"))
        self.namaField.setPlaceholderText(_translate("MainWindow", "Unsername"))
        self.sandiField.setPlaceholderText(_translate("MainWindow", "Password"))
        self.masukButton.setText(_translate("MainWindow", "Masuk"))
        self.daftarButton.setText(_translate("MainWindow", "Belum memiliki akun? <u> Daftar <u>"))
