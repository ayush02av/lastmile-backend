from rest_framework import serializers
from database import models

class event_serializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = models.Event
        fields = '__all__'