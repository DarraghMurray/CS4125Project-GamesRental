import tkinter as tk
from tkinter.constants import INSERT

class MainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg="black", height="600",width="600")
        self.createNotification()

    
    def createNotification(self):
        self.notificationText = tk.Text(self, height="20")
        #self.notificationText.pack()
        self.notificationText.insert(INSERT, "Main Screen")

    def setScreen():
        return
