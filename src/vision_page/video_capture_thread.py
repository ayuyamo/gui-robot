from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
from PyQt5.QtGui import QImage
import cv2

class VideoThread(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.mutex = QMutex()
        self.wait_cond = QWaitCondition()
        self.ThreadActive = True
        self.isPaused = False

    def run(self):
        Capture = cv2.VideoCapture("banana.mp4")
        while self.ThreadActive:
            self.mutex.lock()
            while self.isPaused:
                self.wait_cond.wait(self.mutex)
            self.mutex.unlock()

            ret, frame = Capture.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = rgbImage.shape
                bytesPerLine = channel * width
                qImg = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.ImageUpdate.emit(qImg)

    def stop(self):
        self.ThreadActive = False
        self.wait_cond.wakeAll()
        self.quit()

    def pause(self):
        self.mutex.lock()
        self.isPaused = True
        self.mutex.unlock()

    def resume(self):
        self.mutex.lock()
        self.isPaused = False
        self.wait_cond.wakeAll()
        self.mutex.unlock()
