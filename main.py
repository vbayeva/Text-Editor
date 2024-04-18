import sys
from tkinter import *
from file_handler import FileHandler

WINDOWS_SIZE = 400

def add_menu_commands(filemenu, file_handler):
    filemenu.add_command(label="New", command=file_handler.new_file)
    filemenu.add_command(label="Open", command=file_handler.open_file)
    filemenu.add_command(label="Save As...", command=file_handler.saveas)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=root.quit)

def define_window(root):
    root.minsize(width=WINDOWS_SIZE, height=WINDOWS_SIZE)
    root.maxsize(width=WINDOWS_SIZE, height=WINDOWS_SIZE)

def define_font(menubar):
    fontmenu = Menu(menubar, tearoff=0)
    fonts = ["Helvetica", "Courier", "Times"]
    for font in fonts:
        fontmenu.add_command(label=font, command=lambda f=font: text_handler.change_font(f))
    menubar.add_cascade(label="Font", menu=fontmenu)

filename = None
root = Tk("Super Text Editor")
define_window(root=root)

text_grid = Text(root, width=WINDOWS_SIZE, height=WINDOWS_SIZE)
text_grid.grid(sticky="nsew")

text_handler = FileHandler(text_grid)

menubar = Menu(root)
filemenu = Menu(menubar)
add_menu_commands(filemenu=filemenu, file_handler=text_handler)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
define_font(menubar=menubar)

root.mainloop()