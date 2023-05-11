from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
import json, asyncio, websockets

class MyConsumer:

    async def connect(self):
        self.websocket = await websockets.connect('ws://localhost:8765')

    async def receive(self):
        message = await self.websocket.recv()
        return json.loads(message)

    async def send(self, data):
        message = json.dumps(data)
        await self.websocket.send(message)

    async def disconnect(self):
        await self.websocket.close()
