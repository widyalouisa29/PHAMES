import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from add_stock_page import Ui_AddStockWindow  
from PyQt5.QtCore import Qt, QSysInfo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_AddStockWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    QApplication.setAttribute
    QApplication.setAttribute
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
