from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime




class API(Document):
    user=ReferenceField(User, required=True)
    api_value=StringField(required=True,unique=True)
    created_at=DateTimeField(required=True,default=datetime.datetime.now)
    updated_at=DateTimeField(default=None)
    is_active=BooleanField(default=True)
    class Meta:
        collection="apis"