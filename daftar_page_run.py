import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from daftar_page import Ui_DaftarWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_DaftarWindow()
        self.ui.setupUi(self)

        self.ui.masukButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.namaField.toPlainText()
        password = self.ui.sandiField.toPlainText()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
