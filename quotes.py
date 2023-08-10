import random
import json


def get_quote():
    with open("quotes.json", "r") as file:
        data = json.load(file)
        quote = random.choice(data["motivational_quotes"])
    return quote
