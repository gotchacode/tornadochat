"""
simple python chat server
"""
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define, options, parse_command_line
from handlers.routes import route

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


def main():
    """
    main application entry point
    """
    parse_command_line()
    app = tornado.web.Application(
        route,
        cookie_secret="adnadfhaihjngjwgegegjsofsknfmadajdn",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=False,
        debug=options.debug,
    )
    print("Server running at http://localhost:8888")
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
