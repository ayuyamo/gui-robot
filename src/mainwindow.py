from PyQt5 import QtWidgets, uic
from pid_control import PIDController
from mission_planning import MissionPlanning
from vision import Vision

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the .ui file
        uic.loadUi('ui/mainwindow.ui', self)

        pid_page = PIDController()
        vision_page = Vision()
        mission_page = MissionPlanning()

        self.stacked_widget.addWidget(pid_page)
        self.stacked_widget.addWidget(vision_page)
        self.stacked_widget.addWidget(mission_page)

        self.home.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.pid_control.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(pid_page))
        self.vision.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(vision_page))
        self.mission_planning.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(mission_page))






            

