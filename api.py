from datetime import datetime

import uvicorn
from fastapi import FastAPI
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


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
