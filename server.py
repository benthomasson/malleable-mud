#!/usr/local/bin/python

import stackless
import game.interface
import game.model
import game.world
import game.cli
import game.scheduler
import game.sandman
import game.actor
import game.telnetinterface
import game.exceptions

class Server():

    def __init__(self):
        w = game.world.World()       
        telnetServer = game.telnetinterface.Server(w)
        i = game.interface.LocalInterface(w)
        game.sandman.Sandman(0.001)

        game.scheduler.world = w
        s = game.scheduler.Scheduler(0.1)

        game.model.world = w
        game.model.scheduler = s

        if w.hasObject('2'):
            r = w.getObject('2')
        else:
            r = game.model.Room()

        i.room = r

        def reloadCode(self):
            """Reload the code"""
            reload(game.cli)
            reload(game.model)
            reload(game.world)
            reload(game.interface)
            reload(game.actor)
            reload(sandman)
            print "Reload complete"

        i.commands['reload'] = reloadCode

        w.load()

        try:
            stackless.run()
        except game.exceptions.GameExit, ge:
            pass
        finally:
            telnetServer.close()

if __name__ == '__main__':
    Server()


