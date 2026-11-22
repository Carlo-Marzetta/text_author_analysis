

class DataObject:
    inputs = []
    decomposed = []
    evaluated = []

    def __init__(self):
        pass

    def setInputs(self, inputs):
        self.inputs = inputs

    def getInputs(self):
        return self.inputs

    def setDecomposed(self, decomposed):
        self.decomposed = decomposed

    def getDecomposed(self):
        return self.decomposed

    def setEvaluated(self, evaluated):
        self.evaluated = evaluated

    def getEvaluated(self):
        return self.evaluated