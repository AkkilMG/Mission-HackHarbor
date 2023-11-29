

from fastapi import FastAPI

# pip install fastapi "uvicorn[standard]"

app = FastAPI()

@app.get("/")
async def home():
    return "Hello World"

# cd ./Day3/API
# uvicorn app:app --reload