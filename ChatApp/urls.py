from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:roomName>/messages/', views.getmessages, name='getmsg'),
    path('add_chat/<int:userId>', views.add_to_chat_group, name='add-chat'),
    path('create_group', views.create_group, name='create-group'),
]