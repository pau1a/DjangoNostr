"""
ASGI config for nostrelay project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os, logging, ssl, logging.config
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from channels.middleware import BaseMiddleware
from channels.security.websocket import OriginValidator
import django
django.setup()
from therelay import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nostrelay.settings')


#settings.configure()
django_asgi_app = get_asgi_application()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#logging.info(django_asgi_app)

def log_ssl_info(conn):
    logging.debug("TLS connection established: %s", conn.cipher())

#ssl_context.set_servername_callback(lambda conn, server_name: log_ssl_info(conn))

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": 
    AuthMiddlewareStack(
      URLRouter(
        routing.websocket_urlpatterns
      )
  ),
})
