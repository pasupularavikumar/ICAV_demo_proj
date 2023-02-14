from rest_framework import serializers
from .models import *

 
class bookSerializer(serializers.HyperlinkedModelSerializer):    
    
    class Meta:
        model = Book    
        fields = '__all__'