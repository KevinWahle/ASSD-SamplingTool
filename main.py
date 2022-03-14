import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.ui.windows.Main_Window import Ui_MainWindow

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())