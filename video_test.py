
# import os
# from PyQt5.QtCore import QLibraryInfo

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
#     QLibraryInfo.PluginsPath
# )

from PyQt5.QtCore import Qt  # Import the Qt module
from PyQt5.QtGui import QPixmap  # Import the QPixmap class
from PyQt5 import QtWidgets, uic  # Import required PyQt5 modules
from vision_page.video_capture_thread import VideoThread  # Import the custom VideoThread class
from vision_page.icons import Icons  # Import the custom Icons class

class Vision(QtWidgets.QDialog):  # Create a custom Vision class that inherits from QDialog
    def __init__(self):  # Define the constructor method
        super().__init__()  # Call the constructor of the parent class

        self.start_video()  # Start the video

        uic.loadUi('../ui/vision.ui', self)  # Load the .ui file for the new window

        self.paused = False  # Initialize the paused flag as False

        self.media_toggle_button.clicked.connect(self.toggleFeed)  # Connect the toggleFeed method to the button's click event
        self.stop_video.clicked.connect(self.cancel_feed)  # Connect the cancel_feed method to the button's click event
        self.icon = Icons(self)  # Initialize an instance of the Icons class
        self.icon.setIcons()  # Set the icons

    def start_video(self):  # Method to start the video feed
        self.video_thread = VideoThread()  # Create an instance of the VideoThread class
        self.video_thread.image_signal.connect(self.update_image)  # Connect the update_image method to the image_signal signal
        self.video_thread.text_signal.connect(self.set_video_text)  # Connect the set_video_text method to the text_signal signal
        self.video_thread.start()  # Start the video thread

    def set_video_text(self, text):  # Method to set the video text
        self.video_status.setText(text)  # Set the text for the video status

    def update_image(self, image):  # Method to update the displayed image
        if image is not None:  # Check if the image is not None
            pixmap = QPixmap.fromImage(image)  # Create a QPixmap from the image
            self.camera_feed.setPixmap(pixmap.scaled(self.camera_feed.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))  # Set the pixmap for the camera feed

    def toggleFeed(self):  # Method to toggle the video feed
        if self.paused:  # Check if the video is paused
            self.paused = False  # Set the paused flag to False
            self.video_thread.resume()  # Resume the video feed
        else:
            self.paused = True  # Set the paused flag to True
            self.video_thread.pause()  # Pause the video feed
        self.icon.setIcons()  # Set the icons

    def cancel_feed(self):  # Method to cancel the video feed
        self.video_thread.stop()  # Stop the video feed
        self.video_status.setText("Video Stopped")  # Set the text for the video status

