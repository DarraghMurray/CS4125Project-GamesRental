import tkinter as tk
from tkinter.constants import LEFT, RIGHT
from Navbar import Navbar
from MainScreen import MainScreen

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.grid()
        self.mainscreen = MainScreen(master)
        self.navbar = Navbar(master)
        self.mainscreen.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = tk.W+tk.E+tk.N+tk.S)
        self.navbar.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S)
        


root = tk.Tk()
root.title("page")
root.geometry("800x600")
app = MainApplication(root)
root.mainloop()
        