import tkinter as tk


class ItemPageUI(tk.Frame):

    def __init__(self,master, item, controller):
        tk.Frame.__init__(self,master)
        self.controller = controller
        self.item = item

    def createWidgets(self):
        self.buttonAddToCart = tk.Button(self, text="Add To Cart", command=self.controller.addToCart(self.item), borderwidth="0",fg="white", bg="dark gray")
        self.buttonRent = tk.Button(self, text="Rent", command=self.controller.rentItem(self.item), borderwidth="0",fg="white", bg="dark gray")
