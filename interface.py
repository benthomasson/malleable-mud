"""interface module"""

import string
import sys
import cPickle
import commands
import world

class Color():

    def __init__(self):
        self.color()

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

class Interface(Color):

    def __init__(self):
        Color.__init__(self)
        self.memory = { }
        self.commands = { 
                     'exit'     : sys.exit,
                     '?'        : self.help,
                     'help'     : self.help,
                     'color'    : self.color,
                     'nocolor'  : self.nocolor,
                     'objects'  : self.objects,
                     'setobject' : self.setobject, }
        self.object = None

    def lookup(self,x, notFound=None):
        if self.memory.has_key(x):
            return self.memory[x]
        else:
            return notFound

    def prompt(self):
        print "%s%s%s>%s" % (self.red, self.underline, self.object, self.clear ),
        commandline = raw_input()
        try:
            splitcommand = string.split(commandline)
            if self.commands.has_key(splitcommand[0]):
                apply(self.commands[splitcommand[0]],splitcommand[1:])
            else:
                print "%sWhat?%s" % (self.red,self.clear)
        #except Exception, error:
        #    print "%sWhat?%s" % (self.red,self.clear)
        finally:
            pass

    def help(obj):
        print "Commands: "
        for x in sorted(obj.commands.keys()):
            print x

    def objects(self):
        for x in world.world.world.keys():
            print "%s: %s" % (x,world.world.getObject(x))

    def setobject(self,x):
        self.object = world.world.getObject(x)
           

