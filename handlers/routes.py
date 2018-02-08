from handlers.mainhandler import MainHandler
from handlers.newmessage import MessageNewHandler
from handlers.updatemessage import MessageUpdatesHandler, EchoWebSocket

route = [
            (r"/", MainHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/websocket", EchoWebSocket),
            (r"/a/message/updates", MessageUpdatesHandler),
        ]
