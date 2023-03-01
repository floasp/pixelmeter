import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class ExpandableFrame(ttk.Frame):
    
    def __init__(self, parent):

        super().__init__(parent)
    
        # border_image = ImageTk.PhotoImage(Image.open("ui/theme/theme/dark/outline-basic.png"))
        # style = ttk.Style()
        # style.element_create("RoundedFrame",
        #              "image", border_image,
        #              ("focus", border_image),
        #              border=16, sticky="nsew")
        # style.layout("RoundedFrame",
        #      [("RoundedFrame", {"sticky": "nsew"})])
        
        
        # self.columnconfigure(index=0, weight=1)
        # self.columnconfigure(index=1, weight=1)
        # self.columnconfigure(index=2, weight=1)
        # self.rowconfigure(index=0, weight=1)
        # self.rowconfigure(index=1, weight=1)
        # self.rowconfigure(index=2, weight=1)
        
        # self.top_frame = ttk.Frame(self)
        # self.top_frame.grid(row=0, column=0, sticky="new")
        
        # self.frame = ttk.Frame(self)
        # self.frame.grid(row=1, column=0, sticky="nsew")
        
        
        # self.top_frame.columnconfigure(index=0, weight=1)
        # self.top_frame.rowconfigure(index=0, weight=1)
        
        # self.label = ttk.Label(self.top_frame, text="test")
        # self.label.grid(row=0, column=0)
        
        
        # self.columnconfigure(index=0, weight=1)
        # self.rowconfigure(index=0, weight=1)
        
        border_image = ImageTk.PhotoImage(Image.open("ui/theme/theme/dark/outline-basic.png"))
        style = ttk.Style()
        style.element_create("RoundedFrame",
                      "image", border_image,
                      ("focus", border_image),
                      border=16, sticky="nsew")
        style.layout("RoundedFrame",
              [("RoundedFrame", {"sticky": "nsew"})])
        
        self.border_frame = ttk.Frame(self, style="RoundedFrame", padding=10)
        # self.border_frame = ttk.Frame(self, padding=10)
        text1 = tk.Text(self.border_frame, borderwidth=0, highlightthickness=0, wrap="word",
                width=40, height=4)
        text1.grid(row=0, column=0, sticky="nesw")
        text1.insert("end", "Test widget")
        # self.border_frame.pack(side="top", fill="both", expand=True, padx=0, pady=0)
        self.border_frame.grid(row=0, column=0)
        
        
        
        
        