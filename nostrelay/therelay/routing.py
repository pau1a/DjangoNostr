from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'/', consumers.MyConsumer.as_asgi()),
    re_path(r'', consumers.MyConsumer.as_asgi())
]
