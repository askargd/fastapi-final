from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get('/{sum1n}')
def get_sum1n(n: int):
    n=(n*(n+1)//2)
    return{"result": n}


@app.get('/{fibo}')
def get_fibo(terms: int):
    n1=0
    n2=1
    count=1
    while count<terms:
        nth=n1+n2
        #New values
        n1=n2
        n2=nth
        count += 1
    return{"result": n1}
