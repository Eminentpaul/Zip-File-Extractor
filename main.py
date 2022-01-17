from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox as mg, filedialog as open
import os
from zipfile import ZipFile
from pathlib import Path

root = tk.ThemedTk()
root.title("Zip Extractor")
root.get_themes()
root.set_theme("radiance")
root.resizable(0, 0)
root.minsize(550, 250)

zipping_file = []


def zip_file():
    file_path = open.askopenfilenames(initialdir="", filetypes=(("All Files", "*.*"), ("Mp3 files", "*.mp3")),
                                       title="Select Files")
    
    name = open.asksaveasfilename(initialdir="/", defaultextension=".zip")

    for files in file_path:
        zipping_file.append(files)

    with ZipFile(str(name), "w") as file:
        for path in Path(str(file_path)).rglob("*.*"):
            file.write(path)

button = Button(root, text="Select", command=zip_file).pack()

root.mainloop()