"""model module.  Contains definitions for the game model"""

import actor
import messages
import pickle

scheduler = None
world = None

class Object(actor.Actor):

    commands = { }

    def dump(self):
        """Dump debug data to screen"""
        print self.__class__
        for x in self.__dict__.keys():
            print "%10s : %s" % (repr(x), repr(self.__dict__[x]))
        #print self.__dict__
        #print pickle.dumps(self)

    def update(self,message):
        pass

    def getCommands(self):
        return self.commands.items()

    def getCommand(self,name):
        if self.commands.has_key(name):
            return self.commands[name]
        if self.mycommands.has_key(name):
            return self.mycommands[name]
        return None

    def applyCommand(self,command,args):
        apply(command,[ self ] + args)

    def __getstate__(self):
        dict = actor.Actor.__getstate__(self)
        dict['interface'] = None
        return dict

    def __setstate__(self,dict):
        actor.Actor.__setstate__(self,dict)
        if scheduler: scheduler.addObject(self.id)

class Character(Object):

    def __init__(self,name='Nobody'):
        global scheduler, world
        actor.Actor.__init__(self)
        self.name = name
        self.mycommands = { }
        self.nextAction = None
        self.nextActionArgs = []
        self.location = None
        if world: world.storeObject(self)
        if scheduler: scheduler.addObject(self.id)

    def __str__(self):
        return self.name

    def getCommands(self):
        return self.commands.items() + self.mycommands.items()

    def say(self,*args):
        """Speak"""
        self.nextAction = Character.doSay
        self.nextActionArgs = [ reduce(lambda x,y:x+" "+y, args) ]

    def doSay(self,text):
        if self.location: 
            world.sendMessage(self.location,messages.Speech(self.id,self.name,text))

    def customize(self,name,value):
        """Customize an object"""
        self.__dict__[name] = value

    def update(self,message):
        """Handle an update message"""
        if self.nextAction: 
            apply(self.nextAction,[ self ] + self.nextActionArgs)
            self.nextAction = None
            self.nextActionArgs = []

    def hear(self,message):
        """Handle a speech message"""
        if self.id == message.srcId:
            self.display( "\nYou say '%s.'" % message.text)
        else:
            self.display( "\n%s says '%s.'" % ( message.srcName , message.text ))

    def display(self,text):
        if self.interface:
            self.interface.display(text)

Character.commands = {  'say' : Character.say,
                        'customize' : Character.customize, 
                        'dump' : Character.dump, }

Character.messageHandler = { 'UPDATE' : Character.update,
                             'SPEECH' : Character.hear, }

class Room(Object):

    def __init__(self):
        actor.Actor.__init__(self)
        self.objects = []
        if world: world.storeObject(self)
        if scheduler: scheduler.addObject(self.id)

    def addObject(self,id):
        self.objects.append(id)

    def broadcast(self,message):
        for object in self.objects:
            world.sendMessage(object,message)

Room.commands = { 'dump' : Object.dump, }

Room.messageHandler = { 'UPDATE' : Room.update, 
                        'SPEECH' : Room.broadcast, }

