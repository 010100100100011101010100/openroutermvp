#this file will contain all the necessary APIs and their imports , plus connecting to the Database
#This also contains request models for the APIs

from fastapi import FastAPI,Body
from typing import Annotated
from mongoengine import connect
import os
from services.auth.auth import signup,login
from pydantic import BaseModel,EmailStr as url
from services.api import create_api_key, list_api_keys, delete_api_key
from services.payment import create_payment,handle_webhook
from services.generate import generate
from services.admin import 

app= FastAPI()

connect(db="openrouterdb",host="mongodb+srv://raseshh1827_db_user:password213@openrouterdb.kdvhv7n.mongodb.net/")
print("Connected to DB")

class SignupRequest(BaseModel):
    email: url
    password: str

class LoginRequest(BaseModel):
    email:url
    password:str

class APIKeyRequest(BaseModel):
    uid:str
    api_value:str

class PaymentRequest(BaseModel):
    uid:str
    amount:float
    product_id:str="ai_credits"

class GenerateRequest(BaseModel):
    prompt:str
    uid:str
    model:str
    temperature:float
    max_tokens:int
    modelprovider:str
    modelproviderid:str
    systemprompt:str="You are a helpful assistant"
    conversation_id:str=""


@app.post("/auth/register")
async def register(payload:Annotated[SignupRequest,Body()]):
    return await signup(payload.email,payload.password)

@app.post("/auth/login")
async def login_user(payload:LoginRequest):
    return await login(payload.email,payload.password)

@app.get("/api")
async def get_api_keys(uid:APIKeyRequest.uid):
    return await list_api_keys(uid)

@app.post("/api/create")
async def create_key(payload:APIKeyRequest.uid):
    return await create_api_key(payload.uid)

@app.delete("/api/delete")
async def delete_api_key(payload:APIKeyRequest.api_value):
    return await delete_api_key(payload.api_value)

@app.post("/api/regenerate")
async def regenerate_api_key(payload:APIKeyRequest.api_value):
    return await regenerate_api_key(payload.api_value)


@app.post("/payment/create")
async def create_payments(uid:PaymentRequest.uid,amount:PaymentRequest.amount,product_id:PaymentRequest.product_id):
    return await create_payment(uid,amount,product_id)

@app.post("/payment/webhook")
async def payment_webhook(event:dict):
    return await handle_webhook(event)  


@app.post("/generate/{modelprovider}/{conversation_id}")
async def generate_reply(prompt:GenerateRequest.prompt,uid:GenerateRequest.uid,model:GenerateRequest.model,temperature:GenerateRequest.temperature,max_tokens:GenerateRequest.max_tokens,modelprovider:GenerateRequest.modelprovider,modelproviderid:GenerateRequest.modelproviderid,system_prompt:GenerateRequest.systemprompt,conversation_id:GenerateRequest.conversation_id):
    response=await generate(prompt=prompt,uid=uid,model=model,temperature=temperature,max_tokens=max_tokens,modelprovider=modelprovider,modelproviderid=modelproviderid,system_prompt=system_prompt,conversation_id=conversation_id)
    return {"response":response}

