from django.shortcuts import render

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from . import consumers

def my_view(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_add)("my_group", request.channel_name)
    consumer = consumers.MyConsumer()
    await consumer.connect()
    message = await consumer.receive()
    await consumer.send({"type": "hello"})
    await consumer.disconnect()
    return render(request, "my_template.html")
