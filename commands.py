"""commands module contains all user commands"""

def say(obj,*args):
    print "%sYou say:" % obj.cyan,
    for x in args:
            print obj.lookup(x,notFound=x),
    print obj.clear

def note(obj,name, value):
    obj.memory[name] = value
    print "%sYou remember that %s is %s%s" % (obj.red, name, value, obj.clear)

def notes(obj):
    print "%sYou remember:" % obj.cyan
    for x in memory.keys():
        print "%s as %s" % ( x, memory[x])
    print clear

