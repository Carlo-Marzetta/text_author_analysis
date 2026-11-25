import os
import tkinter as tk
from tkinter import filedialog
from Input.user_inputs import UserInputs

class FileReader:

    origin = None
    instance = None

    def __init__(self):
        pass

    
    def getFileReaderWidget():
        pass

    def browseFile(self):
        path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[
                ("All files", "*.*"),
            ],
        )
        if path:
            UserInputs().originFile.set(path)