from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets

class Icons(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def setIcons(self):
        self.main.home_2.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_ArrowForward))
        self.main.home_1.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_ArrowBack))
        
        self.main.home_2.setAutoRaise(True)  # Remove the border and background
        self.main.home_1.setAutoRaise(True)  # Remove the border and background

