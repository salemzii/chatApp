import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Group

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name =  f"chat_{self.room_name}" #'chat_%s' % self.room_name
        self.grp_name, created = Group.objects.get_or_create(name=self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.grp_name.name,
            self.channel_name
        )

        self.accept()



    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.grp_name.name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.grp_name.name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        Message.objects.create(
            author= self.scope['user'],
            group= self.grp_name,
            content= message
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))


    def send_message(self, message):
        self.send(text_data=json.dumps(message))


