"""model module.  Contains definitions for the game model"""

import actor
import messages
import pickle

scheduler = None
world = None

class Character(actor.Actor):

    def __init__(self,name='Nobody'):
        global scheduler, world
        actor.Actor.__init__(self)
        self.name = name
        self.mycommands = { }
        if world: world.storeObject(self)
        if scheduler: scheduler.addObject(self.id)

    def __str__(self):
        return self.name

    def __setstate__(self,dict):
        actor.Actor.__setstate__(self,dict)
        if scheduler: scheduler.addObject(self.id)

    def applyCommand(self,command,args):
        apply(command,[ self ] + args)

    def getCommand(self,name):
        if self.commands.has_key(name):
            return self.commands[name]
        if self.mycommands.has_key(name):
            return self.mycommands[name]
        return None

    def getCommands(self):
        return self.commands.items() + self.mycommands.items()

    def say(self,*args):
        """Speak"""
        print "You say: '",
        for x in args:
            print x,
        print ".'"

    def customize(self,name,value):
        """Customize an object"""
        self.__dict__[name] = value

    def dump(self):
        print self.__dict__
        print pickle.dumps(self)

    def update(self,message):
        """Handle an update message"""
        #print(self.id)
        pass

Character.commands = {  'say' : Character.say,
                        'customize' : Character.customize, 
                        'dump' : Character.dump, }

Character.messageHandler = { 'UPDATE' : Character.update, }

class Item():
    pass

class Room():
    pass

class Player():
    pass


