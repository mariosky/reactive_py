
from tornado.ioloop import IOLoop
from rx.concurrency import IOLoopScheduler
from tornado.queues import PriorityQueue, QueueEmpty

from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler

from rx import Observable
from rx.subjects import Subject
from  order import Order


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello World")

class ExchangeHandler(WebSocketHandler):
    def open(self):
        Server().messages.on_next(['opened',self.request])
        scheduler = IOLoopScheduler(IOLoop.current())
        def send_order(i):
            for order in Server().posted_orders:
                self.write_message("{}".format(order))
        timer = Observable.interval(1000,scheduler=scheduler)
        self.order_sender = timer.subscribe(send_order)



    def on_message(self, message):
        Server().messages.on_next(['message', message])

    def on_close(self):
        Server().messages.on_next(['closed', self.request])
        self.order_sender.dispose()

class Server:
    class __Server:
        def __init__(self):
            scheduler = IOLoopScheduler(IOLoop.current())
            self._app = make_app()
            self.orders = PriorityQueue()
            self.posted_orders = []
            self.fulfilled_orders = []

            self.messages = Subject()

            only_messages = self.messages.filter(lambda msg: msg[0] == 'message')\
                .map(lambda msg : msg[1].split(',')).publish()

            def queue_order(msg):
                self.orders.put(Order.from_list(msg))


            only_messages \
                .filter(lambda msg: msg[0] == 'order') \
                .map(lambda msg : msg[1:])\
                .subscribe(queue_order)

            def process_order(time):
                try:
                    order = self.orders.get_nowait()
                    print('processing order: {} [{}]'.format(
                        order, order.timestamp))
                    matching = None
                    for posted in self.posted_orders:
                        if posted.matches(order):
                            matching = posted
                            break

                    if matching is None:
                        self.posted_orders.append(order)
                        print('could not find match, posted order count is {}'.format(len(self.posted_orders)))
                    else:
                        self.posted_orders.remove(posted)
                        self.fulfilled_orders.append(posted)
                        self.fulfilled_orders.append(order)
                        print('order fulfilled: {}'.format(order))
                        print('fulfilled by: {}'.format(posted))
                except QueueEmpty:
                    pass

            Observable.interval(100, scheduler=scheduler).subscribe(process_order)
            only_messages.connect()




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
        (r'/exchange',ExchangeHandler),
    ]
    return Application(routes)

if __name__ == '__main__':
    Server().messages \
        .filter(lambda msg: msg == 'opened') \
        .subscribe(lambda msg: print('Connection has been opened'))
    Server().start()
    IOLoop.current().start()
