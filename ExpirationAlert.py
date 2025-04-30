import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QMessageBox,QPushButton
from PyQt5.QtCore import Qt, QDate

class ExpirationAlert(QWidget):
    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Expiration Alert')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Medicine'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Expiration Date'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Status'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Category Obat'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Stock'))
        self.layout.addWidget(self.tableWidget)
        self.check_button = QPushButton('Check Expired')
        self.check_button.clicked.connect(self.checkExpirationDates)
        self.layout.addWidget(self.check_button)
        self.updateTable(self.dataset)

    def checkExpirationDates(self):
        self.showAlerts(self.dataset)

    def updateTable(self, dataset):
        for i, data in enumerate(dataset):
            self.tableWidget.insertRow(i)      
            self.tableWidget.setItem(i, 0, QTableWidgetItem(data['name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data['expiration_date']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data['Category']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(data['stock'])))
            status = self.getExpirationStatus(data['expiration_date'])
            self.tableWidget.setItem(i, 2, QTableWidgetItem(status))

    def getExpirationStatus(self, expiration_date):
            date = [int(i) for i in expiration_date.split("-")]
            date = QDate(date[0], date[1], date[2])
            if date < QDate.currentDate().addDays(-17):
                return 'Expired'
            elif date < QDate.currentDate().addDays(17):
                return 'Near Expiration'
            elif date < QDate.currentDate().addDays(30):
                return 'Near Expiration'
            else:
                 return 'Aman'
    
    def showAlerts(self, medicines):
        for medicine in medicines:
            status = self.getExpirationStatus(medicine['expiration_date'])
            if status != 'Aman':
                self.showAlert(medicine['name'], status, medicine['expiration_date'])

    def showAlert(self, medicine_name, status, expiration_date):
        message = f'Medicine {medicine_name} is {"Expired" if status == "Expired" else "near expiration date"}! ({"Expired on" if status == "Expired" else "Expired on"} {expiration_date})'
        QMessageBox.warning(self, 'Expiry Alert', message)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ExpirationAlert()
#     ex.show()
#     sys.exit(app.exec_())