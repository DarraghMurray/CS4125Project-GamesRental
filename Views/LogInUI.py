
import tkinter as tk
from tkinter.constants import SOLID, W

class LogInUI():
    def __init__(self,master):
        tk.Frame(self,master)
    pass

f = ('Times', 14)


tk.Label(
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

tk.Label( 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = tk.Entry(
    font=f
    )
pwd_tf = tk.Entry(
    font=f,
    show='*'
    )
login_btn = tk.Button(
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
