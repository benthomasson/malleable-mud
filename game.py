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

w = world.World()       
i = interface.Interface(w)
sandman.Sandman(0.001)

scheduler.world = w
s = scheduler.Scheduler()

model.world = w
model.scheduler = s

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

stackless.run()


