"""
Classes:
    :MainWindow: The main window, where the user can configure the
                    Input Parameter Editor settings.
"""
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton,
    QMenu,
    QHBoxLayout,
    QFrame,
    QLabel
)
from ui.frames.frame_control import ControlLayout
from ui.frames.frame_image import ImageFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(ControlLayout())
        main_layout.addWidget(ImageFrame())
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        
        # Set the central widget of the Window.
        # self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())