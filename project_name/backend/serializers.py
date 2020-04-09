from rest_framework import serializers
from .models import #Models

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model 
        fields = '__all__'