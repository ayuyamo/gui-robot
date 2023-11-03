from PyQt5 import QtWidgets, uic
from home_page.navigate_pages import ButtonActions
from home_page.add_pages import AddPage
from home_page.launch_page import Launch
from icons import Icons

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the .ui file
        uic.loadUi('ui/mainwindow.ui', self)

        add_page = AddPage(self)
        add_page.add_widgets()

        button_handler = ButtonActions(self)
        button_handler.connect_buttons()
        
        icons = Icons(self)
        icons.setIcons()
        
        self.stacked_widget.setCurrentIndex(0)  # Set the initial page to index 0
        
        launch_page = Launch(self)





            

