#this file will contain all the necessary APIs and their imports , plus connecting to the Database
#This also contains request models for the APIs

from fastapi import FastAPI
from mongoengine import connect
import os
from services.auth.auth import signup,login
from pydantic import BaseModel,EmailStr as url

app= FastAPI()

connect(db="openrouterdb",host=os.environ.get("MONGO_URI"))
print("Connected to DB")

class SignupRequest(BaseModel):
    email: url
    password: str

class LoginRequest(BaseModel):
    email:url
    password:str

@app.post("/register")
async def register(payload:SignupRequest):
    return await signup(payload.email,payload.password)

@app.post("/login")
async def login_user(payload:LoginRequest):
    return await login(payload.email,payload.password)



