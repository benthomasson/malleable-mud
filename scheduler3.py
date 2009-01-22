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

    messageHandler = { }
    
    def __init__(self,id):
        Actor.__init__(self,id)
        world.addObject(self)

    def update(self,message):
        print "Update %s"  % self.id

    def die(self,message):
        print "%d died" % self.id
        self.id = None
        self.channel = None
        self.task.kill()

Object.messageHandler = { "UPDATE" : Object.update, "DIE" : Object.die }

class World():
    
    def __init__(self):
        self.world = {} 

    def addObject(self,object):
        self.world[object.id] = object

    def getObject(self,id):
        if self.world.has_key(id):
            return self.world[id]
        else:
            return None

    def hasObject(self,id):
        return self.world.has_key(id)

    def sendMessage(self,id,message):
        if self.world.has_key(id) and self.world[id].channel:
                self.world[id].channel.send(message)

class Scheduler(Actor):

    def __init__(self,objects=[]):
        Actor.__init__(self,0)
        self.objects = objects[:]
        self.update = Update()
        self.die = Die()

    def addObject(self,id):
        self.objects.append(id)

    def run(self):
        while 1:
            random.shuffle(self.objects)
            for id in self.objects:
                world.sendMessage(id,self.update)
            if len(self.objects) == 0: break
            world.sendMessage(self.objects[-1],self.die)
            del self.objects[-1]

world = World()
Object(1)
Object(2)
Object(3)
Object(4)
Object(5)
Object(6)
            
s = Scheduler([1,2,3,4,5,6])

stackless.run()

