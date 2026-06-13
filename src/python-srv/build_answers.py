import spacy

nlp = spacy.load("en_core_web_sm")

with open("answers.txt") as f:
    words = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(words)} words")
print(words[:10])

approved=[]

allowed_pos = {"NOUN", "PROPN", "ADJ", "VERB"}

for word in words:
    doc = nlp(word)

    print(f"\nWord: {word}")
    for token in doc:
        print(f"Token: {token.text} | POS: {token.pos_}")

    valid = True

    if all(token.pos_ in allowed_pos for token in doc):
        approved.append(word)

with open("answers_filtered.txt", "w") as f:
    for word in approved:
        f.write(word + "\n")

print(f"Approved {len(approved)} words")
