from PyQt5.QtCore import QObject
from pid_control import PIDController
from mission_planning import MissionPlanning
from vision import Vision

class AddPage(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def add_widgets(self):
        self.main.pid_page = PIDController()
        self.main.vision_page = Vision()
        self.main.mission_page = MissionPlanning()
        
        self.main.stacked_widget.addWidget(self.main.pid_page)
        self.main.stacked_widget.addWidget(self.main.vision_page)
        self.main.stacked_widget.addWidget(self.main.mission_page)
