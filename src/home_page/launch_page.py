from PyQt5.QtWidgets import QCheckBox, QTextEdit
from PyQt5.QtCore import QObject

class Launch(QObject):
    def __init__(self, main):
        self.main = main
        page2 = self.main.stacked_widget.widget(1)
        
        text_edit = page2.findChild(QTextEdit, 'nodes_selected')
        main_node = page2.findChild(QCheckBox, 'main_node')
        pid_node = page2.findChild(QCheckBox, 'pid_node')
        desired_state_node = page2.findChild(QCheckBox, 'desired_state_node')
        current_state_node = page2.findChild(QCheckBox, 'current_state_node')
        absolute_state_node = page2.findChild(QCheckBox, 'absolute_state_node')

        self.connect_checkbox(main_node, text_edit)
        self.connect_checkbox(pid_node, text_edit)
        self.connect_checkbox(desired_state_node, text_edit)
        self.connect_checkbox(current_state_node, text_edit)
        self.connect_checkbox(absolute_state_node, text_edit)
        
    def connect_checkbox(self, checkbox, text_edit):
        checkbox.toggled.connect(lambda state, te=text_edit, cb=checkbox: self.on_checkbox_toggled(state, te, cb))
            
    def on_checkbox_toggled(self, state, text_edit, checkbox):
        if state:
            text_edit.append(checkbox.objectName())  # Append the checkbox's object name to the text edit
        else:
            text = text_edit.toPlainText()
            text_edit.setPlainText(text.replace(checkbox.objectName(), ''))  # Remove the checkbox's object name