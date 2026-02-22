from mongoengine import (Document,StringField,DateTimeField,IntField,FloatField,EmailField,ListField,BooleanField,ReferenceField,URLField,DictField)
import datetime
from enum import Enum
class ModelType(Enum):
    OPEN_SOURCE="open_source"
    PROPRIETARY="proprietary"
    TRANSFORMER="transformer"
    RNN="rnn"
    CNN="cnn"
    GAN="gan"
    LSTM="lstm"

class ModalityType(Enum):
    TEXT="text"
    MULTIMODAL="multimodal"
    IMAGE="image"
    AUDIO="audio"
    VIDEO="video"
    STRUCTUREDDATA="structureddata"
    CODE="code"

class AIModel(Document):
    name=StringField(required=True)
    description=StringField()
    providers=ListField(StringField())
    token_price=FloatField(required=True)
    model_size=StringField(required=True)
    model_type=StringField(required=True,choices=[model_type.value for model_type in ModelType])
    inputmodality=StringField(required=True,choices=[modality.value for modality in ModalityType])
    outputmodality=StringField(required=True,choices=[modality.value for modality in ModalityType])
    model_slug=StringField(required=True,unique=True)
    class Meta:
        collection="aimodels"