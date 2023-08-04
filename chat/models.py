from django.db import models
from core.models import BaseModel, User

# Create your models here.

class Message(BaseModel):
    subject = models.CharField(max_length=40)
    sender = models.ForeignKey(User, models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, models.CASCADE, related_name='received_messages')
    content = models.CharField(max_length=400)
    replay_ref = models.ForeignKey("Message", models.SET_NULL, null=True, default=None, blank=True)
    seen = models.BooleanField(default=False, null=False, blank=False)
    seen_timestamp = models.DateTimeField(default=None, null=True, blank=True)