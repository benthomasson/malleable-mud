#!/usr/bin/python

import string
import sys

print "\x1B[31mHello World!\x1B[0m"

clear = "\x1B[0m"
bold = "\x1B[1m"
italics = "\x1B[3m"
underline = "\x1B[4m"
inverse = "\x1B[7m"
black = "\x1B[30m"
red = "\x1B[31m"
green = "\x1B[32m"
yellow = "\x1B[33m"
blue = "\x1B[34m"
magenta = "\x1B[35m"
cyan = "\x1B[36m"
white = "\x1B[37m"
black_background = "\x1B[40m"
red_background = "\x1B[41m"
green_background = "\x1B[42m"
yellow_background = "\x1B[43m"
blue_background = "\x1B[44m"
magenta_background = "\x1B[45m"
cyan_background = "\x1B[46m"
white_background = "\x1B[47m"

def say(*args):
    print "%sYou say:" % cyan,
    for x in args:
        if memory.has_key(x):
            print memory[x]
        else:
            print x,
    print clear

def note(name, value):
    memory[name] = value
    print "%sYou remember that %s is %s%s" % (red, name, value, clear)

def notes():
    print "%sYou remember:" % cyan
    for x in memory.keys():
        print "%s as %s" % ( x, memory[x])
    print clear

commands = { 'say': say, 
             'exit': sys.exit,
             'note': note,
             'notes':  notes }
memory = { }

def nocolor():
    global clear, bold, italics, underline, inverse, black, red, green, yellow, blue, magenta, cyan, white, black_background, red_background, green_background, yellow_background, blue_background, magenta_background, cyan_background, white_background
    clear = ""
    bold = ""
    italics = ""
    underline = ""
    inverse = ""
    black = ""
    red = ""
    green = ""
    yellow = ""
    blue = ""
    magenta = ""
    cyan = ""
    white = ""
    black_background = ""
    red_background = ""
    green_background = ""
    yellow_background = ""
    blue_background = ""
    magenta_background = ""
    cyan_background = ""
    white_background = ""

def prompt():
    print "%s%s>%s" % (red, underline, clear ),
    commandline = raw_input()
    splitcommand = string.split(commandline," ")
    if commands.has_key(splitcommand[0]):
        apply(commands[splitcommand[0]],splitcommand[1:])
    else:
        print "%sWhat?%s" % (red,clear)
    
while 1:
    prompt()



