import tkinter as tk
from tkinter.constants import LEFT, RIGHT, TOP
from Topbar import Topbar
from Navbar import Navbar
from MainScreen import MainScreen

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.topbar = Topbar(master)
        self.mainscreen = MainScreen(master)
        self.navbar = Navbar(master,self.mainscreen)
        self.navbar.pack( side = LEFT)
        self.topbar.pack( side = TOP)
        self.mainscreen.pack( side = RIGHT)
        


root = tk.Tk()
root.title("page")
app = MainApplication(root)
root.mainloop()
        