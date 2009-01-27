"""model module.  Contains definitions for the game model"""

import actor
import messages
import pickle

scheduler = None
world = None

class Object(actor.Actor):

    commands = { }
    mycommands = { }
    scripts = { }
    myscripts = { }

    def __init__(self):
        actor.Actor.__init__(self)
        self.updateCommand = None

    def getCommands(self):
        return self.commands.items()

    def getCommand(self,name):
        if self.commands.has_key(name):
            return self.commands[name]
        if self.mycommands.has_key(name):
            return self.mycommands[name]
        return None

    def getScript(self,name):
        if self.scripts.has_key(name):
            return self.scripts[name]
        if self.myscripts.has_key(name):
            return self.myscripts[name]
        return None

    def applyCommand(self,command,args):
        apply(command,[ self ] + args)

    def update(self):
        if self.updateCommand:
            try:
                self.applyCommand(self.updateCommand[0],self.updateCommand[1:])
            finally:
                self.updateCommand = None

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
        Object.__init__(self)
        self.name = name
        self.mycommands = { }
        self.myscripts = { }
        self.nextAction = None
        self.nextActionArgs = []
        self.location = None
        self.interface = None
        if world: world.storeObject(self)
        if scheduler: scheduler.addObject(self.id)

    def __str__(self):
        return self.name

    def getCommands(self):
        return self.commands.items() + self.mycommands.items()

    def say(self,*args):
        """Speak"""
        self.waitForUpdate()
        text = reduce(lambda x,y:x+" "+y, args)
        if self.location: 
            world.sendMessage(self.location,messages.Speech(self.id,self.name,text))

    def customize(self,name,value):
        """Customize an object"""
        self.__dict__[name] = value

    def hear(self,message):
        """Handle a speech message"""
        if self.id == message.srcId:
            self.display( "\nYou say '%s.'" % message.text)
        else:
            self.display( "\n%s says '%s.'" % ( message.srcName , message.text ))

    def display(self,text):
        if self.interface:
            self.interface.display(text)

    def dump(self):
        """Dump debug data to screen"""
        self.display(repr(self.__class__))
        for x in self.__dict__.keys():
            self.display("%10s : %s" % (repr(x), repr(self.__dict__[x])))

Character.commands = {  'say' : Character.say,
                        'customize' : Character.customize, 
                        'dump' : Character.dump, }

Character.messageHandler = { 'SPEECH' : Character.hear, }

class Room(Object):

    def __init__(self):
        Object.__init__(self)
        self.objects = []
        if world: world.storeObject(self)
        if scheduler: scheduler.addObject(self.id)

    def addObject(self,id):
        self.objects.append(id)

    def broadcast(self,message):
        for object in self.objects:
            world.sendMessage(object,message)

#Room.commands = { 'dump' : Object.dump, }

Room.messageHandler = { 'SPEECH' : Room.broadcast, }

