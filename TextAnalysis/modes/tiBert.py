
from transformers import AutoTokenizer, AutoModel
import torch


class BERTAnalyzer:
    tokenizer = None
    model = None
    model_path = None


    def __init__(self, model_path: str = "../../TiBERT/"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModel.from_pretrained(model_path)


    def getAnalysis(self, text: str):
        textInputs = self.tokenizer(text, return_tensors="pt")
        textAnalysis = None

        with torch.no_grad():
            textAnalysis = self.model(**textInputs)

        if textAnalysis is not None:
            return textAnalysis

        return []

        
    def getDictionaryKeys(self):
        state_dict = torch.load(
            self.model_path + 'pytorch_model.bin', 
            map_location=torch.device('cpu')
        )
        return state_dict.keys()
