# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_l = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_l.sizePolicy().hasHeightForWidth())
        self.input_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.input_l.setFont(font)
        self.input_l.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.input_l.setFrameShadow(QtWidgets.QFrame.Plain)
        self.input_l.setTextFormat(QtCore.Qt.PlainText)
        self.input_l.setAlignment(QtCore.Qt.AlignCenter)
        self.input_l.setWordWrap(False)
        self.input_l.setObjectName("input_l")
        self.verticalLayout_2.addWidget(self.input_l)
        self.type_cb = QtWidgets.QComboBox(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_cb.sizePolicy().hasHeightForWidth())
        self.type_cb.setSizePolicy(sizePolicy)
        self.type_cb.setMinimumSize(QtCore.QSize(150, 0))
        self.type_cb.setObjectName("type_cb")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.verticalLayout_2.addWidget(self.type_cb)
        self.vmaxWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vmaxWidget.sizePolicy().hasHeightForWidth())
        self.vmaxWidget.setSizePolicy(sizePolicy)
        self.vmaxWidget.setObjectName("vmaxWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.vmaxWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.vmax_l = QtWidgets.QLabel(self.vmaxWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vmax_l.sizePolicy().hasHeightForWidth())
        self.vmax_l.setSizePolicy(sizePolicy)
        self.vmax_l.setMinimumSize(QtCore.QSize(32, 0))
        self.vmax_l.setAlignment(QtCore.Qt.AlignCenter)
        self.vmax_l.setObjectName("vmax_l")
        self.horizontalLayout_4.addWidget(self.vmax_l)
        self.vmax_dsb = QtWidgets.QDoubleSpinBox(self.vmaxWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vmax_dsb.sizePolicy().hasHeightForWidth())
        self.vmax_dsb.setSizePolicy(sizePolicy)
        self.vmax_dsb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.vmax_dsb.setMaximum(999.99)
        self.vmax_dsb.setProperty("value", 1.0)
        self.vmax_dsb.setObjectName("vmax_dsb")
        self.horizontalLayout_4.addWidget(self.vmax_dsb)
        self.vmax_cb = QtWidgets.QComboBox(self.vmaxWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vmax_cb.sizePolicy().hasHeightForWidth())
        self.vmax_cb.setSizePolicy(sizePolicy)
        self.vmax_cb.setMaximumSize(QtCore.QSize(55, 16777215))
        self.vmax_cb.setObjectName("vmax_cb")
        self.vmax_cb.addItem("")
        self.vmax_cb.addItem("")
        self.vmax_cb.addItem("")
        self.horizontalLayout_4.addWidget(self.vmax_cb)
        self.verticalLayout_2.addWidget(self.vmaxWidget)
        self.fWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fWidget.sizePolicy().hasHeightForWidth())
        self.fWidget.setSizePolicy(sizePolicy)
        self.fWidget.setObjectName("fWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.f_l = QtWidgets.QLabel(self.fWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_l.sizePolicy().hasHeightForWidth())
        self.f_l.setSizePolicy(sizePolicy)
        self.f_l.setMinimumSize(QtCore.QSize(32, 0))
        self.f_l.setAlignment(QtCore.Qt.AlignCenter)
        self.f_l.setObjectName("f_l")
        self.horizontalLayout_7.addWidget(self.f_l)
        self.f_dsb = QtWidgets.QDoubleSpinBox(self.fWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_dsb.sizePolicy().hasHeightForWidth())
        self.f_dsb.setSizePolicy(sizePolicy)
        self.f_dsb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_dsb.setMaximum(999.99)
        self.f_dsb.setProperty("value", 10.0)
        self.f_dsb.setObjectName("f_dsb")
        self.horizontalLayout_7.addWidget(self.f_dsb)
        self.f_cb = QtWidgets.QComboBox(self.fWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_cb.sizePolicy().hasHeightForWidth())
        self.f_cb.setSizePolicy(sizePolicy)
        self.f_cb.setMaximumSize(QtCore.QSize(55, 16777215))
        self.f_cb.setObjectName("f_cb")
        self.f_cb.addItem("")
        self.f_cb.addItem("")
        self.f_cb.addItem("")
        self.horizontalLayout_7.addWidget(self.f_cb)
        self.verticalLayout_2.addWidget(self.fWidget)
        self.thetaWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thetaWidget.sizePolicy().hasHeightForWidth())
        self.thetaWidget.setSizePolicy(sizePolicy)
        self.thetaWidget.setObjectName("thetaWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.thetaWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 13)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.theta_l = QtWidgets.QLabel(self.thetaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theta_l.sizePolicy().hasHeightForWidth())
        self.theta_l.setSizePolicy(sizePolicy)
        self.theta_l.setMinimumSize(QtCore.QSize(32, 0))
        self.theta_l.setAlignment(QtCore.Qt.AlignCenter)
        self.theta_l.setObjectName("theta_l")
        self.horizontalLayout_8.addWidget(self.theta_l)
        self.theta_dsb = QtWidgets.QDoubleSpinBox(self.thetaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theta_dsb.sizePolicy().hasHeightForWidth())
        self.theta_dsb.setSizePolicy(sizePolicy)
        self.theta_dsb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.theta_dsb.setMaximum(999.99)
        self.theta_dsb.setObjectName("theta_dsb")
        self.horizontalLayout_8.addWidget(self.theta_dsb)
        self.theta_cb = QtWidgets.QComboBox(self.thetaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theta_cb.sizePolicy().hasHeightForWidth())
        self.theta_cb.setSizePolicy(sizePolicy)
        self.theta_cb.setMaximumSize(QtCore.QSize(55, 16777215))
        self.theta_cb.setObjectName("theta_cb")
        self.theta_cb.addItem("")
        self.horizontalLayout_8.addWidget(self.theta_cb)
        self.verticalLayout_2.addWidget(self.thetaWidget)
        self.input_l_2 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_l_2.sizePolicy().hasHeightForWidth())
        self.input_l_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.input_l_2.setFont(font)
        self.input_l_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.input_l_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.input_l_2.setTextFormat(QtCore.Qt.PlainText)
        self.input_l_2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_l_2.setWordWrap(False)
        self.input_l_2.setObjectName("input_l_2")
        self.verticalLayout_2.addWidget(self.input_l_2)
        self.TWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TWidget.sizePolicy().hasHeightForWidth())
        self.TWidget.setSizePolicy(sizePolicy)
        self.TWidget.setObjectName("TWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.TWidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fs_l = QtWidgets.QLabel(self.TWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_l.sizePolicy().hasHeightForWidth())
        self.fs_l.setSizePolicy(sizePolicy)
        self.fs_l.setMinimumSize(QtCore.QSize(32, 0))
        self.fs_l.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_l.setObjectName("fs_l")
        self.horizontalLayout_9.addWidget(self.fs_l)
        self.fs_dsb = QtWidgets.QDoubleSpinBox(self.TWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_dsb.sizePolicy().hasHeightForWidth())
        self.fs_dsb.setSizePolicy(sizePolicy)
        self.fs_dsb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fs_dsb.setMaximum(999.99)
        self.fs_dsb.setProperty("value", 10.0)
        self.fs_dsb.setObjectName("fs_dsb")
        self.horizontalLayout_9.addWidget(self.fs_dsb)
        self.fs_cb = QtWidgets.QComboBox(self.TWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_cb.sizePolicy().hasHeightForWidth())
        self.fs_cb.setSizePolicy(sizePolicy)
        self.fs_cb.setMaximumSize(QtCore.QSize(55, 16777215))
        self.fs_cb.setObjectName("fs_cb")
        self.fs_cb.addItem("")
        self.fs_cb.addItem("")
        self.fs_cb.addItem("")
        self.horizontalLayout_9.addWidget(self.fs_cb)
        self.verticalLayout_2.addWidget(self.TWidget)
        self.DCWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DCWidget.sizePolicy().hasHeightForWidth())
        self.DCWidget.setSizePolicy(sizePolicy)
        self.DCWidget.setObjectName("DCWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.DCWidget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 13)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.DC_l = QtWidgets.QLabel(self.DCWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DC_l.sizePolicy().hasHeightForWidth())
        self.DC_l.setSizePolicy(sizePolicy)
        self.DC_l.setMinimumSize(QtCore.QSize(32, 0))
        self.DC_l.setAlignment(QtCore.Qt.AlignCenter)
        self.DC_l.setObjectName("DC_l")
        self.horizontalLayout_10.addWidget(self.DC_l)
        self.DC_dsb = QtWidgets.QDoubleSpinBox(self.DCWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DC_dsb.sizePolicy().hasHeightForWidth())
        self.DC_dsb.setSizePolicy(sizePolicy)
        self.DC_dsb.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DC_dsb.setMaximum(100.0)
        self.DC_dsb.setProperty("value", 50.0)
        self.DC_dsb.setObjectName("DC_dsb")
        self.horizontalLayout_10.addWidget(self.DC_dsb)
        self.DC_cb = QtWidgets.QComboBox(self.DCWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DC_cb.sizePolicy().hasHeightForWidth())
        self.DC_cb.setSizePolicy(sizePolicy)
        self.DC_cb.setMaximumSize(QtCore.QSize(55, 16777215))
        self.DC_cb.setObjectName("DC_cb")
        self.DC_cb.addItem("")
        self.horizontalLayout_10.addWidget(self.DC_cb)
        self.verticalLayout_2.addWidget(self.DCWidget)
        self.stages_l = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stages_l.sizePolicy().hasHeightForWidth())
        self.stages_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.stages_l.setFont(font)
        self.stages_l.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stages_l.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stages_l.setTextFormat(QtCore.Qt.PlainText)
        self.stages_l.setAlignment(QtCore.Qt.AlignCenter)
        self.stages_l.setWordWrap(False)
        self.stages_l.setObjectName("stages_l")
        self.verticalLayout_2.addWidget(self.stages_l)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stages_l_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stages_l_2.sizePolicy().hasHeightForWidth())
        self.stages_l_2.setSizePolicy(sizePolicy)
        self.stages_l_2.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.stages_l_2.setFont(font)
        self.stages_l_2.setAlignment(QtCore.Qt.AlignCenter)
        self.stages_l_2.setObjectName("stages_l_2")
        self.horizontalLayout_3.addWidget(self.stages_l_2)
        self.ON_l = QtWidgets.QLabel(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ON_l.sizePolicy().hasHeightForWidth())
        self.ON_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.ON_l.setFont(font)
        self.ON_l.setAlignment(QtCore.Qt.AlignCenter)
        self.ON_l.setObjectName("ON_l")
        self.horizontalLayout_3.addWidget(self.ON_l)
        self.plot_l = QtWidgets.QLabel(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_l.sizePolicy().hasHeightForWidth())
        self.plot_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.plot_l.setFont(font)
        self.plot_l.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_l.setObjectName("plot_l")
        self.horizontalLayout_3.addWidget(self.plot_l)
        self.verticalLayout_2.addWidget(self.horizontalWidget_2)
        self.xinWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xinWidget.sizePolicy().hasHeightForWidth())
        self.xinWidget.setSizePolicy(sizePolicy)
        self.xinWidget.setObjectName("xinWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.xinWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(50)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.xin_l = QtWidgets.QLabel(self.xinWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xin_l.sizePolicy().hasHeightForWidth())
        self.xin_l.setSizePolicy(sizePolicy)
        self.xin_l.setMinimumSize(QtCore.QSize(46, 0))
        self.xin_l.setAlignment(QtCore.Qt.AlignCenter)
        self.xin_l.setObjectName("xin_l")
        self.horizontalLayout_11.addWidget(self.xin_l)
        self.xin_plot = QtWidgets.QCheckBox(self.xinWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xin_plot.sizePolicy().hasHeightForWidth())
        self.xin_plot.setSizePolicy(sizePolicy)
        self.xin_plot.setText("")
        self.xin_plot.setObjectName("xin_plot")
        self.horizontalLayout_11.addWidget(self.xin_plot)
        self.verticalLayout_2.addWidget(self.xinWidget)
        self.FAAWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FAAWidget.sizePolicy().hasHeightForWidth())
        self.FAAWidget.setSizePolicy(sizePolicy)
        self.FAAWidget.setObjectName("FAAWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.FAAWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.FAA_l = QtWidgets.QLabel(self.FAAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FAA_l.sizePolicy().hasHeightForWidth())
        self.FAA_l.setSizePolicy(sizePolicy)
        self.FAA_l.setMinimumSize(QtCore.QSize(46, 0))
        self.FAA_l.setAlignment(QtCore.Qt.AlignCenter)
        self.FAA_l.setObjectName("FAA_l")
        self.horizontalLayout_12.addWidget(self.FAA_l)
        self.FAA_ON = QtWidgets.QCheckBox(self.FAAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FAA_ON.sizePolicy().hasHeightForWidth())
        self.FAA_ON.setSizePolicy(sizePolicy)
        self.FAA_ON.setText("")
        self.FAA_ON.setObjectName("FAA_ON")
        self.horizontalLayout_12.addWidget(self.FAA_ON)
        self.FAA_plot = QtWidgets.QCheckBox(self.FAAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FAA_plot.sizePolicy().hasHeightForWidth())
        self.FAA_plot.setSizePolicy(sizePolicy)
        self.FAA_plot.setText("")
        self.FAA_plot.setObjectName("FAA_plot")
        self.horizontalLayout_12.addWidget(self.FAA_plot)
        self.verticalLayout_2.addWidget(self.FAAWidget)
        self.SHWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SHWidget.sizePolicy().hasHeightForWidth())
        self.SHWidget.setSizePolicy(sizePolicy)
        self.SHWidget.setObjectName("SHWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.SHWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(13)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.SH_l = QtWidgets.QLabel(self.SHWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SH_l.sizePolicy().hasHeightForWidth())
        self.SH_l.setSizePolicy(sizePolicy)
        self.SH_l.setMinimumSize(QtCore.QSize(46, 0))
        self.SH_l.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_l.setObjectName("SH_l")
        self.horizontalLayout_13.addWidget(self.SH_l)
        self.SH_ON = QtWidgets.QCheckBox(self.SHWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SH_ON.sizePolicy().hasHeightForWidth())
        self.SH_ON.setSizePolicy(sizePolicy)
        self.SH_ON.setText("")
        self.SH_ON.setObjectName("SH_ON")
        self.horizontalLayout_13.addWidget(self.SH_ON)
        self.SH_plot = QtWidgets.QCheckBox(self.SHWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SH_plot.sizePolicy().hasHeightForWidth())
        self.SH_plot.setSizePolicy(sizePolicy)
        self.SH_plot.setText("")
        self.SH_plot.setObjectName("SH_plot")
        self.horizontalLayout_13.addWidget(self.SH_plot)
        self.verticalLayout_2.addWidget(self.SHWidget)
        self.LAWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LAWidget.sizePolicy().hasHeightForWidth())
        self.LAWidget.setSizePolicy(sizePolicy)
        self.LAWidget.setObjectName("LAWidget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.LAWidget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(13)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.LA_l = QtWidgets.QLabel(self.LAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LA_l.sizePolicy().hasHeightForWidth())
        self.LA_l.setSizePolicy(sizePolicy)
        self.LA_l.setMinimumSize(QtCore.QSize(46, 0))
        self.LA_l.setAlignment(QtCore.Qt.AlignCenter)
        self.LA_l.setObjectName("LA_l")
        self.horizontalLayout_14.addWidget(self.LA_l)
        self.LA_ON = QtWidgets.QCheckBox(self.LAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LA_ON.sizePolicy().hasHeightForWidth())
        self.LA_ON.setSizePolicy(sizePolicy)
        self.LA_ON.setText("")
        self.LA_ON.setObjectName("LA_ON")
        self.horizontalLayout_14.addWidget(self.LA_ON)
        self.LA_plot = QtWidgets.QCheckBox(self.LAWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LA_plot.sizePolicy().hasHeightForWidth())
        self.LA_plot.setSizePolicy(sizePolicy)
        self.LA_plot.setText("")
        self.LA_plot.setObjectName("LA_plot")
        self.horizontalLayout_14.addWidget(self.LA_plot)
        self.verticalLayout_2.addWidget(self.LAWidget)
        self.xoutWidget = QtWidgets.QWidget(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xoutWidget.sizePolicy().hasHeightForWidth())
        self.xoutWidget.setSizePolicy(sizePolicy)
        self.xoutWidget.setObjectName("xoutWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.xoutWidget)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_15.setSpacing(13)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.xout_l = QtWidgets.QLabel(self.xoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xout_l.sizePolicy().hasHeightForWidth())
        self.xout_l.setSizePolicy(sizePolicy)
        self.xout_l.setMinimumSize(QtCore.QSize(46, 0))
        self.xout_l.setAlignment(QtCore.Qt.AlignCenter)
        self.xout_l.setObjectName("xout_l")
        self.horizontalLayout_15.addWidget(self.xout_l)
        self.xout_ON = QtWidgets.QCheckBox(self.xoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xout_ON.sizePolicy().hasHeightForWidth())
        self.xout_ON.setSizePolicy(sizePolicy)
        self.xout_ON.setText("")
        self.xout_ON.setObjectName("xout_ON")
        self.horizontalLayout_15.addWidget(self.xout_ON)
        self.xout_plot = QtWidgets.QCheckBox(self.xoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xout_plot.sizePolicy().hasHeightForWidth())
        self.xout_plot.setSizePolicy(sizePolicy)
        self.xout_plot.setText("")
        self.xout_plot.setObjectName("xout_plot")
        self.horizontalLayout_15.addWidget(self.xout_plot)
        self.verticalLayout_2.addWidget(self.xoutWidget)
        self.update_b = QtWidgets.QPushButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_b.setFont(font)
        self.update_b.setObjectName("update_b")
        self.verticalLayout_2.addWidget(self.update_b)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.t_plot = PlotWidget(self.centralwidget)
        self.t_plot.setObjectName("t_plot")
        self.verticalLayout.addWidget(self.t_plot)
        self.f_plot = PlotWidget(self.centralwidget)
        self.f_plot.setObjectName("f_plot")
        self.verticalLayout.addWidget(self.f_plot)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SamplingTool"))
        self.input_l.setText(_translate("MainWindow", "INPUT"))
        self.type_cb.setItemText(0, _translate("MainWindow", "Vmax⋅Cos (2⋅𝜋⋅f⋅t)"))
        self.type_cb.setItemText(1, _translate("MainWindow", "Vmax⋅Sin (2⋅𝜋⋅ f/5⋅t)"))
        self.type_cb.setItemText(2, _translate("MainWindow", "Vmax⋅[Λ (t⋅f + 1) - Λ (t⋅f -1)]"))
        self.vmax_l.setText(_translate("MainWindow", "Vmax"))
        self.vmax_cb.setItemText(0, _translate("MainWindow", "V"))
        self.vmax_cb.setItemText(1, _translate("MainWindow", "mV"))
        self.vmax_cb.setItemText(2, _translate("MainWindow", "μV"))
        self.f_l.setText(_translate("MainWindow", "f"))
        self.f_cb.setItemText(0, _translate("MainWindow", "Hz"))
        self.f_cb.setItemText(1, _translate("MainWindow", "kHz"))
        self.f_cb.setItemText(2, _translate("MainWindow", "MHz"))
        self.theta_l.setText(_translate("MainWindow", "θ"))
        self.theta_cb.setItemText(0, _translate("MainWindow", "°"))
        self.input_l_2.setText(_translate("MainWindow", "SAMPLING"))
        self.fs_l.setText(_translate("MainWindow", "fs"))
        self.fs_cb.setItemText(0, _translate("MainWindow", "Hz"))
        self.fs_cb.setItemText(1, _translate("MainWindow", "kHz"))
        self.fs_cb.setItemText(2, _translate("MainWindow", "MHz"))
        self.DC_l.setText(_translate("MainWindow", "DC"))
        self.DC_cb.setItemText(0, _translate("MainWindow", "%"))
        self.stages_l.setText(_translate("MainWindow", "STAGES"))
        self.stages_l_2.setText(_translate("MainWindow", "Stages"))
        self.ON_l.setText(_translate("MainWindow", "ON"))
        self.plot_l.setText(_translate("MainWindow", "Plot"))
        self.xin_l.setText(_translate("MainWindow", "Xin"))
        self.FAA_l.setText(_translate("MainWindow", "FAA"))
        self.SH_l.setText(_translate("MainWindow", "S&H"))
        self.LA_l.setText(_translate("MainWindow", "LA"))
        self.xout_l.setText(_translate("MainWindow", "FR/Xout"))
        self.update_b.setText(_translate("MainWindow", "Update"))
from src.ui.widgets.PlotWidget import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
