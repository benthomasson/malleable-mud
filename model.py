"""model module.  Contains definitions for the game model"""

def say(*args):
    print "You say: '",
    for x in args:
        print x,
    print ".'"

class Character():

    commands = {}

    def __init__(self,name='Nobody'):
        self.name = name
        self.commands = { 'say' : say}

class Item():
    pass

class Room():
    pass

class Player():
    pass


