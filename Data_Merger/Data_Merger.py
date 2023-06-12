
from tkinter import *
from tkinter import ttk
from turtle import width

#Main Window
root = Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.title("Data Merger")

#Main Body 
bodyFram = ttk.Frame(root, borderwidth=5, width=1000, height =1000)
bodyFram.grid(column=0, row=0)



root.mainloop()