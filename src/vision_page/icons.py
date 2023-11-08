from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets

class Icons(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def setIcons(self):
        # Set icons for play/pause button        
        if self.main.paused == False: # Check if video is playing
            # Set the pause icon if the video is playing
            self.main.media_toggle_button.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        else:
            # Set the play icon if the video is paused
            self.main.media_toggle_button.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        
        self.main.media_toggle_button.setAutoRaise(True)  # Remove the border and background
        
        
        # Set icons for stop button
        # Set the stop icon for the stop button
        self.main.stop_video.setIcon(self.main.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.main.stop_video.setAutoRaise(True)  # Remove the border and background