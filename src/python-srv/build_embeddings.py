from sentence_transformers import SentenceTransformer
import numpy as np
import json

print("Loading model...")

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

print("Loading answers...")

with open("answers_filtered.txt") as f:
    answers = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(answers)} answers")
print("Generating embeddings...")

embeddings = model.encode(answers, convert_to_numpy=True, show_progress_bar=True)

print("Embeddings generated, saving...")

with open("answers.json", "w") as f:
    json.dump(answers, f)

np.save("embeddings.npy", embeddings)

print(f"Generated {len(answers)} embeddings")