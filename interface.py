"""interface module"""

import string
import sys
import cPickle
import commands
import model
import world
import traceback
import cli

class Color():

    def __init__(self):
        self.color()
        self.cli = cli.CommandLineInterface(tabCallBack=self.getCommands)

    def color(self):
        """Enable color"""
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
        """Disable color"""
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

    def __init__(self,world):
        Color.__init__(self)
        self.memory = { }
        self.world = world
        self.commands = { 
                     'exit'      : self.exit,
                     'sync'      : self.world.sync,
                     '?'         : self.help,
                     'help'      : self.help,
                     'color'     : self.color,
                     'nocolor'   : self.nocolor,
                     'objects'   : self.objects,
                     'setobject' : self.setobject, 
                     'create'    : self.create, }
        self.object = None

    def lookup(self,x, notFound=None):
        if self.memory.has_key(x):
            return self.memory[x]
        else:
            return notFound

    def getCommand(self,command):
        if self.commands.has_key(command):
            return self.commands[command]
        else:
            return None

    def applyCommand(self,command,args):
        apply(command,args)

    def prompt(self):
        print "%s%s%s>%s" % (self.red, self.underline, self.object, self.clear ),
        commandline = self.cli.getCommand()
        try:
            splitcommand = string.split(commandline)
            if len(splitcommand) == 0: return
            command = self.getCommand(splitcommand[0])
            if command is not None:
                self.applyCommand(command,splitcommand[1:])
                return
            if self.object is not None: 
                command = self.object.getCommand(splitcommand[0])
                if command is not None:
                    self.object.applyCommand(command,splitcommand[1:])
                    return
            print "%sWhat?%s" % (self.red,self.clear)
        except Exception, error:
            print "%sWhat?%s" % (self.red,self.clear)
            print "Error: ", error
            traceback.print_tb(sys.exc_info()[2])
        finally:
            pass
    
    def getCommands(self,prefix):
        commands = []
        commands += self.commands.items()
        if self.object is not None:
            commands += self.object.getCommands()
        return filter(lambda x: x[0].startswith(prefix),commands)

    def help(self):
        """Print the help for commands"""
        print "Commands: "
        for (name,command) in sorted(self.commands.items()):
            print "%-*s - %s" % (10,name,command.__doc__)
        if self.object is not None:
            for (name,command) in sorted(self.object.getCommands()):
                print "%-*s - %s" % (10,name,command.__doc__)

    def objects(self):
        """Get a list of all the objects"""
        for x in self.world.world.keys():
            print "%s: %s" % (x,self.world.getObject(x))

    def setobject(self,x):
        """Change the object you control"""
        self.object = self.world.getObject(x)

    def create(self,type="Character"):
        """Create a new object"""
        self.world.storeObject(eval("model.%s()" % (type,)))
        print "Done!"

    def exit(self):
        """Exit the game"""
        self.world.close()
        sys.exit()

    def reload(self):
        """Reload the code"""
        reload(cli)
        reload(model)
        print "Reload complete"

