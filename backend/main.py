#this file will contain all the necessary APIs and their imports , plus connecting to the Database
#This also contains request models for the APIs

from fastapi import FastAPI,Body
from typing import Annotated
from mongoengine import connect
import os
from services.auth.auth import signup,login
from pydantic import BaseModel,EmailStr as url

app= FastAPI()

connect(db="openrouterdb",host="mongodb+srv://raseshh1827_db_user:password213@openrouterdb.kdvhv7n.mongodb.net/")
print("Connected to DB")

class SignupRequest(BaseModel):
    email: url
    password: str

class LoginRequest(BaseModel):
    email:url
    password:str

@app.post("/register")
async def register(payload:Annotated[SignupRequest,Body()]):
    return await signup(payload.email,payload.password)

@app.post("/login")
async def login_user(payload:LoginRequest):
    return await login(payload.email,payload.password)



