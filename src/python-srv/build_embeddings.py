from sentence_transformers import SentenceTransformer
import numpy as np
import json

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("answers_filtered.text") as f:
    answers = [line.strip() for line in f if line.strip()]

embeddings = model.encode(answers, convert_to_numpy=True, show_progress_bar=True)

with open("answers.json", "w") as f:
    json.dump(answers, f)

print(f"Generated {len(answers)} embeddings")