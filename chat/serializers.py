from rest_framework import serializers
from .models import Message


class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)
