import unittest
from app.actor import Actor

class ActorTest(unittest.TestCase):

    def setUp(self):
        self.actor = Actor()

    def test_actor(self):
        self.assertTrue(isinstance(self.actor, Actor))

    def test_receive(self):
        receive = getattr(self.actor, 'receive')
        self.assertTrue(callable(receive))

    def test_run(self):
        self.actor.inbox.put(1)
        self.assertRaises(NotImplementedError, lambda:self.actor._run())
