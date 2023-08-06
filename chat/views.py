from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChatSerializers
from .models import Message
from django.db.models import Q
from rest_framework import status


def index_view(req):
    data = {
        'message': "Hello world",
    }
    return JsonResponse(data)

class ChatView(APIView):
    def get(self, request, user_id=None):
        query_set = Message.objects.all()
        serializers_data =  ChatSerializers(query_set, many=True)
        if user_id:
            query_set = Message.objects.filter(Q(sender=user_id) | Q(receiver=user_id))
            serializers_data =  ChatSerializers(query_set, many=True)
        return Response(serializers_data.data)
        

    def post(self, request):
        serializers_data = ChatSerializers(data=request.POST)
        if serializers_data.is_valid():
            serializers_data.create(serializers_data.validated_data)
            return Response(serializers_data.data, status=status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)
