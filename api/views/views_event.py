from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import serializers_event
from database import models

class events(APIView):
    serializer_class = serializers_event.event_serializer
    
    def get(self, request):
        result = list()
        
        queryset = models.Event.objects.filter(ended = False)
        serializer = self.serializer_class(queryset, many = True).data
        result += serializer
        
        queryset = models.Event.objects.filter(ended = True)
        serializer = self.serializer_class(queryset, many = True).data
        result += serializer

        return Response(result)