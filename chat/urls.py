from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_chat),
    path('messages/', get_chat_messages),
]
