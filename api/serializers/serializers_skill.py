from rest_framework import serializers
from database import models

class skill_serializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = models.Skill
        fields = '__all__'