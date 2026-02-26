#CRUD for API endpoint (this will be used to store API keys taki we can use them jab curl request karein)

from models.api import API
from datetime import datetime
from models.user import User
from api.helpers import create_api_key
async def create_api_key(uid:str)-> str:
    if not User.objects(uid=uid):
        raise Exception("User not found")
    created_api_key=create_api_key()
    while created_api_key in API.objects(api_value=created_api_key):
        created_api_key=create_api_key()
    timenow=datetime.now()
    api_key=API(uid=uid,api_value=created_api_key,created_at=timenow)
    api_key.save()
    api_key_list=User.objects(uid=uid).first().api_keys
    api_key_list.append(created_api_key)
    User.objects(uid=uid).update(api_keys=api_key_list)
    return created_api_key
    

async def delete_api_key(api_value:str)->dict:
    API.objects(api_value=api_value).delete()
    User.objects(uid=API.objects(api_value=api_value).first().uid).update(pull__api_keys=api_value)
    return {"message":"API key deleted successfully"}
    

async def regenerate_api_key(api_value:str) -> str:
    if not API.objects(api_value=api_value):
        raise Exception("API key not found")
    regenerated_api_value=create_api_key()
    while regenerated_api_value in API.objects(api_value=regenerated_api_value):
        regenerated_api_value=create_api_key()
    API.objects(api_value=api_value).update(api_value=regenerated_api_value,created_at=datetime.now())
    api_keys_list=User.objects(uid=API.objects(api_value=regenerated_api_value).first().uid).first().api_keys
    api_keys_list.remove(api_value)
    api_keys_list.append(regenerated_api_value)
    User.objects(uid=API.objects(api_value=regenerated_api_value).first().uid).update(api_keys=api_keys_list)
    return regenerated_api_value

    

async def get_api_keys(uid:str)->list:
    api_keys_list=User.objects(uid=uid).first().api_keys
    return api_keys_list

