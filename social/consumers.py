import json
from django.core.checks import messages
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from social.models import chat_model, userdt_model
from django.contrib.auth import get_user_model

x = None


class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        room_name = self.scope['url_route']['kwargs']['room_name']
        x = chat_model.objects.all()
        if len(x) > 51:
            messages = chat_model.objects.filter(
                room_name=room_name).order_by("cr_time")[:50]
        else:
            messages = chat_model.objects.filter(
                room_name=room_name).order_by("cr_time")

        content = {

            'message': self.messages_to_json(messages)
        }

        self.send_message(content)

    def new_message(self, data):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        author = self.scope['user']
        aut = userdt_model.objects.get(user=author)

        message = chat_model.objects.create(
            body=data['message'],
            room_name=self.room_name,
            author=aut.user,

        )
        message.save()

        content = {
            'command': 'new_message',
            'message': self.message_to_json(message),
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return{
            'author': str(message.author),
            'body': message.body,
            'time': str(message.cr_time),
            'room_name': message.room_name,
        }

    commands = {
        "fetch_messages": fetch_messages,
        "new_message": new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)

        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group

    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
