from django.shortcuts import render
import json
from .models import Group, Message, Groupmember
from django.contrib.auth.models import User
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


def make_admin(request, UserId):
    to_make = User.objects.get(id=UserId)
    if request.user.is_admin():
        to_make.is_admin = True
        to_make.save()
    else:
        print("Member without admin permissions can't perform this operation")
    return JsonResponse(f"{to_make.username}, is now an admin", safe=False)



def add_to_chat_group(request, userId):

    requester = request.user
    print(requester)
    requestee = User.objects.get(id=userId)
    groupName = f"{requester}&&{requestee}"
    created_group = Group.objects.create(name=groupName, private=True)
    grp1 = Groupmember.objects.create(user=requester, group=created_group)
    grp2 = Groupmember.objects.create(user=requestee, group=created_group)
    grp1.save()
    grp2.save()
    return JsonResponse('Personnal Group Created Successfully!', safe=False)


def create_group(request):

    if request.method == "POST":
        data = {}
        data['name'] = request.POST['name']
        if data:
            grp = Group.objects.create(name=data['name'])
            grp.save()
            Groupmember.objects.create(user=request.user, group=grp)
        else:
            pass
    return JsonResponse('Group Created Successfully!', safe=False)


