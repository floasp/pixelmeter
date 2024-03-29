from PySide6.QtGui import QAction, QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton,
    QMenu,
    QFrame,
    QLabel,
    QVBoxLayout
)


class ExpandableFrame(QFrame):
    
    def __init__(self, title):
        super().__init__()
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setLineWidth(2);
        
        self.layout = QVBoxLayout()
        
        self.title_lbl = QLabel()
        self.title_lbl.setText(title)
        # self.title_lbl.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.title_lbl)
        
        self.setLayout(self.layout)
        
        
        
        
        
        
        
        
        