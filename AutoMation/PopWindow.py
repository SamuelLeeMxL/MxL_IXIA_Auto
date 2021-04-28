import tkinter as tk
import globals
from tkinter import messagebox as mb

def slave():
    globals.str5 = 'slave'

def master():
    globals.str5 = 'master'

tk.Button(text='Master mode(Just for the test LOG mark)', command=master).pack(fill=tk.X)
tk.Button(text='Slave  mode(Just for the test LOG mark)', command=slave).pack(fill=tk.X)
tk.mainloop()