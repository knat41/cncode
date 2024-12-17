import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get("1.0", tk.END)
            file.write(content.strip())

def exit_app():
    root.quit()

def undo_action():
    text_area.event_generate("<<Undo>>")

def redo_action():
    text_area.event_generate("<<Redo>>")

def clear_text():
    text_area.delete("1.0", tk.END)

def show_about():
    messagebox.showinfo("About", "Note-Taking App\nVersion 1.0\nCreated with Tkinter")

# GUI Setup
root = tk.Tk()
root.title("Note-Taking App")

# Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
edit_menu.add_separator()
edit_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Set Menu Bar
root.config(menu=menu_bar)

# Text Widget with Scrollbar
text_area = tk.Text(root, wrap=tk.WORD, undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Start GUI
root.mainloop()
