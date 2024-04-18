from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class FileHandler():
    def __init__(self, text_grid) -> None:
        self.text_grid = text_grid

    def new_file(self):
        self.text_grid.delete(0.0, END)

    def saveas(self):
        text = self.text_grid.get("1.0", "end-1c")
        save_location = filedialog.asksaveasfilename(defaultextension=".txt")

        try:
            with open(save_location, 'w+') as saved_file:
                saved_file.write(text.rstrip())
        except:
            messagebox.showerror(title="Oops!", message="Unable to save file for some reason")

    def open_file(self):
        opened_file = filedialog.askopenfile(mode='r')
        text = opened_file.read()
        self.text_grid.delete(0.0, END)
        self.text_grid.insert(0.0, text)

    def change_font(self, font):
        self.text_grid.config(font=(font, 12))

