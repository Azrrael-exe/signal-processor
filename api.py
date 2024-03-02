from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using the app instance and the decorator syntax
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/signal-read")
async def read_singa():
    with open("output.txt", "r") as file:
        line = file.readlines(1)
        return {"line": line}
