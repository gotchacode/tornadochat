from handlers.mainhandler import MainHandler
from handlers.newmessage import MessageNewHandler
from handlers.updatemessage import MessageUpdatesHandler

route = [
            (r"/", MainHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
        ]
