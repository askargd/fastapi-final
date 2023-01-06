from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get('/{sum1n}')
def get_sum1n(n: int):
    n=(n*(n+1)//2)
    return{"sum": n}

