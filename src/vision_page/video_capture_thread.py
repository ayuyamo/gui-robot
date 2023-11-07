from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
from PyQt5.QtGui import QImage
import cv2
import socket
import pickle
import struct

class VideoThread(QThread):
    image_signal = pyqtSignal(QImage)  # Signal to emit the processed image
    text_signal = pyqtSignal(str)  # Signal to emit text messages
    HOST = "146.244.98.44"  # IP address to connect to
    PORT = 8089  # Port number to connect to
    
    def __init__(self):
        super().__init__()
        self.check_play_option()  # Initialize play options
        self.ThreadActive = False  # Initially set flag for threat status to false (not active)

    
    def check_play_option(self):
        # Initialize mutex and wait condition for handling pausing
        self.mutex = QMutex()
        self.wait_cond = QWaitCondition()
        self.isPaused = False  # Flag to indicate if the video is paused
    
    def set_socket(self):
        try:
            # Set up the server socket and handle errors
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.text_signal.emit("Socket Created")
            server_socket.bind((self.HOST, self.PORT))
            self.text_signal.emit("Socket Bound")
            server_socket.listen(10)
            self.text_signal.emit("Socket Listening")

            client_socket, client_address = server_socket.accept()
            self.text_signal.emit("Accepted Client Connection")
            data = b'' # Initialize data to store received data
            payload_size = struct.calcsize("=L") # Calculate payload size
            return server_socket, client_socket, data, payload_size
        except Exception as e:
            self.text_signal.emit("Socket Setup Error")
            return None, None, None, None
    
    def run(self):
        # Initialize socket and set the thread as active
        self.server_socket, self.client_socket, self.data, self.payload_size = self.set_socket()
        self.ThreadActive = True
        self.text_signal.emit("Video Running")
        
        while self.ThreadActive and self.client_socket is not None:
            # Pause handling
            self.mutex.lock()
            while self.isPaused:
                self.wait_cond.wait(self.mutex)
            self.mutex.unlock()
            
            # Receiving and processing data
            while len(self.data) < self.payload_size:
                self.data += self.client_socket.recv(4096)
            
            # Extracting message size and data    
            packed_msg_size = self.data[:self.payload_size]
            self.data = self.data[self.payload_size:]
            msg_size = struct.unpack("=L", packed_msg_size)[0]

            # Receiving complete data
            while len(self.data) < msg_size:
                self.data += self.client_socket.recv(4096)
            
            # Extracting frame data    
            frame_data = self.data[:msg_size]
            self.data = self.data[msg_size:]
            frame = pickle.loads(frame_data)
            
            # Converting frame to RGB and creating QImage
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame_rgb.shape
            bytes_per_line = channel * width
            
            # Emitting the image signal
            final_image = QImage(frame_rgb.data, frame.shape[1], frame.shape[0], bytes_per_line, QImage.Format_RGB888)
            self.image_signal.emit(final_image)

    def stop(self):
        # Stop the thread and wake all waiting threads
        self.ThreadActive = False
        self.wait_cond.wakeAll()
        self.quit()

    def pause(self):
        # Pause the video by setting the isPaused flag to True
        self.mutex.lock()
        self.isPaused = True
        self.mutex.unlock()

    def resume(self):
        # Resume the video by setting the isPaused flag to False and waking all waiting threads
        self.mutex.lock()
        self.isPaused = False
        self.wait_cond.wakeAll()
        self.mutex.unlock()
