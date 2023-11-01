from PyQt5 import QtWidgets
import sys
from mainwindow import MyWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = "styles/stylesheet.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
