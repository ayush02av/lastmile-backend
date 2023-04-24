from rest_framework import serializers
from database import models
from api.serializers import serializers_user

class collab_serializer(serializers.ModelSerializer):
    from_user = serializers_user.user_serializer
    to_user = serializers_user.user_serializer
    
    class Meta(object):
        model = models.Collab
        fields = '__all__'