from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QAction, 
    QIntValidator, 
    QDoubleValidator, 
    QFont)
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
    QPushButton,
    QGridLayout,
    QSizePolicy,
    QLineEdit,
    QRadioButton
)

class Origin(QWidget):
    
    def __init__(self):
        self.pxx = 0
        self.pxy = 0
        self.pxw = 0
        self.pxh = 0
        
        self.refx = 0
        self.refy = 0
        
        self.origin_icon = QLabel()
        self.x_icon = QLabel()
        self.y_icon = QLabel()