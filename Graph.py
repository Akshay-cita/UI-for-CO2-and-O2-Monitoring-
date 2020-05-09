# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import uart_CO2
import test_1
import o2_value_reading
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import terminal_input
import numpy as np

class Ui_graph(QtWidgets.QMainWindow):
    def __init__(self,parent):
        self.PARENT = parent
        super().__init__()
        self.setupUi()
        self.threadclass = Threadclass_3()
        self.threadclass.start()
        self.threadclass.signal.connect(self.plot)
        #self.threadclass.signal_1.connect(self.terminal_plot)
        
    def setupUi(self):

        self.setObjectName("graph")
        self.resize(787, 539)
        self.setMaximumSize(QtCore.QSize(1080, 998))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Next_button = QtWidgets.QPushButton()
        self.Next_button.setFixedSize(89, 25)
        self.Next_button.setObjectName("Next_button")

        self.layout = QGridLayout(self.centralwidget)
        self.layout.setGeometry(QtCore.QRect(0, 0, 780, 625))
        self.layout.setObjectName("Layout")
        self.figure = plt.figure()
        self.figure.set_facecolor("grey")
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize(780, 425)
        self.button = QPushButton()
        self.button.setFixedSize(89, 25)

        self.layout.addWidget(self.canvas, 0, 0, 1, 4)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addWidget(self.Next_button, 1, 3)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def plot(self,plot_val):
        print(plot_val)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('xkcd:grey')
        left = [1, 2, 3, 4]
        tick_label = ['CO2(%)', 'O2(%)', 'Humidity', 'Temperature (C)']
        ax.bar(left,plot_val, tick_label=tick_label, width=0.4, color=['Red', 'Green', 'Blue', 'Orange'])
        #ax.set_ylim([0,100])
        self.canvas.draw()
        time.sleep(5)
        
    def terminal_plot(self,terminal_val):
        print(terminal_val)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('xkcd:grey')
        
        left = [1, 2, 3, 4]
        tick_label = ['CO2(%)', 'O2(%)', 'Humidity', 'Temperature (C)']
        ax.bar(left,terminal_val, tick_label=tick_label, width=0.4, color=['Red', 'Green', 'Blue', 'Orange'])
        #ax.get_yaxis().set_visible(False)
        #ax.set_yticks(np.range(0,101,10))
        
        
        self.canvas.draw()
        time.sleep(5)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Home.setWindowTitle(_translate("Home", "MainWindow"))
        self.Next_button.setText(_translate("graph", "Next"))
        self.button.setText(_translate("graph", "Back"))
        self.button.clicked.connect(self.humid_temp)
        self.Next_button.clicked.connect(self.home)
    def humid_temp(self):
        
        self.threadclass.terminate()
        self.close()
        from humid_temp_1 import Ui_Temp_humid
        newWidget=Ui_Temp_humid(self.PARENT)
        self.PARENT.setCentralWidget(newWidget)
    def home(self):
        
        self.threadclass.terminate()
        self.close()
        from CO2_O2_reading import Ui_Home
        newWidget = Ui_Home(self.PARENT)
        self.PARENT.setCentralWidget(newWidget)

class Threadclass_3(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)
    #signal_1 = QtCore.pyqtSignal(list)
    def __init__(self, parent=None):
        super(Threadclass_3, self).__init__(parent)

    def run(self):  # continuosly running
        while (1):
            time.sleep(3)
            val_1= uart_CO2.co2_value()
            
            time.sleep(5)
            val_2=o2_value_reading.O2Value()
            time.sleep(1)
            val_3=test_1.Humidity()
            time.sleep(5)
            val_4=test_1.Temperature()
            plot_val = [val_1,val_2,val_3,val_4]
            
            self.signal.emit(list(plot_val))
            time.sleep(5)
            


