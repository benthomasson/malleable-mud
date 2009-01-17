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

def help(obj):
    print "Commands: "
    for x in sorted(obj.commands.keys()):
        print x

def save(obj):
   file = open("state", 'w')
   cPickle.dump(obj,file)
   file.close()

def color(self):
    self.clear = "\x1B[0m"
    self.bold = "\x1B[1m"
    self.italics = "\x1B[3m"
    self.underline = "\x1B[4m"
    self.inverse = "\x1B[7m"
    self.black = "\x1B[30m"
    self.red = "\x1B[31m"
    self.green = "\x1B[32m"
    self.yellow = "\x1B[33m"
    self.blue = "\x1B[34m"
    self.magenta = "\x1B[35m"
    self.cyan = "\x1B[36m"
    self.white = "\x1B[37m"
    self.black_background = "\x1B[40m"
    self.red_background = "\x1B[41m"
    self.green_background = "\x1B[42m"
    self.yellow_background = "\x1B[43m"
    self.blue_background = "\x1B[44m"
    self.magenta_background = "\x1B[45m"
    self.cyan_background = "\x1B[46m"
    self.white_background = "\x1B[47m"

def nocolor(self):
    self.clear = ""
    self.bold = ""
    self.italics = ""
    self.underline = ""
    self.inverse = ""
    self.black = ""
    self.red = ""
    self.green = ""
    self.yellow = ""
    self.blue = ""
    self.magenta = ""
    self.cyan = ""
    self.white = ""
    self.black_background = ""
    self.red_background = ""
    self.green_background = ""
    self.yellow_background = ""
    self.blue_background = ""
    self.magenta_background = ""
    self.cyan_background = ""
    self.white_background = ""
