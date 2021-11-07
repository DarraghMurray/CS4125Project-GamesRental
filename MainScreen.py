import tkinter as tk
from tkinter.constants import INSERT

class MainScreen(tk.Frame):
    def __init__(self, master, width):
        tk.Frame.__init__(self, master,bg="black",width=width)
        self.createNotification()

    
    def createNotification(self):
        self.notificationText = tk.Text(self, height="20")
        self.notificationText.insert(INSERT, "Main Screen")

    def setScreen():
        return
