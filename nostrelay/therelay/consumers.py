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
        trumpet = " TOOT TOOT"
        print("hiho2")
        text_data_json = json.loads(text_data)
        the_index = text_data_json[0]
        print("BRIANS BIT IS -------------->    " + str(text_data_json))
        message = text_data_json[the_index]
        print(message)

        await self.send(text_data=json.dumps({
            'message': str(message) + trumpet 
        }))


class BriansConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("hi Im brian")
        await self.accept()

    async def disconnect(self, fled):
        print("hiho4")
        pass

    async def receive(self, text_data):
        trumpet = " POOP TOOT"
        print("hiho2000 away ")
        text_data_json = json.loads(text_data)
        the_index = text_data_json[0]
        print("BRIANS BIT IS -------------->    " + str(text_data_json))
        message = text_data_json[the_index]
        print(message)

        await self.send(text_data=json.dumps({
            'message': str(message) + trumpet
        }))
