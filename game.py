#!/usr/local/bin/python

import interface
import model
import world
import cli
import model
import scheduler
import stackless
import sandman
import actor
import telnetinterface

telnetServer = telnetinterface.Server()

w = world.World()       
i = interface.LocalInterface(w)
sandman.Sandman(0.001)

scheduler.world = w
s = scheduler.Scheduler(0.1)

model.world = w
model.scheduler = s

if w.hasObject('2'):
    r = w.getObject('2')
else:
    r = model.Room()

i.room = r

def reloadCode(self):
    """Reload the code"""
    reload(cli)
    reload(model)
    reload(world)
    reload(interface)
    reload(actor)
    reload(sandman)
    print "Reload complete"

i.commands['reload'] = reloadCode

w.load()

try:
    stackless.run()
finally:
    telnetServer.close()


