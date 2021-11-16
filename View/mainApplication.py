import tkinter as tk
from View.navbar import navbar
from View.mainScreen import mainScreen
from Controller.navigationController import NavigationController

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main")
        self.geometry("600x600")
        self.grid()
        self.navigator = NavigationController()
        self.navbar = navbar(self, self.navigator)
        self.mainScreen = mainScreen(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.navbar.grid(row=0, column=0, sticky="nsew")
        self.mainScreen.grid(row=0, column=1, sticky="nsew")
        
app = MainApplication()
app.mainloop()
        