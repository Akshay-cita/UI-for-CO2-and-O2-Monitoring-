# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'humid_temp_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import test_1
import terminal_input

class Ui_Temp_humid(QtWidgets.QMainWindow):
    def __init__(self,parent):
        self.PARENT = parent

        super().__init__()
        self.setupUi()
        self.threadclass = Threadclass_2()
        self.threadclass.signal.connect(self.updateHumidity)
        self.threadclass.signal_1.connect(self.updateTemperature)
        #self.threadclass.terminal_signal.connect(self.terminal_updatehumidity)
        #self.threadclass.terminal_signal_1.connect(self.terminal_updatetemperature)
        self.threadclass.start()
    def setupUi(self):
        self.setObjectName("Temp_humid")
        self.resize(787, 539)
        self.setMaximumSize(QtCore.QSize(1080, 998))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 971, 831))
        self.frame.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(420, 200, 311, 211))
        self.widget.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 281, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background-color: rgb(3, 98, 4);\n"
"background-color: rgb(14, 63, 2);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_temperature = QtWidgets.QLabel(self.widget)
        self.label_temperature.setGeometry(QtCore.QRect(20, 10, 281, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(85)
        self.label_temperature.setFont(font)
        self.label_temperature.setStyleSheet("background-color: rgb(225, 92, 9);\n"
"color: rgb(255, 255, 255);")
        self.label_temperature.setObjectName("label_temperature")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(50, 200, 321, 211))
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 281, 181))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(163, 21, 21);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_Humidity = QtWidgets.QLabel(self.widget_2)
        self.label_Humidity.setGeometry(QtCore.QRect(20, 10, 281, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(85)
        self.label_Humidity.setFont(font)
        self.label_Humidity.setStyleSheet("background-color: rgb(15, 109, 186);\n"
"color: rgb(255, 255, 255);")
        self.label_Humidity.setObjectName("label_Humidity")
        self.Next_2_button = QtWidgets.QPushButton(self.frame)
        self.Next_2_button.setGeometry(QtCore.QRect(640, 420, 89, 25))
        self.Next_2_button.setObjectName("Next_2_button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 70, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(410, 70, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_back.setGeometry(QtCore.QRect(80, 420, 89, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def updateHumidity(self, val):
        self.label_Humidity.setText(str(val))
        # self.progressBar.setValue(float(val))
    def updateTemperature(self, var):
        self.label_temperature.setText(str(var))
    def terminal_updatehumidity(self,str_1):
        self.label_Humidity.setText(str(str_1))
    def terminal_updatetemperature(self,str_2):
        self.label_temperature.setText(str(str_2))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Temp_humid.setWindowTitle(_translate("Temp_humid", "MainWindow"))
        self.pushButton_back.clicked.connect(self.home)
        self.Next_2_button.clicked.connect(self.graph)
        self.label_temperature.setText(_translate("Temp_humid", "      "))
        self.label_Humidity.setText(_translate("Temp_humid", "      "))
        self.Next_2_button.setText(_translate("Temp_humid", "Next"))
        self.label.setText(_translate("Temp_humid", "Humidity"))
        self.label_2.setText(_translate("Temp_humid", "Temperature"))
        self.pushButton_back.setText(_translate("Temp_humid", "Back"))
    def home(self):
        
        self.threadclass.terminate()
        self.close()
        from sample_1 import Ui_Home
        newWidget = Ui_Home(self.PARENT)
        self.PARENT.setCentralWidget(newWidget)
    def graph(self):
        
        self.threadclass.terminate()
        self.close()
        #self.close()
        from Graph import Ui_graph
        newWidget = Ui_graph(self.PARENT)
        self.PARENT.setCentralWidget(newWidget)


class Threadclass_2(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    signal_1 = QtCore.pyqtSignal(str)
    #terminal_signal = QtCore.pyqtSignal(str)
    #terminal_signal_1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Threadclass_2, self).__init__(parent)

    def run(self):  # continuosly running
        while (1):
            val=test_1.Humidity()
            time.sleep(3)
            var=test_1.Temperature()

            self.signal.emit(str(val))  # emit val signal to the main class
            self.signal_1.emit(str(var))
            time.sleep(10)

