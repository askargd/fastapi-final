# FastAPI final
This is my homework project on educational platform  <<https://stepik.org/>>

![](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)


First you have to download all libraries. All the dependencies in requirements.txt
sudo apt install requirements.txt



## Installation
```
$ pip install fastapi

---> 100%
```

You will also need an ASGI server, for production such as Uvicorn or Hypercorn.

```
$ pip install "uvicorn[standard]"

---> 100%
```

### Run it

Run the server with:

```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```




## Routes


### sum1n
To get sum of numbers til n go to  http://localhost:8000/sum1n/<n>
Where n is number

For example: http://localhost:8000/sum1n/5
{"result": 15}


### Fibonacci sequence

In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2. Starting from 0 and 1, the first few values in the sequence are:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

To get n number from fibonacci sequence go to http://localhost:8000/fibo?n=<yournameber>

Example: http://localhost:8000/fibo?n=5
{"result": 3}


### reverse
This route will reverse the string text you write. Go to http://127.0.0.1:8000/reverse?string=yourtext

Example:
http://localhost:8000/reverse?string=Hello
{"result": olleH}


### list
This route allows you to put data into list variable and request it by http get request.

To pass a list of string through JSON body go to http://localhost:8000/list/yourtext

Example: 

```
Put request

curl -X 'PUT' \ 'http://127.0.0.1:8000/list/Apple' \ -H 'accept: application/json'
```


```
get request

curl -X 'GET' \ 'http://127.0.0.1:8000/list' \ -H 'accept: application/json'

or

http://127.0.0.1:8000/list
```



### calculator
Line ```expr``` passing through a JSON body. Line ```expr``` consists math expressions and it's format is num1, operator, num2.

* num1 and num2 are integers
* operator is string

Request example.
```
$ curl -X POST -d '{"expr": "1,+,1"}' -H 'Content-Type: application/json' http://localhost:8000/calculator
{"result": 2}
```

