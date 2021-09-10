from django.contrib import admin
from .models import Message, Group, Groupmember

admin.site.register(Message)
admin.site.register(Group)
admin.site.register(Groupmember)

# Register your models here.
