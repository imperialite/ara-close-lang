# -*- coding: utf-8 -*-
"""ACL2023 - Extract_Embeddings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fIPw6yZdGWKAm7D9MDZ2zCA0ziL4SgkE
"""

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel
import torch
import pickle
import numpy as np

titles = []
contents = []

with open("ceb_all_data.txt","r",errors='ignore') as file:
  file_contents = file.readlines()
  for i in file_contents:
    parsed_text = i.split(',',2)
    parsed_text[0] = parsed_text[0].strip()
    print(parsed_text[0])
    titles.append(parsed_text[0].strip())
    contents.append(parsed_text[2])

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

#cebuano
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-uncased")
model = AutoModel.from_pretrained("bert-base-multilingual-uncased")

#Tokenize sentences
encoded_input = tokenizer(contents, padding=True, truncation=True, max_length=512, return_tensors='pt')

#Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

#Perform pooling. In this case, mean pooling
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

#sentence_embeddings_np = torch.stack(sentence_embeddings).numpy()
sentence_embeddings_np = sentence_embeddings.numpy()
sentence_embeddings_np[0]

import pandas as pd

np.savetxt('ceb_mbert_features.csv', sentence_embeddings_np, delimiter=',')

#DF = pd.DataFrame(sentence_embeddings)

#DF.to_csv("Sentence_Embedding_BERT.csv")