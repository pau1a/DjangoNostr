from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
from .parsers import parse_message
import json, asyncio, websockets

class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("Connected to websocket")
        await self.accept()

    async def disconnect(self, fled):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type, *rest = text_data_json
        await parse_message(message_type, rest)

        await self.send(text_data=json.dumps({
            'data': list(["NOTICE", "Under test"]),
            'other_key': "other_value"
        }))
