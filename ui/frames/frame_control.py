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
from ui.frames.frame_expandable import ExpandableFrame

class ControlLayout(QVBoxLayout):
    
    def __init__(self):
        super().__init__()
        # self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # self.setLineWidth(2);
        
        # self.layout = QVBoxLayout()
        
        self.ref_frame = self.load_ref()
        self.add_frame = self.load_add()
        self.pro_frame = self.load_properties()
        
        # self.setLayout(self.layout)
        
    def load_ref(self):
        frame = ExpandableFrame("reference")
        
        grid = QGridLayout()
        grid.setAlignment(Qt.AlignTop)
        
        origin_lbl = QLabel("origin:")
        x_l_lbl = QLabel("x length:")
        y_l_lbl = QLabel("y length:")
        # type_lbl = QLabel("type:")
        # persp_lbl = QLabel("perspective:")
        
        px_lbl = QLabel("px")
        origin_px_lbl = QLabel("x,y")
        x_l_px_lbl = QLabel("xx")
        y_l_px_lbl = QLabel("yy")
        
        mm_lbl = QLabel("mm")
        x_l_mm_txt = QLineEdit("xx")
        x_l_mm_txt.setValidator(QDoubleValidator(0.99,99.99,5))
        y_l_mm_txt = QLineEdit("yy")
        y_l_mm_txt.setValidator(QDoubleValidator(0.99,99.99,5))
        
        
        grid.addWidget(origin_lbl, 1, 0)
        grid.addWidget(x_l_lbl, 2, 0)
        grid.addWidget(y_l_lbl, 3, 0)
        # grid.addWidget(type_lbl, 4, 0)
        # grid.addWidget(persp_lbl, 5, 0)
        
        grid.addWidget(px_lbl, 0, 1)
        grid.addWidget(origin_px_lbl, 1, 1)
        grid.addWidget(x_l_px_lbl, 2, 1)
        grid.addWidget(y_l_px_lbl, 3, 1)
        
        grid.addWidget(mm_lbl, 0, 2)
        grid.addWidget(x_l_mm_txt, 2, 2)
        grid.addWidget(y_l_mm_txt, 3, 2)
        
        spacer = QLabel()
        spacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        grid.addWidget(spacer, grid.rowCount(), 0)
        frame.layout.addLayout(grid)
        
        self.addWidget(frame)
        
        return frame
    
    def load_add(self):
        frame = ExpandableFrame("add")
        
        grid = QGridLayout()
        grid.setAlignment(Qt.AlignTop)
        
        title = QLabel()
        title.setText("test1")
        
        button = QPushButton()
        button.setText("test1")
        
        grid.addWidget(title, 0, 0)
        grid.addWidget(button, 1, 0)
        
        spacer = QLabel()
        spacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        grid.addWidget(spacer, grid.rowCount(), 0)
        frame.layout.addLayout(grid)
        
        self.addWidget(frame)
        return frame
    
    def load_properties(self):
        frame = ExpandableFrame("properties")
        
        self.addWidget(frame)
        return frame
        
        
        
        
        