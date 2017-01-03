from gevent.queue import Queue
from gevent import Greenlet

class Actor(Greenlet):
    def __init__(self):
        self.inbox = Queue()
        Greenlet.__init__(self)

    def receive(self, message):
        raise NotImplementedError()

    def _run(self):
        self.running = True
        while self.running:
            message = self.inbox.get()
            self.receive(message)
