"""
    Utility functions
"""
import tkinter as tk
import tkinter.ttk as ttk

root = None
def move_window(event):
    if root is not None:
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def redo_title_bar(window):
    window.overrideredirect(True) # turns off title bar, geometry
    window.geometry('400x100+200+200') # set new geometry
    
    # make a frame for the title bar
    title_bar = ttk.Frame(window, relief='raised')
    
    # put a close button on the title bar
    close_button = ttk.Button(title_bar, text='x', command=window.destroy)
    
    # a canvas for the main area of the window
    main_area = tk.Canvas(window)
    
    # pack the widgets
    title_bar.pack(expand=1, fill='x')
    close_button.pack(side="right")
    main_area.pack(expand=1, fill="both")
    
    # bind title bar motion to the move window function
    title_bar.bind('<B1-Motion>', move_window)
    
    return main_area
    