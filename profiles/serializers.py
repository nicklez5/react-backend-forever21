from rest_framework import serializers
from django.db import models
from .models import Profile
class SerializeProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['address']
    
    def update(self,instance,validated_data):
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance 