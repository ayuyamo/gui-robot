
# import os
# from PyQt5.QtCore import QLibraryInfo

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
#     QLibraryInfo.PluginsPath
# )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
from vision_page.video_capture_thread import VideoThread

class Vision(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.start_video()
        
        uic.loadUi('../ui/vision.ui', self)  # Load the .ui file for the new window
        
        self.stop_video.clicked.connect(self.CancelFeed)
    def start_video(self):
        self.video_thread = VideoThread()
        self.video_thread.image_signal.connect(self.update_image)
        self.video_thread.text_signal.connect(self.set_video_text)
        self.video_thread.start()

    def set_video_text(self, text):
        self.video_status.setText(text)
        
    def update_image(self, image):
        if image is not None:
            pixmap = QPixmap.fromImage(image)
            self.camera_feed.setPixmap(pixmap.scaled(self.camera_feed.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def CancelFeed(self): 
        self.video_thread.stop()
        self.video_status.setText("Video Stopped")
