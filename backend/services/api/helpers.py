from random import random
from models.api import API

def create_api_key():
    #The general format of our API key will be "or-" followed by a 12 bit random number which we have to ensure is not in our database
    api_key=""
    chars="abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(12):
        api_key+=chars[int(random()*len(chars))]
    return "or-"+api_key