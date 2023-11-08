#!/usr/bin/python3
from PyQt5 import QtWidgets
import sys
from home_page.mainwindow import MyWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = "../styles/indigo.qss"
    with open(qss, "r") as fh: # Open the stylesheet file in read mode
        app.setStyleSheet(fh.read()) # Set the application's style sheet
    window = MyWindow() # Create an instance of the MyWindow class
    window.show() # Show the main window
    sys.exit(app.exec_()) # Execute the application's event loop and exit the script when the window is closed

