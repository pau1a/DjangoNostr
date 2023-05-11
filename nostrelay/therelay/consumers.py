from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
import json, asyncio, websockets

class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("hiho")
        self.websocket = await websockets.connect('ws://localhost:8765')

    async def receive(self):
        print("hiho")
        message = await self.websocket.recv()
        return json.loads(message)

    async def send(self, data):
        print("hiho")
        message = json.dumps(data)
        await self.websocket.send(message)

    async def disconnect(self):
        print("hiho")
        await self.websocket.close()
