"""
Classes:
    :MainWindow: The main window, where the user can configure the
                    Input Parameter Editor settings.
"""
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class MainWindow(tk.Tk):
    """
    This is the class for the Main Window.
    
    """

    def __init__(self):
        super().__init__()
        
        self.title("Pixelmeter")
        self.option_add("*tearOff", False)
        
        # Make the app responsive
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1)
        
        # Create a style
        style = ttk.Style(self)
        
        # Import the tcl file
        self.tk.call("source", "ui/theme/azure.tcl")
        # Set the theme with the theme_use method
        self.tk.call("set_theme", "dark")
        
        # Create a Frame for the Checkbuttons
        control_frame = ttk.LabelFrame(self, text="Controls", padding=(20, 10))
        control_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        
        # Create a Frame for the Image
        image_frame = ttk.LabelFrame(self, text="Image", padding=(20, 10))
        image_frame.grid(row=0, column=1, padx=10, pady=(20, 10), sticky="nsew")
        
        img = ImageTk.PhotoImage(Image.open("ui/icons/no-image-icon.png"))
        panel = ttk.Label(image_frame, image=img)
        panel.pack()
        
        # self.resizable(False, False)
        # Center the window, and set minsize
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        x_cordinate = int((self.winfo_screenwidth()/2) - (self.winfo_width()/2))
        y_cordinate = int((self.winfo_screenheight()/2) - (self.winfo_height()/2))
        self.geometry("+{}+{}".format(x_cordinate, y_cordinate))
        
        self.mainloop()
        
    