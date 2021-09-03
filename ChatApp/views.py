from django.shortcuts import render
import json
from .models import Group, Message
from django.http import JsonResponse

def index(request):
    return render(request, 'ChatApp/index.html', {})


def room(request, room_name):

    return render(request, 'ChatApp/room.html', {
        'room_name': room_name
    })


def getmessages(request, roomName):
    
    groupname = roomName
    print(f"fetching group {groupname} ...../")
    
    grp = Group.objects.get(name=groupname)
    messages = Message.objects.filter(group=grp)
    context = {
        'messages': messages_to_json(messages)
    }

    return JsonResponse(context, safe=False)


def messages_to_json(messages):
    result = []
    for message in messages:
        result.append(message_to_json(message))
    return result


def message_to_json(message):
    return {
        'id': message.id,
        'author': message.author.username,
        'content': message.content,
        'timestamp': str(message.time)
    }

