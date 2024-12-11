from fastapi import FastAPI
import uvicorn as uv

app = FastAPI()

@app.get("/")
def getTodos():
    print("get todos called")
    return "Get todos called"


@app.get("/hello")
def helloWorld():
    print("Hello World")
    return "Hello World"


@app.get("/world")
def world():
    print("World is mine")
    return "world is mine"



def start():
    uv.run("todos.main:app", host="127.0.0.1", port=8000, reload=True)