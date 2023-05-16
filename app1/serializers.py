from rest_framework.serializers import ModelSerializer
from .models import *

class SerializerMachine(ModelSerializer):
    class Meta:
        model = Book_Model
        fields = '__all__'