from models.admin import Admin
from models.modelprovider import ModelProviders
from models.model import Model
def create_admin(email,password,superadminmail,superadminpassword)-> dict:
    if superadminmail=="raseshh1827@gmail.com" and superadminpassword=="123456":
        newadmin=Admin(email=email,password=password)
        newadmin.save()
        return {"message":"Admin created successfully"}
    else:
        return {"message":"Unauthorized"},401
    

async def adminLogin(email:str,password:str):
    admin=Admin.objects(email=email).first()
    if admin and admin.password==password:
        return {"message":"Admin login successful"}
    else:
        return {"message":"Invalid email or password"},401

async def addModelProvider(modelProviderID:str,modelID:str,providerName:str,providerURL:str,adminEmail:str,adminPassword:str):
    admin=Admin.objects(email=adminEmail).first()
    if not admin or admin.password!=adminPassword:
        return {"message":"Unauthorized"},401
    else:
        if adminPassword!=Admin.objects(adminEmail=adminEmail).first().password:
            return {"message":"Unauthorized"},401
        else:
            mP=ModelProviders(modelProviderID=modelProviderID,model=modelID,providerName=providerName,providerURL=providerURL)
            mP.save()
            return {"message":"Model provider added successfully"}



async def addModel(name:str,description:str,providers:list,creators:list,token_price:float,model_size:str,model_type:str,inputmodality:str,outputmodality:str,model_slug:str,adminEmail:str,adminPassword:str):
    if(not Admin.objects(email=adminEmail).first() or Admin.objects(email=adminEmail).first().password!=adminPassword):
        return {"message":"Unauthorized"},401
    else:
        if adminPassword!=Admin.objects(email=adminEmail).first().password:
            return {"message":"Unauthorized"},401
        else:
            newModel=Model(name=name,description=description,providers=providers,creators=creators,token_price=token_price,model_size=model_size,model_type=model_type,inputmodality=inputmodality,outputmodality=outputmodality,model_slug=model_slug)
            newModel.save()
            return {"message":"Model added successfully"}
        
    
