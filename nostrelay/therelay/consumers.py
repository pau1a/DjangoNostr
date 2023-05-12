from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
import json, asyncio, websockets

class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("hiho1")
        await self.accept()

    async def disconnect(self, fled):
        print("hiho4")
        pass

    async def receive(self, text_data):
        print("hiho2")
        text_data_json = json.loads(text_data)
        message = text_data_json[1]

        await self.send(text_data=json.dumps({
            'message': message
        }))
