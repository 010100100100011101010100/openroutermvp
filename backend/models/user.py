from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime

class User(Document):
    email=EmailField(required=True,unique=True)
    hashedpassword=StringField(required=True)
    creditbalance=FloatField(default=0.0)
    api_keys=ListField(StringField(),default=[])
    uid=StringField(required=True,unique=True)
    class Meta:
        collection="users"