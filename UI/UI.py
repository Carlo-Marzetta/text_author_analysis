from UI.window import Window


class UI:
    instance = None
    window = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.window = Window()


    def getInputData(self):
        pass

    def getOptionsData(self):
        pass

    def getVisualizationData(self):
        pass
