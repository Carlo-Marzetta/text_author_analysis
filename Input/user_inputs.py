import tkinter as tk


class UserInputs:
    instance = None

    originFile = None

    options = None



    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.originFile = tk.StringVar()   #make bindable to UI field

        return cls.instance

    