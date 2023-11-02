#!/usr/bin/python3
from PyQt5 import QtWidgets
import sys
from home_page.mainwindow import MyWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = "styles/indigo.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
