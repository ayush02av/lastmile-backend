from rest_framework import status
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

class skill_user(APIView):
    serializer_class = serializers_skill.skilluser_serializer
    
    def get(self, request, skill):
        try:
            return Response(
                self.serializer_class(
                    models.SkillUser.objects.filter(
                        skill = models.Skill.objects.get(name__iexact = skill)
                    ).order_by('-rating'),
                many = True).data
            )

        except Exception as exception:
            return Response({
                'message': 'Skill does not exist',
                'exception': exception.__str__()
            }, status = status.HTTP_404_NOT_FOUND)