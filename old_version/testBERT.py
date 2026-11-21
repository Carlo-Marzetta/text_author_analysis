
from transformers import AutoTokenizer, AutoModel
from torch.nn.functional import cosine_similarity
import torch

tokenizer = AutoTokenizer.from_pretrained('./TiBERT/')
model = AutoModel.from_pretrained('./TiBERT/')

testText = """
    de nas mtshan ma rnams dang dka' thub stobs las ni
    skye ba mthar mdzad bltams pa de ni rtogs gyur nas
    dam pa'i chos la gus pa'i shākya'i dbang phyug gi
    gnas su dkar min drang srong chen po gshegs par gyur
    """

testTextInputs = tokenizer(testText, return_tensors="pt")

with torch.no_grad():
    testTextAnalysis = model(**testTextInputs)
    print(testTextAnalysis)



state_dict = torch.load(
    './TiBERT/pytorch_model.bin', 
    map_location=torch.device('cpu')
)

print(state_dict.keys())
