from PyQt5.QtWidgets import QMainWindow

from src.ui.windows.Main_Window import Ui_MainWindow

class SamplingToolApp (QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(SamplingToolApp, self).__init__(*args, **kwargs)
        self.setupUi(self)