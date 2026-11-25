import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from Input import *
from Input.console import Console
from Input.file_reader import FileReader
from Input.file_reader import UserInputs

class Window:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.instance.window = tk.Tk()
        self.instance.window.title("Text analysis")
        self.instance.window.geometry("1200x720")

        self.initTabs(self.instance.window).pack(expand=1, fill="both")

        
        self.instance.window.mainloop()

    #create tabs for workflow
    def initTabs(self, parent):
        ttk.Style().configure('Custom.TNotebook.Tab', padding=[30,4], width=100)
        tabControl = ttk.Notebook(parent, style = "Custom.TNotebook")

        tab1 = self.instance.initInputTab(tabControl)
        tab2 = self.instance.initOptionsTab(tabControl)
        tab3 = self.instance.initVisualizationTab(tabControl)
        tab4 = self.instance.getConsoleTab(tabControl)

        tabControl.add(tab1, text='Input')
        tabControl.add(tab2, text='Options')    
        tabControl.add(tab3, text='Visualization')
        tabControl.add(tab4, text='Console')

        return tabControl

    #input tab handles file input and initial changes to the text
    def initInputTab(self, parent):
        frame, content = self.instance.getBaseLayout(parent)

        tk.Label(content, text="Select File:").grid(row=0, column=1, pady=10)
        tk.Entry(content, textvariable=UserInputs().originFile, width=50).grid(row=1, column=1)
        tk.Button(
            content, 
            text="Browse", 
            command=FileReader().browseFile
        ).grid(row=1, column=2, padx=5)
        tk.Label(content, textvariable=UserInputs().originFile).grid(row=2, column=1, pady=10);

        return frame

    #options tab handles analysis options and parameters
    def initOptionsTab(self, parent):
        frame, content = self.instance.getBaseLayout(parent)


        return frame

    #visualization tab handles the display of results in multiple ways
    def initVisualizationTab(self, parent):
        frame, content = self.instance.getBaseLayout(parent)
        return frame

    def getConsoleTab(self, parent):
        self.console = Console(parent)
        return self.console.frame

    def getBaseLayout(self, parent):
        frame = tk.Frame(parent, bg="#BABABA")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=5)
        frame.columnconfigure(2, weight=1)
        content = tk.Frame(frame, bg="#FAFAFA", padx=20, pady=20, )
        content.grid(row=0, column=1, sticky="ns", rowspan=3, ipady=1000)

        return frame, content