from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
import json, asyncio, websockets

class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("hiho1")
        #self.websocket = await websockets.connect('ws://165.22.113.110:13167/ws/my-websocket/')

    async def receive(self):
        print("hiho2")
        message = await self.websocket.recv()
        return json.loads(message)

    async def send(self, data):
        print("hiho3")
        message = json.dumps(data)
        await self.websocket.send(message)

    async def disconnect(self):
        print("hiho4")
        await self.websocket.close()
