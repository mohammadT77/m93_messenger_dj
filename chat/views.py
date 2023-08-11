from django.http.response import JsonResponse
from .models import Message
from django.contrib.auth.decorators import login_required
from .serializers import *
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

# @csrf_exempt
# def index_post(req):
#     pass