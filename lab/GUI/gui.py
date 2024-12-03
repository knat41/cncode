import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

# Create instance
win = tk.Tk()
win.title("CN Utility for Student")
win.rowconfigure(0, minsize=640, weight=1)
win.columnconfigure(0, minsize=800, weight=1)

# Create a container frame
mighty = ttk.LabelFrame(win, text=' Please enter your student ID')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Add a Label
a_label = ttk.Label(mighty, text="Enter an ID:")
a_label.grid(column=0, row=0, sticky='W')

# Define functions
def exitwindow():
    win.destroy()

def click_me():
    _msgDoneBox()

def _msgBox():
    msg.showinfo('Info Box', 'Data Science Tool:\ncn team 2023.')

def _msgDoneBox():
    msg.showinfo('Info Box', 'Done')
    
def dummyPass():
    pass

# Add a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=20, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

# Add a Button
action = ttk.Button(mighty, text="Select!", command=click_me)
action.grid(column=2, row=1)

# Create three Radiobuttons
radVar = tk.IntVar()
radVar.set(1)
rad1 = ttk.Radiobutton(mighty, text="Option 1", variable=radVar, value=1)
rad2 = ttk.Radiobutton(mighty, text="Option 2", variable=radVar, value=2)
rad1.grid(column=0, row=2, sticky='W')
rad2.grid(column=0, row=3, sticky='W')

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=dummyPass)
file_menu.add_command(label="Exit", command=exitwindow)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add QR menu
qr_menu = Menu(menu_bar, tearoff=0)
qr_menu.add_command(label="Link", command=dummyPass)
qr_menu.add_command(label="Wifi", command=dummyPass)
qr_menu.add_command(label="info", command=dummyPass)
menu_bar.add_cascade(label="QR Code", menu=qr_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)

name_entered.focus()

# Start GUI
win.mainloop()
