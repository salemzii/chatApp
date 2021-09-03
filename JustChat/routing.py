from channels.routing import ProtocolTypeRouter
from channels.http import AsgiHandler

application = ProtocolTypeRouter({
      "http": AsgiHandler(),
})