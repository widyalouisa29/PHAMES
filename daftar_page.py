from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

class Ui_DaftarWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Daftar")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)

        app = QApplication.instance()
        app.setStyle("Fusion")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.frame.setStyleSheet("background-image: url('login_bg.png')")#frame 1
        
        self.frame.setObjectName("frame")#frame 2
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(399, 0, 401, 600))
        self.frame_2.setStyleSheet("background-color: #8c7bff;")
        
        self.frame_2.setObjectName("frame_2")
        self.appNameLabel = QtWidgets.QLabel(self.frame_2)
        self.appNameLabel.setGeometry(QtCore.QRect(60, 80, 315, 90))#label 
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        font.setBold(True)#Label pharmacy
        self.appNameLabel.setFont(font)
        # self.appNameLabel.setAlignment(QtCore.Qt.Qt.AlignmentFlag.AlignCenter)
        self.appNameLabel.setObjectName("appNameLabel")
        self.appNameLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.namaField = QtWidgets.QTextEdit(self.frame_2)
        self.namaField.setGeometry(QtCore.QRect(60, 230, 291, 49))#unsername
        font = QtGui.QFont()
        font.setFamily("Helvetica")#unsername
        font.setPointSize(10)#unsername
        font.setBold(False)#unsername
        self.namaField.setFont(font)
        self.namaField.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; padding-top: 10px; padding-bottom:10px; padding-left: 20px;")
  
        self.namaField.setObjectName("namaField")
        self.sandiField = QtWidgets.QTextEdit(self.frame_2)
        self.sandiField.setGeometry(QtCore.QRect(60, 294, 291, 49))#password
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        self.sandiField.setFont(font)
        self.sandiField.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 50%; padding-top: 10px; padding-bottom:10px; padding-left: 20px;")
        # self.sandiField.setFrameShape(QtCore.Qt.QFrame.Shape.Box)
        self.sandiField.setObjectName("sandiField")
        self.masukButton = QtWidgets.QPushButton(self.frame_2)
        self.masukButton.setGeometry(QtCore.QRect(60, 365, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        self.masukButton.setFont(font)
        self.masukButton.setStyleSheet(" border: 1px solid #000000; background-color: #fed100; color: #000000; border-radius: 50%; ")
        self.masukButton.setObjectName("masukButton")
        # self.daftarButton = QtWidgets.QLabel(self.frame_2)
        # self.daftarButton.setGeometry(QtCore.QRect(60, 430, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        # self.daftarButton.setFont(font)
        # self.daftarButton.setAlignment(QtCore.Qt.Qt.AlignmentFlag.AlignCenter)
        # self.daftarButton.setObjectName("daftarButton")
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
        MainWindow.setWindowTitle(_translate("Daftar", "Daftar"))
        self.appNameLabel.setText(_translate("MainWindow", "Pharmacy Inventory <br> Management System"))
        self.namaField.setPlaceholderText(_translate("MainWindow", "Unsername"))
        self.sandiField.setPlaceholderText(_translate("MainWindow", "Password"))
        self.masukButton.setText(_translate("MainWindow", "Daftar"))
        # self.daftarButton.setText(_translate("MainWindow", "Belum memiliki akun? <u> Daftar <u>"))
