import tkinter as tkk
from tkinter.simpledialog import SimpleDialog


class CustomDialog(SimpleDialog):
    def __init__(self, parent, title, text):
        self.text = text
        super().__init__(parent, title=title)

    def body(self, master):
        tkk.Label(master, text=self.text, wraplength=400, font=("Arial", 14), bg="#f0f0f0").pack(padx=20, pady=20)

    def buttonbox(self):
        box = tkk.Frame(self)
        ok_button = tkk.Button(box, text="OK", command=self.ok, width=15, font=("Arial", 12), bg='#4CAF50', fg="white")
        ok_button.pack(padx=10, pady=10)
        box.pack()

    def ok(self, event=None):
        self.withdraw()
        self.update_idletasks()
        self.parent.focus_set()
        self.destroy()
