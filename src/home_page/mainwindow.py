from PyQt5 import QtWidgets, uic
from home_page.navigate_pages import ButtonActions
from home_page.add_pages import AddPage

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the .ui file
        uic.loadUi('ui/mainwindow.ui', self)
        
        add_page = AddPage(self)
        add_page.add_widgets()

        button_handler = ButtonActions(self)
        button_handler.connect_buttons()




            

