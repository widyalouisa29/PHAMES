import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from home_page import Ui_HomeWindow  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
    def openExpiryAlert(self):
        self.ui = Ui_HomeWindow
        self.ui.setupUi(self)
    def openLowStockAlert(self):
        self.ui = Ui_HomeWindow
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
