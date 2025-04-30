import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QDate

class LowStockAlert(QWidget):
    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Low Stock Alert')

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        self.check_button = QPushButton('Check Stock')
        self.check_button.clicked.connect(self.checkStock)
        self.layout.addWidget(self.check_button)

        self.setLayout(self.layout)

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Expiration Date"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Category"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Stock"))
        # self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Alert"))

        for i, item in enumerate(self.dataset):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item['name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(item['expiration_date']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(item['Category']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(item['stock'])))

    def checkStock(self):
        self.checkStockLastYear()
        self.checkStockNow()

    def checkStockLastYear(self):
        current_date = QDate.currentDate()
        last_year_date = current_date.addYears(-1)
        for data in self.dataset:
            date = [int(i) for i in data["expiration_date"].split("-")]
            expiration_date = QDate(date[0], date[1], date[2])
            stock = data["stock"]
            if expiration_date.year() < last_year_date.year() and stock < data["stock"]:
                self.showMessageBox(data["name"], "Periksa Stok Tahun Lalu",
                                    f"Stok obat {data['name']} pada tahun lalu adalah {data['stock']} unit. "
                                    f"Mohon periksa kembali stok tersebut.")

    def checkStockNow(self):
        current_date = QDate.currentDate()
        for data in self.dataset:
            date = [int(i) for i in data["expiration_date"].split("-")]
            expiration_date = QDate(date[0], date[1], date[2])
            stock = data["stock"]
            min_stock_level= data["min_stock"]
            if expiration_date <= current_date:
                self.showMessageBox(data["name"], "Tidak Perlu Restock",
                                    f"Obat {data['name']} sudah kadaluarsa, tidak perlu restock.")
            elif expiration_date.daysTo(current_date) <= 30 and stock < min_stock_level:
                self.showMessageBox(data["name"], "Butuh Restock",
                                    f"Stok obat {data['name']} akan habis sebelum tanggal kadaluarsa. "
                                    f"Mohon restock segera.")
            elif expiration_date > current_date and stock < min_stock_level:
                self.showMessageBox(data["name"], "Butuh Restock",
                                    f"Stok obat {data['name']} kurang dari minimal, "
                                    f"mohon restock segera.")
    def showMessageBox(self, name, title, message):
        icon = QMessageBox.Warning
        if title == "Periksa Stok Tahun Lalu":
            icon = QMessageBox.Information
        reply = QMessageBox.question(self, title, message, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            print(f"User clicked OK for {name}")
    
