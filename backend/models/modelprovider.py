from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime
from models.model import AIModel

class ModelProviders(Document):
    modelProviderID=StringField(required=True,unique=True)
    model=ReferenceField(AIModel, required=True)
    providerName=StringField(required=True,choices=["groq","hugging"])
    providerURL=URLField(required=True)
    class Meta:
        collection="modelproviders"