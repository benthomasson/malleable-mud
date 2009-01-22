#!/usr/local/bin/python

import stackless
import random

class Message():
    
    def __init__(self,name):
        self.name = name

class Update(Message):

    def __init__(self):
        Message.__init__(self,"UPDATE")

class Die(Message):

    def __init__(self):
        Message.__init__(self,"DIE")

class Actor():

    messageHandler = { }

    def __init__(self,id):
        self.id = id
        self.channel = stackless.channel()
        self.task = stackless.tasklet(self.run)()

    def run(self):
        while 1:
            self.processMessage(self.channel.receive())

    def processMessage(self,message):
        if self.messageHandler.has_key(message.name):
            apply(self.messageHandler[message.name],[self,message])
        else:
            print "%s Unknown message: %s" % ( self.id, message )


class Object(Actor):
    
    def __init__(self,id):
        Actor.__init__(self,id)
        self.messageHandler = { "UPDATE" : Object.update, "DIE" : Object.die }

    def update(self,message):
        print "Update %s"  % ( self.id, )

    def die(self,message):
        print "%d died" % self.id
        self.id = None
        self.channel = None
        self.task.kill()

class Scheduler():

    def __init__(self):
        self.objects = {}
        stackless.tasklet(self.sendMessages)()
        self.update = Update()
        self.die = Die()

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
                self.objects[key].channel.send(self.update)
            if len(keys) == 0: break
            self.objects[keys[0]].channel.send(self.die)
            del self.objects[keys[0]]
            
s = Scheduler()

s.addObject(Object(1))
s.addObject(Object(2))
s.addObject(Object(3))
s.addObject(Object(4))
s.addObject(Object(5))
s.addObject(Object(6))

s.run()

