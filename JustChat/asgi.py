import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import ChatApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JustChat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ChatApp.routing.websocket_urlpatterns
        )
    ),
})