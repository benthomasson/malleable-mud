#!/usr/local/bin/python

import stackless
import random

class Object():
    
    def __init__(self,id):
        self.id = id
        self.task = stackless.tasklet(self.run)()
        self.channel = stackless.channel()

    def run(self):
        while self.channel.receive():
            print "Running %d" % self.id

    def die(self):
        print "%d died" % self.id
        self.id = None
        self.channel = None
        self.task.kill()

class Scheduler():

    def __init__(self):
        self.objects = {}
        stackless.tasklet(self.sendMessages)()

    def run(self):
        stackless.run()        

    def addObject(self,object):
        self.objects[object.id] = object

    def removeObject(self,id=None,object=None):
        if id:
            object = self.objects[id]
        else:
            id = object.id
        object.die()
        del self.objects[id]

    def sendMessages(self):
        while 1:
            keys = self.objects.keys()
            random.shuffle(keys)
            for key in keys:
                self.objects[key].channel.send('Run')

s = Scheduler()

s.addObject(Object(1))
s.addObject(Object(2))
s.addObject(Object(3))
s.addObject(Object(4))
s.addObject(Object(5))
s.addObject(Object(6))

s.run()

