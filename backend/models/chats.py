from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime
from models.user import User
from models.modelprovider import ModelProviders
from models.model import AIModel
from models.api import API


class ChatsConversation(Document):
    user=ReferenceField(User,required=True)
    model=ReferenceField(AIModel,required=True)
    modelProviderID=ReferenceField(ModelProviders,required=True)
    conversation_id=StringField(required=True,unique=True)
    conversation_history=ListField(DictField())
    API_key=ReferenceField(API,required=True)
    class Meta:
        collection="chatsconversation"