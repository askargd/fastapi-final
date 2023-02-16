# FastAPI final
This is my homework project on educational platform  <<stepik.org>>

![](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

##First you have to download all libraries. All the dependencies in requirements.txt
sudo apt install requirements.txt


##Installation
```
$ pip install fastapi

---> 100%
```

You will also need an ASGI server, for production such as Uvicorn or Hypercorn.

```
$ pip install "uvicorn[standard]"

---> 100%
```

###Run it

Run the server with:

```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```



#Routes

#sum1n
To get sum of numbers til n go to  http://localhost:8000/sum1n/n


#fibo
To get n number from fibonacci sequence go to http://localhost:8000/fibo?n=5


#reverse
This route will reverse the string text you write. Go to http://127.0.0.1:8000/reverse?string=yourtext


##list
To pass a list of string through JSON body go to http://localhost:8000/list/yourtext


##calculator
Line ```expr``` passing through a JSON body. Line ```expr``` consists math expressions. Through cli enter curl -X POST -d '{"expr": "1,+,1"}' -H 'Content-Type: application/json' http://localhost:8000/calculator


