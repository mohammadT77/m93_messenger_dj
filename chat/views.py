from django.http.response import JsonResponse
# from .models import Message
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@login_required(login_url='http://localhost:8000/admin/login')
def get_all_chat(req):
    all_receiver = map(lambda msg: msg.receiver.username, Message.objects.filter(sender=req.user))
    distinct_receivers = set(all_receiver)
    return JsonResponse({'data': list(distinct_receivers)})


@login_required(login_url='http://localhost:8000/admin/login')
def get_chat_messages(req):
    data = Message.objects.filter(sender=req.user)
    print("All messages:", data)
    
    # def to_dict(msg):
    #     return {
    #         'subject': msg.subject,
    #         'sender': msg.sender.username,
    #         'receiver': msg.receiver.username,
    #         'content': msg.content,
    #     }
    # data: List[Message]
    messages_serializer = MessageBriefSerializer(data, many=True)
    return JsonResponse({'data':messages_serializer.data})

@login_required(login_url='http://localhost:8000/admin/login')
def get_chat_with_receiver(req, receiver_id):
    data = Message.objects.filter(sender=req.user, receiver_id = receiver_id)
    print(f"Messages with {receiver_id}:", data)
    
    messages_serializer = MessageBriefSerializer(data, many=True)
    return JsonResponse({'data':messages_serializer.data})


@login_required(login_url='http://localhost:8000/admin/login')
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
