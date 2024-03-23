from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using the app instance and the decorator syntax
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/signal-read")
async def read_signal():
    with open("output.txt", "r") as file:
        line = file.readlines(-1)
        return {"line": line}
    

class SingalCapture(BaseModel):
    value: float
    source: str
    timestamp: str = None

@app.post("/signal-capture")
async def create_signal(input: SingalCapture):
    input.timestamp = input.timestamp or str(datetime.now())
    with open("output.txt", "a") as file:
        file.write(f"{input.model_dump()}\n")
    return {"message": "Signal captured successfully"}