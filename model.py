"""model module.  Contains definitions for the game model"""

def say(self,*args):
    """Speak"""
    print "You say: '",
    for x in args:
        print x,
    print ".'"

talking = { 'say' : say }

class Character():

    commandSets = { 'talking' : talking }
    commands = { } 

    def __init__(self,name='Nobody'):
        self.name = name
        self.commands = { }

    def __str__(self):
        return self.name

    def applyCommand(self,command,args):
        apply(command,[ self ] + args)

    def getCommand(self,name):
        if self.commands.has_key(name):
            return self.commands[name]
        for set in self.commandSets.values():
            if set.has_key(name):
                return set[name]
        return None

    def getCommands(self):
        commands = self.commands.items()
        for (name, set) in self.commandSets.items():
            commands += set.items()
        return commands
        
class Item():
    pass

class Room():
    pass

class Player():
    pass


