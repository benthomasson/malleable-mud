#!/usr/local/bin/python

import stackless
import messages
import actor

world = None

class Scheduler(actor.Actor):

    def __init__(self,objects=[],interfaces=[]):
        actor.Actor.__init__(self)
        self.objects = objects[:]
        self.interfaces = interfaces[:]
        self.update = messages.Update()

    def addObject(self,id):
        self.objects.append(id)

    def addObject(self,id):
        self.interfaces.append(id)

    def run(self):
        global world
        while 1:
            for id in self.objects:
                world.sendMessage(id,self.update)
            stackless.schedule()
                



