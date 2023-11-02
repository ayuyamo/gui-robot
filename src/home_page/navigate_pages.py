from PyQt5.QtCore import QObject

class ButtonActions(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main

    def connect_buttons(self):
        self.main.home.clicked.connect(lambda: self.main.stacked_widget.setCurrentIndex(0))
        self.main.home_1.clicked.connect(lambda: self.main.stacked_widget.setCurrentIndex(0))
        self.main.home_2.clicked.connect(lambda: self.main.stacked_widget.setCurrentIndex(1))
        self.main.pid_control.clicked.connect(lambda: self.main.stacked_widget.setCurrentWidget(self.main.pid_page))
        self.main.vision.clicked.connect(lambda: self.main.stacked_widget.setCurrentWidget(self.main.vision_page))
        self.main.mission_planning.clicked.connect(lambda: self.main.stacked_widget.setCurrentWidget(self.main.mission_page))
