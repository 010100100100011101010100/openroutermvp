from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime

class ModelProviders(Document):
    model=ReferenceField(AIModel, required=True)
    providerName=StringField(required=True)
    providerURL=URLField(required=True)
    class Meta:
        collection="modelproviders"