
from fastapi import FastAPI
from quotes import get_quote

app = FastAPI()


@app.get("/")
def get_base():
    return "Motivational API"


@app.get("/quote")
def get_complete_quote():
    return get_quote()


@app.get("/quote/single")
def get_base_quote_only():
    return get_quote()["quote"]
