from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=101)
    created = models.DateTimeField(default=timezone.now)
    members = models.ForeignKey(User, on_delete=models.DO_NOTHING,
     null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, related_name='authormsg',
    on_delete=models.CASCADE)

    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.author.username
    
    def last_12_msg(self):
        return Message.objects.order_by('-time').all


# Create your models here.
