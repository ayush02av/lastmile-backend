import jwt
from database.models import User
from rest_framework import status
from rest_framework.response import Response

def get_user(details):
    try:
        user = User.objects.get(
            username = details['nickname']
        )
        return user
    except:
        return None

def get_or_create_user(userinfo):
    try:
        new_user = User.objects.get(
            sub = userinfo['sub']
        )
    except:
        new_user = User.objects.create_user(
            username = userinfo['nickname'],
            first_name = userinfo['given_name'],
            last_name = userinfo['family_name'],
            email = userinfo['email'],
            sub = userinfo['sub'],
            sid = userinfo['sid']
        )
        new_user.save()

    return new_user

def get_user_from_request(request):
    if 'Authorization' not in request.headers.keys():
        return False, Response({
            'detail': 'Not logged in'
        }, status = status.HTTP_401_UNAUTHORIZED)
    
    token = request.headers['Authorization'].split()[1]
    decoded = jwt.decode(token, options={"verify_signature": False})

    return True, get_user(decoded)