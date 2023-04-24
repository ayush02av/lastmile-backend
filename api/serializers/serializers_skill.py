from rest_framework import serializers
from database import models
from api.serializers import serializers_user

class skill_serializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = models.Skill
        fields = '__all__'

class skilluser_serializer(serializers.ModelSerializer):
    user = serializers_user.user_serializer
    
    class Meta(object):
        model = models.SkillUser
        fields = '__all__'