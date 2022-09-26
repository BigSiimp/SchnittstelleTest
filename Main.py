from fastapi import FastAPI
app = FastAPI()

@app.get("Main")

async def index():
    return {"message": "Hallo Welt"}