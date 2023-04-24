from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import serializers_user, serializers_collab
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
            models.SkillUser(skill = skill_object, user = user).save()

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

class start_collab(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]
        
        try:
            target_user = models.User.objects.get(id = request.data.get('to'))
            skill = models.Skill.objects.get(name = request.data.get('skill'))

            models.Collab(
                from_user = user,
                to_user = target_user,
                skill = skill
            ).save()
            
            return Response({
                'detail': 'Collab requested'
            })

        except:
            return Response({
                'detail': 'Target user or skill does not exist'
            }, status = status.HTTP_404_NOT_FOUND)

class incoming_collabs(APIView):
    serializer_class = serializers_collab.collab_serializer
    
    def get(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]
        
        return self.serializer_class(
            models.Collab.objects.filter(
                to_user = user,
                accepted = False,
                rejected = False
            )
            , many = True).data

class react_collab(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]
        
        try:
            if request.data.get('reaction') == 1:
                models.Collab.objects.filter(
                    id = request.data.get('collab'),
                ).update(
                    accepted = True
                )
            else:
                models.Collab.objects.filter(
                    id = request.data.get('collab'),
                ).update(
                    rejected = True
                )
            
            return Response({
                'detail': 'Reacted to collab'
            }, status = status.HTTP_202_ACCEPTED)
            
        except:
            return Response({
                'detail': 'Collab does not exist'
            }, status = status.HTTP_404_NOT_FOUND)

class end_collab(APIView):
    def post(self, request):
        user = user_controller.get_user_from_request(request)

        if user[0] == False:
            return user[1]
        
        user = user[1]
        
        try:
            models.Collab.objects.filter(
                id = request.data.get('collab'),
            ).update(
                rating = request.data.get('rating'),
                ended = True
            )
            
            return Response({
                'detail': 'Ended and rated collab'
            }, status = status.HTTP_202_ACCEPTED)
            
        except:
            return Response({
                'detail': 'Collab does not exist'
            }, status = status.HTTP_404_NOT_FOUND)