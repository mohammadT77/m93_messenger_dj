from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['seen_timestamp','create_timestamp','delete_timestamp','modify_timestamp',]