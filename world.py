#!/usr/bin/python

import shelve
import time

class World():

    def __init__(self,db='world'):
        start = time.time()
        self.world = shelve.open(db,writeback=True)
        print "Load: ", time.time() - start
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
        start = time.time()
        self.world.close()
        print "Close: ", time.time() - start

    def sync(self):
        """Sync the world to the on disk db"""
        start = time.time()
        self.world.sync()
        print "Sync: ", time.time() - start

world = World()

