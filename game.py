#!/usr/local/bin/python

import interface
import model
import world
import cli
import model

w = world.World()       
i = interface.Interface(w)

def reloadCode():
    """Reload the code"""
    reload(cli)
    reload(model)
    reload(world)
    reload(interface)
    print "Reload complete"

i.commands['reload'] = reloadCode

while True:
    i.prompt()

