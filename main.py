import sys
from tkinter import *
from tkinter import filedialog

root = Tk("Super Text Editor")

text_grid = Text(root)
text_grid.grid()

def saveas():
    global text_grid
    text = text_grid.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()

    with open(save_location, 'w+') as saved_file:
        saved_file.write(text)

button = Button(root, text="Save", command=saveas)
button.grid()

font_grid = Menubutton(root, text="Font")
font_grid.grid()
font_grid.menu = Menu(font_grid, tearoff=0)
font_grid["menu"] = font_grid.menu

helvetica = IntVar()
courier = IntVar()

font_by_name = {
    "Courier": courier,
    "Helvetica": helvetica
}

for font in font_by_name.keys():
    font_grid.menu.add_checkbutton(label=font, variable=font_by_name[font], command={
        text_grid.config(font=font)
    })

root.mainloop()
