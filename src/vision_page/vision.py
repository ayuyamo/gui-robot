
import os
from PyQt5.QtCore import QLibraryInfo

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath
)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
from vision_page.video_capture_thread import VideoThread
from vision_page.icons import Icons

class Vision(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.video_thread = VideoThread()
        self.video_thread.start()
        self.video_thread.ImageUpdate.connect(self.ImageUpdateSlot)
        
        uic.loadUi('ui/vision.ui', self)  # Load the .ui file for the new window
        
        icon = Icons(self)
        icon.setIcons()
        
        self.pause = False
        
        # self.media_toggle_button.clicked.connect(self.toggleFeed) # Probably not needed

    def ImageUpdateSlot(self, Image):
        self.camera_feed.setPixmap(QPixmap.fromImage(Image))
        self.camera_feed.setScaledContents(True)

    def toggleFeed(self): # Probably not needed
        self.video_thread.stop()
        # if self.paused:
        #     self.paused = False
        #     self.video_thread.resume()  # Resume the video feed
        # else:
        #     self.paused = True
        #     self.video_thread.pause()  # Pause the video feed

    
    


    

