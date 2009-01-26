#!/usr/local/bin/python

import unittest
import stackless
import game.server
import game.model

class Test(unittest.TestCase):

    def testServer(self):
        server = game.server.TestServer()
        self.assertTrue(server.world)
        self.assertTrue(server.scheduler)
    
    def testCreate(self):
        server = game.server.TestServer()
        self.assertTrue(server.world)
        self.assertTrue(server.scheduler)
        room = game.model.Room()
        o = game.model.Character()
        room.addObject(o.id)
        o.location = room.id
        self.assertEquals(o.location,room.id)
        self.assertEquals(room.objects,[o.id])

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
    

if __name__ == '__main__':
    unittest.main()

