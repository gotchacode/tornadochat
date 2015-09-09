import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define, options, parse_command_line
from handlers.buffer import MessageBuffer
from handlers.newmessage import MessageNewHandler
from handlers.updatemessage import MessageUpdatesHandler

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")
global_message_buffer = MessageBuffer()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=global_message_buffer.cache)


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
        ],
        cookie_secret="adnadfhaihjngjwgegegjsofsknfmadajdn",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=False,
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
