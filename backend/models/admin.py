from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime


class Admin(Document):
    email=EmailField(required=True,unique=True)
    password=StringField(required=True)
    class Meta:
        collection="admins"