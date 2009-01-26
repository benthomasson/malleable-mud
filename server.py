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
        world = game.world.World()       
        telnetServer = game.telnetinterface.Server(world)
        localInterface = game.interface.LocalInterface(world)
        game.sandman.Sandman(0.001)

        scheduler = game.scheduler.Scheduler(0.1,world)

        game.model.world = world
        game.model.scheduler = scheduler

        if world.hasObject('2'):
            room = world.getObject('2')
        else:
            room = game.model.Room()

        localInterface.room = room

        def reloadCode(self):
            """Reload the code"""
            reload(game.cli)
            reload(game.model)
            reload(game.world)
            reload(game.interface)
            reload(game.actor)
            reload(sandman)
            print "Reload complete"

        localInterface.commands['reload'] = reloadCode

        world.load()

        try:
            stackless.run()
        except game.exceptions.GameExit, ge:
            pass
        finally:
            telnetServer.close()

class TestServer(Server):

    def __init__(self):
        self.world = game.world.TestWorld()       
        self.scheduler = game.scheduler.Scheduler(0,self.world)
        game.model.world = self.world
        game.model.scheduler = self.scheduler
        

if __name__ == '__main__':
    Server()


