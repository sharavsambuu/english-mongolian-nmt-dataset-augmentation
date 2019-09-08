import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from datetime import datetime

def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open(sys.argv[1],'r') as f:
    data = f.read()

sentences = sent_tokenize(data)

for sent in sentences:
    print(sent)
