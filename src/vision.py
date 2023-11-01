from PyQt5 import QtWidgets, uic

class Vision(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/vision.ui', self)  # Load the .ui file for the new window
