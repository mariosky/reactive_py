

class Channel(object):
    def set_callback(self,callback):
        self.callback = callback

    def notify(self, value):
        self.callback(value)


class Parser(object):
    def __init__(self, transport):
        transport.set_callback(self.on_data)
        self.state = self.sync
        self.remaining_size = 0

    def on_data(self, data):
        self.state(data)

    def error(self, data):
        print("error: {}".format(data))

    def sync(self, data):
        if data == 42:
            self.state = self.size
        else:
            self.state = self.error

    def size(self, data):
        self.remaining_size = data
        self.state = self.payload

    def payload(self, data):
        if self.remaining_size > 0:
            print("payload: {}".format(data))
        self.remaining_size -= 1
        if self.remaining_size <= 0:
            self.state = self.sync



c = Channel()

p = Parser(c)

c.notify(42)
c.notify(3)
c.notify(33)
c.notify(44)
c.notify(24)
c.notify(42)
c.notify(1)
c.notify(1)
c.notify(1)