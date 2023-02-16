# FastAPI final
This is my homework project on educational platform  <<stepik.org>>

![](https://cdn.pixabay.com/photo/2016/11/19/14/00/code-1839406_960_720.jpg)

##First you have to download all libraries. All the dependencies in requirements.txt
sudo apt install requirements.txt


##In order to run porject
uvicorn main:app --reload


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


