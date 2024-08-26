from tkinter import *
import tkinter.messagebox

root = Tk()

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()