#this file will contain all the necessary APIs and their imports , plus connecting to the Database
#This also contains request models for the APIs

from fastapi import FastAPI,Body
from typing import Annotated
from mongoengine import connect
import os
from services.auth.auth import signup,login
from pydantic import BaseModel,EmailStr as url
from services.api.apicrud import create_api_key, get_api_keys, delete_api_key
from services.payment.payment import create_payment,handle_webhook
from services.generate.generate import generate
from services.admin.admin import adminLogin,create_admin,addModelProvider,addModel

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


class AdminRequest(BaseModel):
    email:url
    password:str

@app.post("/auth/register")
async def register(payload:Annotated[SignupRequest,Body()]):
    return await signup(payload.email,payload.password)

@app.post("/auth/login")
async def login_user(payload:LoginRequest):
    return await login(payload.email,payload.password)

@app.get("/api")
async def get_api_keys(uid:APIKeyRequest.uid):
    return await get_api_keys(uid)

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


@app.post("/admin/addModel")
async def add_model(name:str,description:str,providers:list,creators:list,token_price:float,model_size:str,model_type:str,inputmodality:str,outputmodality:str,model_slug:str,adminEmail:AdminRequest.email,adminPassword:AdminRequest.password):
    add_model_response=await addModel(name=name,description=description,providers=providers,creators=creators,token_price=token_price,model_size=model_size,model_type=model_type,inputmodality=inputmodality,outputmodality=outputmodality,model_slug=model_slug,adminEmail=adminEmail,adminPassword=adminPassword)
    return add_model_response

@app.post("/admin/createAdmin")
async def create_admin(superadmin_email:AdminRequest.email,superadmin_password:AdminRequest.password,new_admin_email:AdminRequest.email,new_admin_password:AdminRequest.password):
    admin_creation_response=await create_admin(superadmin_email,superadmin_password,new_admin_email,new_admin_password)
    return admin_creation_response
    

@app.post("/admin/login")
async def admin_login(email:AdminRequest.email,password:AdminRequest.password):
    admin_login_response=await adminLogin(email,password)
    return admin_login_response

@app.post("/admin/addModelProvider")
async def add_model_provider(modelProviderID:str,modelID:str,providerName:str,providerURL:str,adminEmail:AdminRequest.email,adminPassword:AdminRequest.password):
    response=await addModelProvider(modelProviderID=modelProviderID,modelID=modelID,providerName=providerName,providerURL=providerURL,adminEmail=adminEmail,adminPassword=adminPassword)
    return response