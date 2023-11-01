from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QImage
import cv2



class VideoCapture(QObject):
    frameCaptured = pyqtSignal(QImage)
    
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture("banana.mp4") 
    
    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Convert OpenCV BGR image to RGB format for QImage
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Create QImage from the OpenCV frame
            height, width, channel = rgbImage.shape
            bytesPerLine = channel * width
            qImg = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)

            # Emit the frame to be displayed in the GUI
            self.frameCaptured.emit(qImg)
        
        self.cap.release()