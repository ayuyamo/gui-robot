from PyQt5 import QtWidgets, uic

class PIDController(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/pid_control.ui', self)  # Load the .ui file for the new window
