from rest_framework import serializers
from database import models

class user_serializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = models.User
        exclude = (
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'last_login',
            'sub',
            'sid',
            'groups',
            'user_permissions',
            'date_joined',
        )