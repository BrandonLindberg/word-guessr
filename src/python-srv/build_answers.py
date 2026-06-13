import spacy

nlp = spacy.load("en_core_web_sm")

with open("answers.txt") as f:
    words = [line.strip() for line in f if line.strip()]

approved=[]

for word in words:
    doc = nlp(word)

    valid = True

    for token in doc:
        if token.pos_ not in ["NOUN", "PROPN", "ADJ"]:
            valid = False
            break

with open("answers_filtered.text", "w") as f:
    for word in approved:
        f.write(word + "\n")

print(f"Approved {len(approved)} words")