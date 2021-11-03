import tkinter as tk
from tkinter.constants import INSERT

class Topbar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        self.createNotification()

    
    def createNotification(self):
        self.notificationText = tk.Text(self, height="2")
        self.notificationText.pack()
        self.notificationText.insert(INSERT, "Store Adverts")