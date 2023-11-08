from PyQt5.QtWidgets import QCheckBox, QTextEdit
from PyQt5.QtCore import QObject

class Launch(QObject):
    def __init__(self, main):
        self.main = main
        
        # Connect the checkboxes to the text edit that display checked node boxes 
        self.connect_checkbox(self.main.main_node, self.main.nodes_selected)
        self.connect_checkbox(self.main.pid_node, self.main.nodes_selected)
        self.connect_checkbox(self.main.desired_state_node, self.main.nodes_selected)
        self.connect_checkbox(self.main.current_state_node, self.main.nodes_selected)
        self.connect_checkbox(self.main.absolute_state_node, self.main.nodes_selected)
        
    def connect_checkbox(self, checkbox, text_edit): # Method to connect a checkbox with a text edit
        checkbox.toggled.connect(lambda state, te=text_edit, cb=checkbox: self.on_checkbox_toggled(state, te, cb))
            
    def on_checkbox_toggled(self, state, text_edit, checkbox):
        if state: # Check if the checkbox is checked
            text_edit.append(checkbox.objectName())  # Append the checkbox's object name to the text edit
        else:
            text = text_edit.toPlainText() # Get the current text from the text edit
            text_edit.setPlainText(text.replace(checkbox.objectName(), ''))  # Remove the checkbox's object name