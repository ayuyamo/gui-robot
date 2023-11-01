from PyQt5 import QtWidgets, uic

class NewWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/other.ui', self)  # Load the .ui file for the new window
