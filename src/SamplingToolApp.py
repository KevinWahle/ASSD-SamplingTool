from PyQt5.QtWidgets import QMainWindow

from src.ui.windows.Main_Window import Ui_MainWindow

import numpy as np
import scipy.signal as ss

class SamplingToolApp (QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(SamplingToolApp, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.f_cb.setCurrentIndex(1)    # Default en kHz, se puede hacer desde el designer
        self.fs_cb.setCurrentIndex(1)    # Default en kHz, se puede hacer desde el designer

        # self.FAA = ss.TransferFunction()    #TODO: Armar filtro anti alias

        self.update_b.clicked.connect(self.updatePlot)  # Update button

        self.axes = [ self.t_plot.axes, self.f_plot.axes ] 

    def updatePlot(self):
        self.calcCurves()
        self.t_plot.draw()
        self.f_plot.draw()

    def calcCurves(self):

        A = self.vmax_dsb.value() * 1e-3**(self.vmax_cb.currentIndex())
        print(A)
        f = self.f_dsb.value() * 1e3**(self.f_cb.currentIndex())
        print(f)
        theta = self.theta_dsb.value() * np.pi / 180        # En rad

        fs = self.fs_dsb.value()
        dc = self.DC_dsb.value()

        t = np.linspace(0, 10/f, int(1e6))     # Muestra 10 periodos, 1M muestras

        if (self.type_cb.currentIndex() == 0):
            xin = A*np.cos(2*np.pi*f*t + theta)
        elif (self.type_cb.currentIndex() == 1):
            xin = A*np.sin(2*np.pi*f/5*t + theta)
        elif (self.type_cb.currentIndex() == 2):
            xin = A*ss.sawtooth(2*np.pi*f*t + theta, width=0.5)

        if (self.xin_plot.isChecked()):
            self.axes[0].plot(t,xin)
            #TODO: plotear espectro

        if (self.FAA_ON.isChecked()):
            pass
        if (self.FAA_plot.isChecked()):
            pass
        
        if (self.SH_ON.isChecked()):
            pass
        if (self.SH_plot.isChecked()):
            pass

        if (self.LA_ON.isChecked()):
            pass
        if (self.LA_plot.isChecked()):
            pass
        
        if (self.xout_ON.isChecked()):
            pass
        if (self.xout_plot.isChecked()):
            pass