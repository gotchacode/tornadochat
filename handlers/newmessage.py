import tornado.web
import uuid
import json
from .buffer import MessageBuffer

global_message_buffer = MessageBuffer()


class MessageNewHandler(tornado.web.RequestHandler):
    def get_data(self):
        jsonfile = open("imdb.json")
        json_data = json.load(jsonfile)
        return json_data, len(json_data)

    def post(self):
        from random import randint
        imdb_data, length = self.get_data()
        random_int = randint(0, length - 1)
        message = {
            "id": str(uuid.uuid4()),
            "body": self.get_argument("body"),
            "secret_message": imdb_data[random_int],
        }

        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message))

        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        global_message_buffer.new_messages([message])
