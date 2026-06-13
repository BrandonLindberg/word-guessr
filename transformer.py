from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

app = FastAPI()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@app.get("/crunch")
def crunch(word1: str, word2: str):
    emb1 = model.encode(word1, convert_to_tensor=True)
    emb2 = model.encode(word2, convert_to_tensor=True)

    score = float(cos_sim(emb1, emb2))

    return {"score": score}
