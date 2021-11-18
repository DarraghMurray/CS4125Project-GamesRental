import tkinter as tk
from View.LogInUI import LogInUI

class mainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,bg="black",width=500,height=master.winfo_screenheight())
        self.currentFrame = self.loadInitialFrame()

    
    def loadInitialFrame(self) -> tk.Frame:
        return LogInUI(self)

    def setCurrentFrame(self, frame) :
        self.currentFrame = frame

    def loadScreen(self):
        self.currentFrame(self)
