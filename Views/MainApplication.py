import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT, RIGHT
from Navbar import Navbar
from MainScreen import MainScreen
from Controllers import NavigationController

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main")
        self.geometry("600x600")
        self.grid()
        navigator = NavigationController()
        self.navbar = Navbar(self,navigator)
        self.mainscreen = MainScreen(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.navbar.grid(row=0, column=0, sticky="nsew")
        self.mainscreen.grid(row=0, column=1, sticky="nsew")
        
app = MainApplication()
app.mainloop()
        