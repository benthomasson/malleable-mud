#!/usr/local/bin/python

import stackless

class Object():
    
    def __init__(self,id):
        self.id = id
        stackless.tasklet(self.run)()

    def run(self):
        while 1:
            print "Running %d" % self.id
            stackless.schedule()

class Scheduler():

    def run(self):
        stackless.run()        

Object(1)
Object(2)
Object(3)
Object(4)
Object(5)
Object(6)

Scheduler().run()

