import sys
from PyQt5 import QtWidgets
from interface import Window, Interface



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    ui = Interface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.run_videoplayer()
    sys.exit(app.exec_())
