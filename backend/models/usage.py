from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime

class Usage(Document):
    user=ReferenceField(User,required=True)
    model=ReferenceField(AIModel,required=True)
    provider=ReferenceField(ModelProviders,required=True)
    tokens_usage_mapped_to_date=DictField(required=True)  
    credits_used=FloatField(required=True)
    class Meta:
        collection="usage"