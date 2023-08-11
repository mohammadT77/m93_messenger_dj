from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_chat),
    path('messages/', get_chat_messages),
    path('<int:receiver_id>/', get_chat_with_receiver),
    path('<int:receiver_id>/create/', post_new_message),
]
