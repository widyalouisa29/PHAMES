import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QMessageBox
from PyQt5.QtCore import Qt, QSysInfo
import mysql.connector

from login_page import Ui_LoginWindow  
from daftar_page import Ui_DaftarWindow
from home_page import Ui_HomeWindow
from add_stock_page import Ui_AddStockWindow
from ViewStock import ViewStock
from ExpirationAlert import ExpirationAlert
from LowStockAlert import LowStockAlert

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_LoginWindow()
        self.dataset = []
        self.ui.setupUi(self)

        self.ui.masukButton.clicked.connect(self.login)
        self.ui.daftarButton.mousePressEvent = self.openDaftarWindow

    def openDaftarWindow(self, event):
        self.ui = Ui_DaftarWindow()
        self.ui.setupUi(self)

        self.ui.masukButton.clicked.connect(self.daftar)
    
    def openHomeWindow(self):
        self.ui = Ui_HomeWindow()

        try:
            self.dataset = []
            conn = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="",  
                database="pharmacy_db(1)" 
            )
            cursor = conn.cursor()
            query = "SELECT nama_obat AS name, tanggal_expiry_obat AS expiration_date, jumlah_stok_obat AS stock, minimum_stock AS min_stock, jenis_obat AS Category FROM obat"
            cursor.execute(query)
            for row in cursor:
                self.dataset.append({
                    "name": row[0],
                    "expiration_date": row[1].strftime("%Y-%m-%d").replace("-0", "-"),
                    "stock": row[2],
                    "min_stock": row[3],
                    "Category": row[4]
                })
        except mysql.connector.Error as e:
            print(e)
            self.show_error_dialog("Gagal terhubung ke database!")
            return
        
        lowStock = LowStockAlert(self.dataset)
        viewStock = ViewStock(self.dataset)
        expired = ExpirationAlert(self.dataset)

        self.ui.setupUi(self)
        self.ui.addStockIcon.mousePressEvent = self.openAddStockWindow
        self.ui.addStockLabel.mousePressEvent = self.openAddStockWindow
        self.ui.addStockDescriptionLabel.mousePressEvent = self.openAddStockWindow
        self.ui.lowStockButton.clicked.connect(lambda x: lowStock.show())
        self.ui.viewStockButton.clicked.connect(lambda x: viewStock.show())
        self.ui.expiryButton.clicked.connect(lambda x: expired.show())
    
    def openLoginWindow(self):
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.masukButton.clicked.connect(self.login)
        self.ui.daftarButton.mousePressEvent = self.openDaftarWindow

    def openAddStockWindow(self, event):
        self.ui = Ui_AddStockWindow()
        self.ui.setupUi(self)

        self.ui.simpanObatButton.clicked.connect(self.saveObat)
        self.ui.backButton.clicked.connect(self.openHomeWindow)
    
    # def openLowStockWindow(self, event):
    #     lowStock = LowStockAlert([])
    #     lowStock.show()

    def saveObat(self):
        namaObat = self.ui.namaObatField.text()
        jenisObat = self.ui.typeComboBox.currentText()
        jumlahStokObat = int(self.ui.stockSpinBox.value())
        tanggalExpiryObat =  self.ui.expiryObatDateEdit.date().toString("yyyy-MM-dd")

        if namaObat == "" or jumlahStokObat == 0:
            self.show_warning_dialog("Semua field harus diisi!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="",  
                database="pharmacy_db(1)" 
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(e)
            self.show_error_dialog("Gagal terhubung ke database!")
            return

        query = "INSERT INTO obat (nama_obat, tanggal_expiry_obat, jumlah_stok_obat, jenis_obat) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (namaObat, tanggalExpiryObat, jumlahStokObat, jenisObat))
        conn.commit() 

        self.show_success_dialog("Penambahan obat berhasil! Silakan login.")
        self.ui.namaObatField.setText("")
        self.ui.stockSpinBox.setValue(0)
        conn.close()


    def daftar(self):
        username = self.ui.namaField.toPlainText()
        password = self.ui.sandiField.toPlainText()

        if username == "" or password == "":
            self.show_warning_dialog("Username dan password tidak boleh kosong!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="",  
                database="pharmacy_db(1)" 
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(e)
            self.show_error_dialog("Gagal terhubung ke database!")
            return

        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        if cursor.fetchone() is not None:
            self.show_error_dialog("Username sudah ada!")
            return

        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit() 

        self.show_success_dialog("Pendaftaran berhasil! Silakan login.")
        conn.close()
        self.openLoginWindow()

    def login(self):
        username = self.ui.namaField.toPlainText()
        password = self.ui.sandiField.toPlainText()
        
        if username == "" or password == "":
            self.show_warning_dialog("Username dan password tidak boleh kosong!")
            return
        
        try:
            conn = mysql.connector.connect(
                host="localhost", 
                user="root",  
                password="",  
                database="pharmacy_db(1)" 
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(e)
            self.show_error_dialog("Gagal terhubung ke database!")
            return

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        if cursor.fetchone() is None:
            self.show_error_dialog("Username atau password salah!")
            return

        # Login successful
        self.show_success_dialog("Login berhasil!")
        self.openHomeWindow()
        conn.close()

    def show_warning_dialog(self, message):
        warning_dialog = QMessageBox(QMessageBox.Warning, "Peringatan", message)
        warning_dialog.exec_()

    def show_error_dialog(self, message):
        error_dialog = QMessageBox(QMessageBox.Critical, "Kesalahan", message)
        error_dialog.exec_()

    def show_success_dialog(self, message):
        success_dialog = QMessageBox(QMessageBox.Information, "Sukses", message)
        success_dialog.exec_()

if __name__ == "__main__":
    QApplication.setAttribute
    QApplication.setAttribute

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())