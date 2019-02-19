# From:
# Reactive Programming in Python
# Rudolf Olah


import tornado.ioloop
from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler



class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello World")

class ExchangeHandler(WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        pass

    def on_close(self):
        pass

class Server:
    class __Server:
        def __init__(self):
            self._app = make_app()

        def start(self):
            self._app.listen(8888)

    instance = None

    def __init__(self):
        if Server.instance is None:
            Server.instance = Server.__Server()

    def __getattr__(self, name):
        return getattr(self.instance, name)


def make_app():
    routes = [
        (r"/", MainHandler),
        (r'/exchenage',ExchangeHandler),
    ]
    return Application(routes)

if __name__ == '__main__':
    Server().start()
    tornado.ioloop.IOLoop.current().start()
