from sentence_transformers import SentenceTransformer
import numpy as np
import json

def main():
    print("Loading model...")

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    print("Loading answers...")

    with open("answers_filtered.text") as f:
        answers = [line.strip() for line in f if line.strip()]

    print(f"Loaded {len(answers)} answers")
    print("Generating embeddings...")

    embeddings = model.encode(answers, convert_to_numpy=True, show_progress_bar=True)

    print("Embeddings generated, saving...")

    with open("answers.json", "w") as f:
        json.dump(answers, f)

    print(f"Generated {len(answers)} embeddings")

if _name_ == "_main_":
    main()