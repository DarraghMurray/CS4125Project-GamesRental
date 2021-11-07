import tkinter as tk
from tkinter.constants import LEFT, RIGHT
from Navbar import Navbar
from MainScreen import MainScreen

class MainApplication(tk.Frame):
    def __init__(self, master,height,width):
        tk.Frame.__init__(self,master,height=height, width=width)
        self.grid()
        self.mainscreen = MainScreen(master,width*.8)
        self.navbar = Navbar(master,width*.2)
        self.mainscreen.grid(row = 0, column = 2, rowspan =12, columnspan = 8, sticky = tk.W+tk.E+tk.N+tk.S)
        self.navbar.grid(row = 0, column = 0, rowspan = 12, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S)
        


root = tk.Tk()
root.title("page")
root.geometry("600x600")
rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
app = MainApplication(root,rootHeight, rootWidth)
root.mainloop()
        