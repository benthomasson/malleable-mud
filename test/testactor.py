#!/usr/local/bin/python

import unittest
import stackless
import game.server
import game.model
import game.actor
import game.messages
import time

class TestActor(unittest.TestCase):

    def testProcessMessage(self):
        actor = game.actor.TestableActor()
        self.assertEquals(actor.messages,[])
        actor.processMessage(game.messages.update)
        self.assertEquals(actor.messages,[game.messages.update])

    def testRun(self):
        actor = game.actor.TestableActor()
        self.assertEquals(actor.steps,0)
        actor.channel.send(game.messages.update)
        self.assertEquals(actor.steps,1)
        self.assertEquals(actor.messages,[])
        actor.channel.send(game.messages.die)
        self.assertEquals(actor.steps,2)
        self.assertEquals(actor.messages,[game.messages.die])

    def testWaitForUpdate(self):
        actor = game.actor.TestableActor()
        self.assertEquals(actor.steps,0)
        stackless.tasklet(self.sendUpdate)(actor.channel)
        actor.waitForUpdate()

    def sendUpdate(self,channel):
        time.sleep(1)
        channel.send(game.messages.update)

if __name__ == '__main__':
    unittest.main()



