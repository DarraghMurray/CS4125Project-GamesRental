import tkinter as tk

class navbar(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master, bg="dark gray",width=100,height=master.winfo_screenheight())
        #self.create_widgets()

    def create_widgets(self):
        self.buttonReg = tk.Button(self, text="register", borderwidth="0",fg="white", bg="dark gray")
        self.buttonLogIn = tk.Button(self, text="log-in", borderwidth="0",fg="white", bg="dark gray")
        self.buttonStore = tk.Button(self, text="Store", borderwidth="0",fg="white", bg="dark gray")
        self.buttonLibrary = tk.Button(self, text="Games Library", borderwidth="0",fg="white", bg="dark gray")
        self.buttonSettings = tk.Button(self, text="User Settings", borderwidth="0",fg="white", bg="dark gray")

        self.buttonReg.grid()
        self.buttonLogIn.grid()
        self.buttonStore.grid()
        self.buttonLibrary.grid()
        self.buttonSettings.grid()

    def goToRegister():
        pass
    
    def goToSignIn():
        pass