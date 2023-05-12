from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/my-websocket/$', consumers.MyConsumer.as_asgi()),
    re_path(r'briansthing/$', consumers.BriansConsumer.as_asgi()),
]
