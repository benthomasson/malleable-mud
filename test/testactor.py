#!/usr/local/bin/python

import unittest
import stackless
import game.server
import game.model
import game.actor
import game.messages

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


if __name__ == '__main__':
    unittest.main()



