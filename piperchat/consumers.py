import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name
		self.user = self.scope['user']

		# Join room group
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		await self.accept()

	async def disconnect(self, close_code):
		# Leave room group
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)

	# Receive message from WebSocket
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		message_type = text_data_json['message_type']
		msgtime = text_data_json['msgtime']
		# Send message to room group
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message,
				'message_type': message_type,
				'msgtime': msgtime,
				'username': self.scope['user'].username,
			}
		)

	# Receive message from room group
	async def chat_message(self, event):
		message = event['message']
		username = event['username']
		msgtime = event['msgtime']
		message_type = event['message_type']
		# Send message to WebSocket
		await self.send(text_data=json.dumps({
			'message': message,
			'username': username,
			'msgtime': msgtime,
			'message_type': message_type,
		}))


class Notification(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = "Notification"
		self.room_group_name = "NotificationGroup"
		print("connected to the notification group")
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)
		await self.accept()

	
	async def disconnect(self, close_code):
		# Leave room group
		print("disconnected to the notification group")
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['secret_room_name']
		other_username = text_data_json['other_username']
		print(other_username)
		# Send message to room group
		print('secret room name ' + message)
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message,
				'other_username': other_username,
			}
		)

	async def chat_message(self, event):
		message = event['message']
		other_username = event['other_username']
		# Send message to WebSocket
		print('inside chat_message function 	')
		await self.send(text_data=json.dumps({
			'message': message,
			'other_username': other_username,
		}))