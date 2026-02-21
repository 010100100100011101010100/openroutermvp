from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime


class ChatsConversation(Document):
    user=ReferenceField(User,required=True)
    model=ReferenceField(AIModel,required=True)
    provider=ReferenceField(ModelProviders,required=True)
    conversation_id=StringField(required=True,unique=True)
    conversation_history=ListField(DictField())
    class Meta:
        collection="chatsconversation"