from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime
from models.user import User



class Billing(Document):
    user=ReferenceField(User,required=True)
    amount=FloatField(required=True)
    billing_date=DateTimeField(required=True)
    credits_added=FloatField(required=True)
    class Meta:
        collection="billing"