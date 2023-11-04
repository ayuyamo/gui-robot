from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets

class Icons(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def setIcons(self):
        # self.main.media_toggle_button.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        self.main.media_toggle_button.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        
        self.main.media_toggle_button.setAutoRaise(True)  # Remove the border and background