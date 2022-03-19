import sys
from PyQt5.QtWidgets import QApplication
from src.SamplingToolApp import SamplingToolApp

app = QApplication(sys.argv)
win = SamplingToolApp()
win.show()
sys.exit(app.exec())