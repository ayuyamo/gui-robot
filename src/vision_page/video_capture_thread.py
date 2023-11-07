from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
from PyQt5.QtGui import QImage
import cv2
import socket
import pickle
import struct

class VideoThread(QThread):
    image_signal = pyqtSignal(QImage)
    text_signal = pyqtSignal(str)
    HOST = "146.244.98.44"
    PORT = 8089
    
    def __init__(self):
        super().__init__()
        self.check_play_option()
        self.ThreadActive = False

    
    def check_play_option(self):
        self.mutex = QMutex()
        self.wait_cond = QWaitCondition()
        self.isPaused = False
    
    def set_socket(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.text_signal.emit("Socket Created")
            server_socket.bind((self.HOST, self.PORT))
            self.text_signal.emit("Socket Bound")
            server_socket.listen(10)
            self.text_signal.emit("Socket Listening")

            client_socket, client_address = server_socket.accept()
            self.text_signal.emit("Accepted Client Connection")
            data = b''
            payload_size = struct.calcsize("=L")
            return server_socket, client_socket, data, payload_size
        except Exception as e:
            self.text_signal.emit("Socket Setup Error")
            return None, None, None, None

    # def run(self):
    #     Capture = cv2.VideoCapture("../banana.mp4")
    #     while self.ThreadActive:
    #         self.mutex.lock()
    #         while self.isPaused:
    #             self.wait_cond.wait(self.mutex)
    #         self.mutex.unlock()

    #         ret, frame = Capture.read()
    #         if ret:
    #             rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #             height, width, channel = rgbImage.shape
    #             bytesPerLine = channel * width
    #             qImg = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
    #             self.image_signal.emit(qImg)
    
    def run(self):
        self.server_socket, self.client_socket, self.data, self.payload_size = self.set_socket()
        self.ThreadActive = True
        self.text_signal.emit("Video Running")
        while self.ThreadActive and self.client_socket is not None:
            self.mutex.lock()
            while self.isPaused:
                self.wait_cond.wait(self.mutex)
            self.mutex.unlock()
            
            while len(self.data) < self.payload_size:
                self.data += self.client_socket.recv(4096)
            packed_msg_size = self.data[:self.payload_size]

            self.data = self.data[self.payload_size:]
            msg_size = struct.unpack("=L", packed_msg_size)[0]

            while len(self.data) < msg_size:
                self.data += self.client_socket.recv(4096)
            frame_data = self.data[:msg_size]
            self.data = self.data[msg_size:]
            frame = pickle.loads(frame_data)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame_rgb.shape
            bytes_per_line = channel * width
            final_image = QImage(frame_rgb.data, frame.shape[1], frame.shape[0], bytes_per_line, QImage.Format_RGB888)
            self.image_signal.emit(final_image)

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
