from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
from PyQt5.QtGui import QImage
import cv2

class VideoThread(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture("banana.mp4")
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = rgbImage.shape
                bytesPerLine = channel * width
                qImg = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
                self.ImageUpdate.emit(qImg)
    def stop(self):
        self.ThreadActive = False
        self.quit()