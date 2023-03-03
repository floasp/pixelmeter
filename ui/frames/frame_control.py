from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton,
    QMenu,
    QLabel,
    QHBoxLayout,
    QFrame,
    QVBoxLayout,
    QPushButton
)
from ui.frames.frame_expandable import ExpandableFrame

class ControlFrame(QFrame):
    
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setLineWidth(2);
        
        self.layout = QVBoxLayout()
        
        self.load_ref()
        self.load_add()
        self.load_properties()
        
        self.setLayout(self.layout)
        
    def load_ref(self):
        frame = ExpandableFrame("reference")
        
        title = QLabel()
        title.setText("test")
        frame.layout.addWidget(title)
        
        button = QPushButton()
        button.setText("test")
        frame.layout.addWidget(button)
        
        self.layout.addWidget(frame)
        
        return frame
    
    def load_add(self):
        frame = ExpandableFrame("add")
        
        title = QLabel()
        title.setText("test1")
        frame.layout.addWidget(title)
        
        button = QPushButton()
        button.setText("test1")
        frame.layout.addWidget(button)
        
        self.layout.addWidget(frame)
    
    def load_properties(self):
        pass
        
        
        
        
        