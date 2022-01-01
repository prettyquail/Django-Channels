from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator


# application = ProtocolTypeRouter({
#     'websocket' : URLRouter([
#         path('ws/test/', TestConsumer()),
#         path('ws/chat/',EchoConsumer()),
#     ])
#
# })
from .consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/Chat/',ChatConsumer()),
                ]
            )
        )
    )
})