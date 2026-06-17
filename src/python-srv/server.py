from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import json
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

with open("answers.json") as f:
    answers = json.load(f)

embeddings = np.load("embeddings.npy")

target_index = random.randint(0, len(answers) - 1)
target_word = answers[target_index]
target_embedding = model.encode(f'The concept of {target_word}')

print (f"Target word: {target_word}")

@app.get("/crunch")
def crunch(word: str):

    guess_embedding = model.encode(word)

    score = float(cos_sim(target_embedding, guess_embedding))

    return {"score": score}
