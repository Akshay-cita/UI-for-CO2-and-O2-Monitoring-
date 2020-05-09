from PyQt5 import QtCore, QtGui, QtWidgets
import  uart_CO2
import test_1
import time
import humid_temp_1
import terminal_input
import o2_value_reading
class Ui_Home(QtWidgets.QMainWindow):
    def __init__(self,parent):
        self.PARENT = parent

        super().__init__()
        self.setupUi()
        self.threadclass = Threadclass_1()
        self.threadclass.start()
        self.threadclass.signal.connect(self.updateCO2)
        self.threadclass.signal_1.connect(self.updateO2)
        #self.threadclass.terminal_signal.connect(self.terminal_updateCO2)
        #self.threadclass.terminal_signal_1.connect(self.terminal_updateO2)
        
    def setupUi(self):
        self.setObjectName("Home")
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
        self.widget.setGeometry(QtCore.QRect(420, 210, 311, 211))
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
        self.label_O2 = QtWidgets.QLabel(self.widget)
        self.label_O2.setGeometry(QtCore.QRect(20, 10, 281, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(85)
        self.label_O2.setFont(font)
        self.label_O2.setStyleSheet("background-color: rgb(14, 63, 2);\n"
"color: rgb(255, 255, 255);")
        self.label_O2.setObjectName("label_O2")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(50, 210, 321, 211))
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 281, 181))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(163, 21, 21);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_CO2 = QtWidgets.QLabel(self.widget_2)
        self.label_CO2.setGeometry(QtCore.QRect(20, 10, 281, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(85)
        self.label_CO2.setFont(font)
        self.label_CO2.setStyleSheet("background-color: rgb(208, 18, 18);\n"
"color: rgb(255, 255, 255);")
        self.label_CO2.setObjectName("label_CO2")
        self.Next_button = QtWidgets.QPushButton(self.frame)
        self.Next_button.setGeometry(QtCore.QRect(640, 430, 89, 25))
        self.Next_button.setObjectName("Next_button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 50, 291, 141))
        font = QtGui.QFont()
        
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 50, 231, 131))
        font = QtGui.QFont()
        
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def updateCO2(self,val):
        self.label_CO2.setText(str(val))
    def updateO2(self,var):
        self.label_O2.setText(str(var))
    def terminal_updateCO2(self,str_1):
        self.label_CO2.setText(str(str_1))
    def terminal_updateO2(self,str_2):
        self.label_O2.setText(str(str_2))
        
        
    
    
        #self.progressBar.setValue(float(val))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Home.setWindowTitle(_translate("Home", "MainWindow"))
        self.Next_button.clicked.connect(self.humid_temp)
        self.label_O2.setText(_translate("Home", "         "))
        self.label_CO2.setText(_translate("Home", "        "))
        self.Next_button.setText(_translate("Home", "Next"))
        self.label.setText(_translate("Home", "CO2"))
        self.label_2.setText(_translate("Home", "O2"))
    def humid_temp(self):
        
        self.threadclass.terminate()
        self.close()
        from humid_temp_1 import Ui_Temp_humid
        newWidget=Ui_Temp_humid(self.PARENT)
        self.PARENT.setCentralWidget(newWidget)

class Threadclass_1(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    signal_1 = QtCore.pyqtSignal(str)
    #terminal_signal = QtCore.pyqtSignal(str)
    #terminal_signal_1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Threadclass_1, self).__init__(parent)

    def run(self):  # continuosly running
        while (1):

            co2 = uart_CO2.co2_value()
            time.sleep(3)
            o2 = o2_value_reading.O2Value()
            self.signal_1.emit(str(o2))
            if co2=='a':
                reset()
                
            else:
                self.signal.emit(str(co2))  #emit val signal to the main class

