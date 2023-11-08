from PyQt5.QtCore import QObject
from controller.pid_control import PIDController
from mission_planner.mission_planning import MissionPlanning
from vision_page.vision import Vision

class AddPage(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def add_widgets(self): # Method to add widgets to the main window
        self.main.pid_page = PIDController()
        self.main.vision_page = Vision()
        self.main.mission_page = MissionPlanning()
        
        # Add the pages to the stacked widget
        self.main.stacked_widget.addWidget(self.main.pid_page)
        self.main.stacked_widget.addWidget(self.main.vision_page)
        self.main.stacked_widget.addWidget(self.main.mission_page)
