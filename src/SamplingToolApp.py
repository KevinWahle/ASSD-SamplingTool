from PyQt5.QtWidgets import QMainWindow

from src.ui.windows.Main_Window import Ui_MainWindow

import numpy as np
import scipy.signal as ss
import scipy.fft as sf


class SamplingToolApp (QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(SamplingToolApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Se podria hacer desde el designer
        self.f_cb.setCurrentIndex(1)    # Default en kHz, se puede hacer desde el designer
        self.fs_cb.setCurrentIndex(1)    # Default en kHz
        self.xin_plot.setChecked(True)
        self.FAA_ON.setChecked(True)
        self.SH_ON.setChecked(True)
        self.LA_ON.setChecked(True)
        self.xout_ON.setChecked(True)
        self.xout_plot.setChecked(True)

        #TODO: Armar filtro anti alias
        self.FAA = ss.TransferFunction([2.6832e+50], [1.2089e+24, 3.2022e+29, 1.6322e+35, 2.6626e+40, 4.4854e+45, 2.6832e+50])   # Trannsferencia filtro anti alias
        self.FR = self.FAA

        self.update_b.clicked.connect(self.updatePlot)  # Update button

        self.axes = [ self.t_plot.axes, self.f_plot.axes ] 
        self.axes[0].grid(which='both'); self.axes[1].grid(which='both')
        self.axes[1].set_xscale('log')
        
        # Ejes predefinidos

    def updatePlot(self):
        self.t_plot.clear()
        self.f_plot.clear()
        self.calcCurves()
        self.axes[0].grid(which='both'); self.axes[1].grid(which='both')
        self.axes[0].set_ylabel("$Tensión\ [V]$")
        self.axes[1].set_ylabel("$Potencia\ [dB]$")
        # self.axes[1].set_ylabel("$Tensión\ [\hat{V}]$")
        self.axes[0].set_xlabel("$Tiempo\ [s]$")
        self.axes[1].set_xlabel("$Frecuencia\ [Hz]$")
        self.axes[0].legend(); self.axes[1].legend()  
        self.axes[1].set_xscale('log')
        self.t_plot.draw()
        self.f_plot.draw()

    def calcCurves(self):

        A = self.vmax_dsb.value() * 1e-3**(self.vmax_cb.currentIndex())
        f = self.f_dsb.value() * 1e3**(self.f_cb.currentIndex())
        theta = self.theta_dsb.value() * np.pi / 180        # En rad

        fs = self.fs_dsb.value() * 1e3**(self.fs_cb.currentIndex())
        dc = self.DC_dsb.value() / 100

        N = int(1e5)    # Cantidad de muestras en el tiempo

        t = np.linspace(0, 10/f, N)     # Muestra 10 periodos, 1M muestras

        sc = ss.square(2*np.pi*fs*t, duty=1-dc) < 0        # Control signal

        if (self.type_cb.currentIndex() == 0):
            xin = A*np.cos(2*np.pi*f*t + theta)
        elif (self.type_cb.currentIndex() == 1):

            
            t = np.linspace(0, 75/f, N)     # Muestra 10 periodos, 1M muestras
            t2 = t[t<15/(2*f)]
            xin = A*np.sin(2*np.pi*f/5*t2 + theta)
            xin = np.tile(xin, 10)[:len(t)]
        elif (self.type_cb.currentIndex() == 2):
            xin = A*ss.sawtooth(2*np.pi*f*t + theta, width=0.5)

        signal = xin
        # self.axes[0].plot(t, sc)        # DEBUG
        # self.axes[0].plot(t, self.sampleAndHold(signal, sc))        # DEBUG

        if (self.xin_plot.isChecked()):
            self.axes[0].plot(t, signal, label="$X_{in}$", color='C0')
            freq, spect = self.calcfft(signal, t)
            self.axes[1].plot(freq, spect, label="$X_{in}$", color='C0')

        if (self.FAA_ON.isChecked()):
            t, signal,_  = ss.lsim((self.FAA.num, self.FAA.den), U=signal, T=t)  # Calculamos la Rta
        if (self.FAA_plot.isChecked()):
            self.axes[0].plot(t, signal, label="$FAA$", color='C1')
            freq, spect = self.calcfft(signal, t)
            self.axes[1].plot(freq, spect, label="$FAA$", color='C1')
        
        if (self.SH_ON.isChecked()):
            signal = self.sampleAndHold(signal, sc)
        if (self.SH_plot.isChecked()):
            self.axes[0].plot(t, signal, label="$SH$", color='C2')
            freq, spect = self.calcfft(signal, t)
            self.axes[1].plot(freq, spect, label="$SH$", color='C3')

        if (self.LA_ON.isChecked()):
            signal *= sc
        if (self.LA_plot.isChecked()):
            self.axes[0].plot(t, signal, label="$LA$", color='C3')
            freq, spect = self.calcfft(signal, t)
            self.axes[1].plot(freq, spect, label="$LA$", color='C3')
        
        if (self.xout_ON.isChecked()):
            t, signal,_  = ss.lsim((self.FR.num, self.FR.den), U=signal, T=t)  # Calculamos la Rta
        if (self.xout_plot.isChecked()):
            self.axes[0].plot(t, signal, label="$X_{out}$", color='C4')
            freq, spect = self.calcfft(signal, t)
            self.axes[1].plot(freq, spect, label="$X_{out}$", color='C4')
    
    
    #TODO: Se buguea cuando dc cercano a 100%
    def sampleAndHold(self, signal, control):
        res = signal
        for i in range(len(res)):
            if control[i]:
                res[i] = res[i-1]

        return res

    def calcfft(self, signal, t):

        # # Espectro original:
        # spect = sf.fftshift(sf.fft(signal)) * 2/N
        # # spect = 2*(sf.fftshift(sf.fft(signal))/N)**2    # En potencia
        # freq = sf.fftshift(sf.fftfreq(t.shape[-1], d=t[-1]/t.shape[-1]))
        # return freq[len(freq)//2:], spect[len(spect)//2:]

        # Agregando N0 ceros:
        N0 = 10*len(signal)
        
        Ns = int(len(signal) + N0) # Agregamos 0s para incrementar la cantidad de bines

        # spect = sf.fft(signal, Ns) * 2/len(signal)        # En tension
        spect = sf.fft(signal, Ns)
        spect = 2*abs(spect/len(signal))**2    # En potencia
        spect = spect[:len(spect)//2]   # Me quedo con los armónicos de frec positiva
        spect = 10*np.log10(spect)     # En dB
        
        # spect = 10*np.log10(spect*1e3)     # En dBm
        freq = sf.fftfreq(Ns, d=t[-1]/len(t))
        freq = freq[:len(freq)//2]  # Me quedo con los armónicos de frec positiva
        return freq, spect
    