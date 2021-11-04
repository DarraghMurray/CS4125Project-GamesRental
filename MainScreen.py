import tkinter as tk
from tkinter.constants import INSERT

class MainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createNotification()
        self.main_account_screen()

    
    def createNotification(self):
        self.notificationText = tk.Text(self, height="20")
        self.notificationText.pack()
        self.notificationText.insert(INSERT, "Main Screen")

    def setScreen():
        return

    def main_account_screen(self):
        
        # create a Form label 
        tk.Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
        tk.Label(text="").pack() 
        
        # create Login Button 
        tk.Button(text="Login", height="2", width="30").pack() 
        tk.Label(text="").pack() 
        
        # create a register button
        tk.Button(text="Register", height="2", width="30").pack()