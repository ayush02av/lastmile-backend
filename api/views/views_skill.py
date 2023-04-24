from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import serializers_skill
from database import models

class skills(APIView):
    serializer_class = serializers_skill.skill_serializer
    
    def get(self, request):
        queryset = models.Skill.objects.all()

        serializer = self.serializer_class(queryset, many = True)

        return Response(serializer.data)