#We have to write two things
#1st is signup function, 2nd is login function -> Then I will write all supporting functions for both


from models import user
import bcrypt
from pydantic import EmailStr as url



def randomHashFunction(input:str)->str:
    salt=bcrypt.gensalt(rounds=12)
    input=input.encode('utf-8')
    hashed=bcrypt.hashpw(input,salt)
    return hashed.decode('utf-8')

def verifyHashFunction(input:str,hashed:str)->bool:
    input=input.encode('utf-8')
    hashed=hashed.encode('utf-8')
    return bcrypt.checkpw(input,hashed)

async def signup(email:url,password:str):
    if user.User.objects(email=email).first():
        return {"message":"Email already exists"}
    hashedpassword=randomHashFunction(password)
    uid=randomHashFunction(email)
    new_user=user.User(email=email,hashedpassword=hashedpassword,uid=uid)
    new_user.save()
    return {"message":"User created successfully"}

async def login(email:url,password:str):
    existing_user=user.User.objects(email=email).first()
    if not existing_user:
        return {"message":"User does not exist"}
    if verifyHashFunction(password,existing_user.hashedpassword):
        return {"message":"Login successful","uid":existing_user.uid}
    else:
        return {"message":"Invalid password"}
    