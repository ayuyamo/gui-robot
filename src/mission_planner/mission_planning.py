from PyQt5 import QtWidgets, uic

class MissionPlanning(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/mission_planning.ui', self)  # Load the .ui file for the new window

    