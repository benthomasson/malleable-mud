#!/usr/local/bin/python

import stackless
import messages
import actor
import time

class Scheduler(actor.Actor):

    def __init__(self,roundTime,world):
        actor.Actor.__init__(self)
        self.objects = []
        self.roundTime = roundTime
        self.update = messages.Update()
        self.open = True
        self.world = world
        self.steps = 0

    def addObject(self,id):
        self.objects.append(id)

    def close(self):
        self.open = False
        self.task.kill()

    def run(self):
        lastTime = time.time()
        while self.open:
            if time.time() - lastTime > self.roundTime or not self.roundTime:
                lastTime = time.time()
                self.steps+=1
                for id in self.objects:
                    self.world.sendMessage(id,self.update)
            stackless.schedule()
                
