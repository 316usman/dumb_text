from fastapi import FastAPI

app = FastAPI()

@app.get("/print_text")
def print_text(text: str):
    return {"text": text}
