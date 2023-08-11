from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_chat),
    path('messages/', MessageListView.as_view()),
    path('<int:receiver_id>/', MessageReceivedListView.as_view()),
    path('<int:receiver_id>/create/', post_new_message),
    # path('x/', XView.as_view()),
]
