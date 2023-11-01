# from PyQt5 import QtGui, QtWidgets, uic
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from video_capture_thread import VideoCapture

# class Vision(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()
#         video_capture = VideoCapture()
#         self.initUI()
        
#         uic.loadUi('ui/vision.ui', self)  # Load the .ui file for the new window

#     def initUI(self):
        
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Set the interval (in milliseconds) to read frames


#     def update_frame(self):
#         frame = self.video_capture.get_frame()
#         if frame is not None:
#             h, w, ch = frame.shape
#             bytes_per_line = ch * w
#             q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
#             self.camera_feed.setPixmap(QPixmap.fromImage(q_img).scaled(self.camera_feed.size(), Qt.KeepAspectRatio))

#     def closeEvent(self, event):
#         self.video_capture.release()
#         event.accept()
# import os
from PyQt5 import QtWidgets, QtCore, uic
# from PyQt5.QtCore import QLibraryInfo
from PyQt6.QtGui import QPixmap
from video_capture_thread import VideoCapture

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
#     QLibraryInfo.PluginsPath
# )

class Vision(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()   
        uic.loadUi('ui/vision.ui', self)  # Load the .ui file for the new window
        self.initUI()             

    def initUI(self):
        video_capture = VideoCapture()        
        video_capture.frameCaptured.connect(self.update_frame)

        
    def update_frame(self, image):
        self.camera_feed.setPixmap(QPixmap.fromImage(image))
    

