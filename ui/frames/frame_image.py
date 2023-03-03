from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QAction, 
    QPixmap)
from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton,
    QMenu,
    QFrame,
    QLabel,
    QVBoxLayout,
    QStackedLayout
)


class ImageFrame(QFrame):
    
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setLineWidth(2);
        
        self.layout = QStackedLayout()
        
        self.image_lbl = QLabel()
        image = QPixmap('ui/icons/no-image-icon.png')
        # image = image.scaledToWidth(128)
        self.image_lbl.setPixmap(image)
        self.layout.addWidget(self.image_lbl)
        
        self.setLayout(self.layout)
        
        
        
        
        
        
        
        
        