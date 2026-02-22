from services.modelproviders.groq import groq_completions_query
from services.modelproviders.hugging import hugging_completions_query
from models.chats import ChatsConversation
from models.user import User
from models.api import API
import random
from models.modelprovider import ModelProviders

def create_random_id(length:int=16)->str:
    characters="abcdefghijklmnopqrstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_id="".join(random.choice(characters) for _ in range(length))
    return random_id


async def save_conversation_to_db(uid:str,API_key:str,providerId:str,conversation_id:str="",user_message:str="",assistant_message:str="")->None:
    if conversation_id=="":
        conversation_id=create_random_id()
        conversations=[]
        conversations.append({"role":"user","content":user_message})
        conversations.append({"role":"assistant","content":assistant_message})
        conversation_updated=ChatsConversation(user=User.objects(uid=uid).first(),conversation_id=conversation_id,conversation_history=conversations,API_key=API.objects(key=API_key).first(),model=ModelProviders.objects(modelProviderID=providerId).first().model)
        conversation_updated.save()
        print("New conversation created with ID:", conversation_id)
    else:
        conversation_updated=ChatsConversation.objects(conversation_id=conversation_id).first()
        if conversation_updated:
            conversation_updated.conversation_history.append({"role":"user","content":user_message})
            conversation_updated.conversation_history.append({"role":"assistant","content":assistant_message})
            conversation_updated.save()
            print("Conversation updated with ID:", conversation_id)
        else:
            print("Conversation not found with ID:", conversation_id)
    


    
async def generate(prompt:str,uid:str,model:str,temperature:float,max_tokens:int,modelprovider:str,modelproviderid:str,system_prompt:str="You are a helpful assistant",conversation_id:str="")->str:
    if modelprovider=="groq":
        response= await groq_completions_query(ai=model,prompt=prompt,temperature=temperature,max_tokens=max_tokens,system_prompt=system_prompt)
        save_conversation_to_db(uid=uid,providerId=modelproviderid,conversation_id=conversation_id,)
    elif modelprovider=="hugging":
        response= hugging_completions_query(ai=model,prompt=prompt,temperature=temperature,max_tokens=max_tokens,system_prompt=system_prompt)
    else:
        return "Invalid model provider"
    