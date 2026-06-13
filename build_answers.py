import spacy

nlp = spacey.load("en_core_web_sm")

with open("answers.txt") as f:
    words = [line.strip() for line in f]

approved=[]

for word in words:
    doc = nlp(word)

    if len(doc) == 1:
        token = doc[0]

        if token.pos_ in ["NOUN", "PROPN"]:
            approved.append(word)

with open("answers_filtered.text", "w") as f:
    for word in approved:
        f.write(word + "\n")
