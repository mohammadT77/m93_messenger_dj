from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics
# Create your views here.

@api_view(['GET'])
def get_all_chat(req):
    all_receiver = map(lambda msg: msg.receiver.username, Message.objects.filter(sender=req.user))
    distinct_receivers = set(all_receiver)
    return JsonResponse({'data': list(distinct_receivers)})

@api_view(['GET'])
def get_chat_messages(req):
    data = Message.objects.filter(sender=req.user)
    print("All messages:", data)
   
    messages_serializer = MessageBriefSerializer(data, many=True)
    return Response({'data':messages_serializer.data})

@api_view(['GET'])
def get_chat_with_receiver(req, receiver_id):
    data = Message.objects.filter(sender=req.user, receiver_id = receiver_id)
    print(f"Messages with {receiver_id}:", data)
    
    messages_serializer = MessageBriefSerializer(data, many=True)
    return Response({'data':messages_serializer.data})


@api_view(http_method_names=['POST'])
def post_new_message(req, receiver_id):
    data = req.data
    data['receiver'] = receiver_id
    data['sender'] = req.user.id
    message_serializer = MessageSerializer(data=req.data)
    if message_serializer.is_valid():
        new_message = message_serializer.save()
        return Response({'message': 'created', 'id': new_message.id}, status=status.HTTP_201_CREATED)
    else:
        return Response({'errors': message_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class MessageListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    model = Message
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)
    

class MessageReceivedListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    model = Message
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user, receiver_id=self.kwargs['receiver_id'])
    

from django.shortcuts import render
def index(req) :
    return render(req, 'client.html')