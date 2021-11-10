import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT, RIGHT
from Navbar import Navbar
from MainScreen import MainScreen

class MainApplication(tk.Tk):
    def __init__(self):#, width):
        super().__init__()
        self.title("main")
        self.geometry("600x600")
        self.grid()
        self.navbar = Navbar(self)
        self.mainscreen = MainScreen(self)
        
app = MainApplication()
app.mainloop()
        