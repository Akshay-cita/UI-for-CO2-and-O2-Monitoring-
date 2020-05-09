from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.Init_UI()
        self.loadWidget()

    def Init_UI(self):
        self.resize(787, 539)
    def loadWidget(self):  ## to launch home window on startup

        from humid_temp_1 import Ui_Temp_humid
        self.centralWidget = Ui_Temp_humid(self)
        self.show()
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    ui.showFullScreen()
    sys.exit(app.exec_())
