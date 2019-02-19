# From:
# Reactive Programming in Python
# Rudolf Olah


import asyncio
from random import choice

from rx import Observable
from rx.subjects import Subject
from rx. concurrency import IOLoopScheduler

from tornado.ioloop import IOLoop
from tornado.websocket import websocket_connect


class Client:
    def __init__(self, host='localhost', port='8888'):
        self._url = 'ws://{}:{}/exchange'.format(host,port)
        self.connection = None
        self.opened = Subject()
        self.messages = Subject()

    def connect(self):

        def on_message_callback(message):
            self.messages.on_next(message)

        def on_connect(conn):
            self.connection = conn
            self.opened.on_next(conn)
            self.opened.on_completed()
            self.opened.dispose()

        future_connection = websocket_connect(self._url, on_message_callback=on_message_callback)
        Observable.from_future(future_connection).subscribe(on_connect)

    def write_message(self, message):
        self.connection.write_message(message)


if __name__ == '__main__':
    scheduler = IOLoopScheduler(IOLoop.current())

    def make_say_hello(client, i):
        def schedule_say_hello(conn):
            Observable.interval(choice([300,500,1000,2000]), scheduler=scheduler)\
            .subscribe(lambda value : client.write_message("Hola desde el Cliente: #{}".format(i)))
        return schedule_say_hello

    for i in range(10):
        client = Client()
        client.messages.subscribe(lambda message : print(message))
        client.opened.subscribe(lambda message : print("Connection Opened Cliente {}".format(i)))
        client.opened.subscribe(make_say_hello(client,i))
        client.connect()

    IOLoop.current().start()








