#!/usr/bin/python

import shelve

class World():

    def __init__(self):
        self.world = shelve.open("world")
        if not self.world.has_key('nextId'):
            self.world['nextId'] = 1

    def getNextId(self):
        self.world['nextId'] = self.world['nextId'] + 1
        return self.world['nextId']

    def storeObject(self,object):
        object.id = repr(self.getNextId())
        self.world[object.id] = object

    def removeObject(self,object):
        del self.world[object.id]

    def getObject(self,id):
        if not self.world.has_key(id):
            return None
        else:
            return self.world[id]

    def close(self):
        self.world.close()

world = World()

