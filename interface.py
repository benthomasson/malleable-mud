"""interface module"""

import string
import sys
import cPickle
import commands

class Color():

    def __init__(self):
        commands.color(self)

class Interface(Color):

    def __init__(self):
        Color.__init__(self)
        self.memory = { }
        self.commands = { 
                     'say'      : commands.say, 
                     'exit'     : sys.exit,
                     '?'        : commands.help,
                     'help'     : commands.help,
                     'note'     : commands.note,
                     'notes'    : commands.notes,
                     'color'    : commands.color,
                     'nocolor'  : commands.nocolor,
                     'save'     : commands.save }


    def lookup(self,x, notFound=None):
        if self.memory.has_key(x):
            return self.memory[x]
        else:
            return notFound

    def prompt(self):
        print "%s%s>%s" % (self.red, self.underline, self.clear ),
        commandline = raw_input()
        try:
            splitcommand = string.split(commandline)
            if self.commands.has_key(splitcommand[0]):
                apply(self.commands[splitcommand[0]],[ self ] + splitcommand[1:])
            else:
                print "%sWhat?%s" % (self.red,self.clear)
        #except Exception, error:
        #    print "%sWhat?%s" % (self.red,self.clear)
        finally:
            pass


       

