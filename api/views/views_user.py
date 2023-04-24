from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import serializers_user
from database import models
from api.controllers import user_controller
import json

class user(APIView):
    serializer_class = serializers_user.user_serializer
    
    def get(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]

        user = user[1]
        
        serializer = self.serializer_class(user, many = False)

        return Response(serializer.data)
    
class add(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]

        try:
            interest = int(request.data.get('interest'))

            if interest in serializers_user.user_serializer(user, many = False).data['interests']:
                return Response({
                    'message': 'Skill already added'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            skill_object = models.Skill.objects.get(id = interest)
            user.interests.add(skill_object)
            models.Skill.objects.filter(id = interest).update(count = skill_object.count + 1)
            return Response({
                'message': 'Skill added'
            }, status=status.HTTP_202_ACCEPTED)
            
        except Exception as exception:
            return Response({
                'message': 'Skill does not exist',
                'detail': exception.__str__()
            }, status = status.HTTP_400_BAD_REQUEST)

class start(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]

        try:
            name = request.data.get('name')
            category = int(request.data.get('category'))
            venue_options = json.loads(request.data.get('venue_options'))

            if category not in serializers_user.user_serializer(user, many = False).data['interests']:
                return Response({
                    'message': 'Category not in user interests'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            event = models.Event(
                name = name,
                organizer = user,
                venue_options = venue_options,
                category = models.Skill.objects.get(id=category)
            )
            event.save()
            
            models.EventParticipant(
                event = event,
                user = user,
            ).save()
            
            return Response({
                'message': 'Event created'
            }, status=status.HTTP_202_ACCEPTED)
            
        except Exception as exception:
            return Response({
                'message': 'Invalid request',
                'detail': exception.__str__()
            }, status = status.HTTP_400_BAD_REQUEST)

class join(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]

        try:
            event = request.data.get('event')
            
            event = models.Event.objects.get(id = event)

            if len(models.EventParticipant.objects.filter(event = event, user = user)) != 0:
                return Response({
                    'message': 'Event already joined'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            models.EventParticipant(
                event = event,
                user = user,
            ).save()
            
            return Response({
                'message': 'Event joined'
            }, status=status.HTTP_202_ACCEPTED)
            
        except Exception as exception:
            return Response({
                'message': 'Invalid request',
                'detail': exception.__str__()
            }, status = status.HTTP_400_BAD_REQUEST)