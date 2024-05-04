from fastapi import FastAPI


app : FastAPI = FastAPI()

users = {"user1":{"name":"Qasim","email":"m.qasim@gmail.com"},
         "user2":{"name":"Dr. Najeed","email":"dr.najeed@gmail.com"}}

@app.get('/')
def index():
    return {"Hello": "world1"}

@app.get('/user/')
def fun_users():
    return users




