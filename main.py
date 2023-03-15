"""
    Main method, starts the main window.
"""
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
import qdarktheme

import sys

if __name__ == '__main__':
    # main_window = MainWindow()
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
        
    qdarktheme.setup_theme()
    
    # window = QMainWindow()
    window = MainWindow()
    window.show()
    
    app.exec()
