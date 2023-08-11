from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
# Create your views here.

# @api_view(['POST'])
# @permission_classes([])
# def get_token(req):
#     username = req.data['username']
#     password = req.data['password']

#     # Get user with this credentials
#     user = authenticate(req, username=username, password=password)
#     if user:
#         login(req, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key, 'user': user.id})
    
#     return Response({"error": 'Invalid credentials'}, status=400)
        

class GetToken(APIView):
    permission_classes = []

    def post(self, req, *args, **kwargs):
        username = req.data['username']
        password = req.data['password']

        # Get user with this credentials
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, 'user': user.id})
        
        return Response({"error": 'Invalid credentials'}, status=400)
    