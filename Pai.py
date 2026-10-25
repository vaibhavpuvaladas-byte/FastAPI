from fastapi import FastAPI 
import json

app = FastAPI()

@app.get('/view')
def view():
    data = json.load(f)    
    return data

@app.get("/")
def hello():
    return{'message':'Patient Management System'}

@app.get('/about')
def about():
    return{'message':'A fully functional API to manage your patient record'}


@app.get('/view')
def view():
    data= load_data()

    return data