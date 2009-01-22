#!/usr/local/bin/python

import interface
import model
import world
import cli
import model
import scheduler
import stackless
import sandman

w = world.World()       
i = interface.Interface(w)
sandman = sandman.Sandman(0.001)

scheduler.world = w
s = scheduler.Scheduler()

def reloadCode():
    """Reload the code"""
    reload(cli)
    reload(model)
    reload(world)
    reload(interface)
    print "Reload complete"

i.commands['reload'] = reloadCode

stackless.run()


