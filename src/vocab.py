import json
import random


def load_vocabulary():
    with open("data/vocabulary.json", "r", encoding="utf-8") as file:
        vocabulary = json.load(file)

    return vocabulary


def get_random_word(vocabulary):
    return random.choice(vocabulary)
