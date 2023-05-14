from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from . import consumers
from django.http import HttpResponse

def list_open_websockets(request):
    channel_layer = get_channel_layer()
    print(dir(channel_layer))
    all_channels = channel_layer.channels("websocket")
    open_websockets = []
    for channel in all_channels:
        group_name = channel.split("_")[0]
        group_channels = channel_layer.group_channels(group_name)
        for group_channel in group_channels:
            if group_channel == channel:
                open_websockets.append(channel)
                break
    return HttpResponse(str(open_websockets))

#def my_view(request):
#    channel_layer = get_channel_layer()
#    async_to_sync(channel_layer.group_add)("my_group", request.channel_name)
#    consumer = consumers.MyConsumer()
#    await consumer.connect()
#    message = await consumer.receive()
#    await consumer.send({"type": "hello"})
#    await consumer.disconnect()
#    return render(request, "my_template.html")
