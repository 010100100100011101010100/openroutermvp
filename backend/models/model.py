from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime

class AIModel(Document):
    name=StringField(required=True)
    description=StringField()
    providers=ListField(StringField())
    token_price=FloatField(required=True)
    model_slug=StringField(required=True,unique=True)
    class Meta:
        collection="aimodels"