from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

import numpy as np
import json
import random

app = FastAPI()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("answers.json)") as f:
    answers = json.load(f)

embeddings = np.load("embeddings.npy")

target_index = random.randint(0, len(answers) - 1)
target_word = answers[target_index]

print (f"Target word: {target_word}")

@app.get("/crunch")
def crunch(word1: str, word2: str):
    emb1 = model.encode(word1, convert_to_tensor=True)
    emb2 = model.encode(word2, convert_to_tensor=True)

    score = float(cos_sim(emb1, emb2))

    return {"score": score}
