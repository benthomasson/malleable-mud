#!/usr/local/bin/python

import unittest
import stackless
import game.server
import game.model
import game.actor

class Test(unittest.TestCase):

    def testScheduler(self):
        server = game.server.TestServer()
        self.assertTrue(server.world)
        self.assertTrue(server.scheduler)
        self.assertEquals(server.scheduler.steps,0)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,1)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,2)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,3)
        server.scheduler.close()

    def testAddObject(self):
        server = game.server.TestServer()
        self.assertTrue(server.world)
        self.assertTrue(server.scheduler)
        o = TestObject()
        self.assertEquals(o.steps, 0)
        server.world.storeObject(o)
        self.assertTrue(o.id)
        server.scheduler.addObject(o.id)
        self.assertEquals(server.scheduler.steps,0)
        self.assertEquals(o.steps, 0)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,1)
        self.assertEquals(o.steps, 1)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,1)
        self.assertEquals(o.steps, 1)
        stackless.schedule()
        self.assertEquals(server.scheduler.steps,2)
        self.assertEquals(o.steps, 2)

class TestObject(game.model.Object,game.actor.TestableActor):

    def __init__(self):
        game.actor.TestableActor.__init__(self)

    def run(self):
        game.actor.TestableActor.run(self)


if __name__ == '__main__':
    unittest.main()



