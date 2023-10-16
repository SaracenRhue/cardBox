import pyyaml
import os

subjects = os.listdir('subjects')
cards = []
for subject in subjects:
    with open(f'subjects/{subject}', 'r') as f:
        data = pyyaml.load(f, Loader=pyyaml.FullLoader)
        for card in data:
            cards.append(card)

