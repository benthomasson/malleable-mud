#!/usr/local/bin/python

import stackless
import messages
import actor
import time

world = None

class Scheduler(actor.Actor):

    def __init__(self,roundTime=1):
        actor.Actor.__init__(self)
        self.objects = []
        self.roundTime = roundTime
        self.update = messages.Update()
        self.open = True

    def addObject(self,id):
        self.objects.append(id)

    def close(self):
        self.open = False

    def run(self):
        global world
        lastTime = time.time()
        while self.open:
            if time.time() - lastTime > self.roundTime:
                lastTime = time.time()
                for id in self.objects:
                    world.sendMessage(id,self.update)
            stackless.schedule()
                
