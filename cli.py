#!/usr/bin/python

import sys
import os

def enableRaw():
    os.spawnlp(os.P_WAIT,'/bin/stty','/bin/stty','raw','-echo')

def disableRaw():
    os.spawnlp(os.P_WAIT,'/bin/stty','/bin/stty','-raw','echo')

enableRaw()

command = []

print '>',
while 1:
    char = sys.stdin.read(1)
    if ord(char) == 13 or ord(char) == 10:
        break
    sys.stdout.write(char)
    command.append(char)

disableRaw()

print "\nCommand: "

print "".join(command)


