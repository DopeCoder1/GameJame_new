import json

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from mongoengine import connect
from pydantic import BaseModel, validator
from models import StudentReg

app = FastAPI()
connect(db="pym", host="localhost", port=27017)


class Students(BaseModel):
    teamName: str
    phone: int
    email: str
    fioOne: str
    fioTwo: str
    fioThree: str
    fioFour: str
    fioFive: str
    universityName: str




@app.get('/get_all_users')
def get_all_user():
    users = json.loads(StudentReg.objects().to_json())
    return {"users": users}


@app.post('/register')
def registration(new_user: Students):
    users = StudentReg(
        teamName = new_user.teamName,
        phone = new_user.phone,
        email = new_user.email,
        fioOne = new_user.fioOne,
        fioTwo = new_user.fioTwo,
        fioThree = new_user.fioThree,
        fioFour = new_user.fioFour,
        fioFive = new_user.fioFive,
        universityName = new_user.universityName,
    )

    users.save()
    return {"message": "Вы усешно зарегистраровались"}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', reload=True)