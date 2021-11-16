import tkinter as tk
from View.LogInUI import LogInUI

class mainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,bg="black",width=500,height=master.winfo_screenheight())
        self.loadInit()

    
    def loadInit(self):
        self.LogInUI = LogInUI(self)

    def setScreen():
        return
