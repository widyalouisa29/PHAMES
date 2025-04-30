import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import QDate

def zero_pad_date(date_str):
    parts = date_str.split('-')
    year = parts[0]
    month = parts[1].zfill(2)
    day = parts[2].zfill(2)
    zero_padded_date = f"{year}-{month}-{day}"
    return zero_padded_date

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            leftDate = QDate.fromString(zero_pad_date(left_half[i]["expiration_date"]), "yyyy-MM-dd")
            rightDate = QDate.fromString(zero_pad_date(right_half[j]["expiration_date"]), "yyyy-MM-dd")
            if leftDate.daysTo(rightDate) > 0:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

class ViewStock(QWidget):
    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset
        merge_sort(self.dataset)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('View Stock')

        self.createTable()
        self.createCategoryComboBox()
        self.createViewStockButton()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.category_combo_box)
        self.layout.addWidget(self.view_stock_button)

        self.setLayout(self.layout)

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Expiration Date"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Category"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Stock"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Status"))
        current_date = QDate.currentDate()
        for i, item in enumerate(self.dataset):
            self.tableWidget.insertRow(i)
            date = [int(i) for i in item["expiration_date"].split("-")]
            expiration_date = QDate(date[0], date[1], date[2])
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item["name"]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(item["expiration_date"]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(item["Category"]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(item["stock"])))
            if expiration_date.daysTo(current_date) <= 30 and item["stock"] < item["min_stock"]:
                self.tableWidget.setItem(i, 4, QTableWidgetItem('Expiration date is near and stock is low!'))
            elif expiration_date < current_date and item["stock"] > 0:
                self.tableWidget.setItem(i, 4, QTableWidgetItem('Expired but still has stock!'))
            else:
                self.tableWidget.setItem(i, 4, QTableWidgetItem(''))

    def createCategoryComboBox(self):
        self.category_combo_box = QComboBox()
        self.category_combo_box.addItem('All')
        self.category_combo_box.addItem('Obat Keras')
        self.category_combo_box.addItem('Obat Bebas')
        self.category_combo_box.addItem('Obat Bebas Terikat')
        self.category_combo_box.addItem('Obat Psikotropika')

        self.category_combo_box.currentIndexChanged.connect(self.filterByCategory)

    def createViewStockButton(self):
        self.view_stock_button = QPushButton('View Stock')
        # self.view_stock_button.clicked.connect(self.viewStock)

    def filterByCategory(self, index):
        category = self.category_combo_box.itemText(index)
        current_date = QDate.currentDate()

        if category == 'All':
            self.tableWidget.setRowCount(0)
            for i, item in enumerate(self.dataset):
                self.tableWidget.insertRow(i)
                date = [int(i) for i in item["expiration_date"].split("-")]
                expiration_date = QDate(date[0], date[1], date[2])
                self.tableWidget.setItem(i, 0, QTableWidgetItem(item["name"]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(item["expiration_date"]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(item["Category"]))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(item["stock"])))
                if expiration_date.daysTo(current_date) <= 30 and item["stock"] < item["min_stock"]:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem('Expiration date is near and stock is low!'))
                elif expiration_date < current_date and item["stock"] > 0:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem('Expired but still has stock!'))
                else:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(''))
        else:
            self.tableWidget.setRowCount(0)
            for i, item in enumerate([x for x in self.dataset if x["Category"] == category]):
                self.tableWidget.insertRow(i)
                date = [int(i) for i in item["expiration_date"].split("-")]
                expiration_date = QDate(date[0], date[1], date[2])
                self.tableWidget.setItem(i, 0, QTableWidgetItem(item["name"]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(item["expiration_date"]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(item["Category"]))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(item["stock"])))
                if expiration_date.daysTo(current_date) <= 30 and item["stock"] < item["min_stock"]:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem('Expiration date is near and stock is low!'))
                elif expiration_date < current_date and item["stock"] > 0:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem('Expired but still has stock!'))
                else:
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(''))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ViewStock()
#     window.show()
#     sys.exit(app.exec_())