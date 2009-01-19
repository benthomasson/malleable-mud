#!/usr/bin/python

import sys
import os

class CommandLineInterface():

    def __init__(self):
        self.history = []
        self.historyIndex = 0
        self.out = sys.stdout
        self.index = 0
        self.line = []

    def enableRaw(self):
        os.spawnlp(os.P_WAIT,'/bin/stty','/bin/stty','raw','-echo')

    def disableRaw(self):
        os.spawnlp(os.P_WAIT,'/bin/stty','/bin/stty','-raw','echo')

    def moveLeft(self):
        if self.index > 0:
            self.index += -1
            self.out.write("\x1B\x5B\x44")

    def moveRight(self):
        if self.index < len(self.line):
            self.index += 1
            self.out.write("\x1B\x5B\x43")

    def appendChar(self,char):
        self.out.write(char)
        self.line.append(char)
        self.index+=1

    def insertChar(self,char):
        self.line.insert(self.index,char)
        self.index+=1
        self.out.write(char)
        for x in range(self.index,len(self.line)):
            self.out.write(self.line[x])
        self.out.write(" \b")
        for x in range(self.index,len(self.line)):
            self.out.write("\b")

    def eraseChar(self):
        self.index+=-1
        self.line.pop(self.index)
        self.out.write("\b \b")
        for x in range(self.index,len(self.line)):
            self.out.write(self.line[x])
        self.out.write(" \b")
        for x in range(self.index,len(self.line)):
            self.out.write("\b")
    
    def eraseLine(self):
        for x in range(self.index,len(self.line)):
            self.out.write(" ")
        for x in range(0,len(self.line)):
            self.out.write("\b \b")
        self.line = []
        self.index = 0

    def moveToStart(self):
        for x in range(0,self.index):
            self.out.write("\b")
        self.index = 0

    def moveToEnd(self):
        for x in range(self.index,len(self.line)):
            self.out.write(self.line[x])
        self.index = len(self.line)
    
    def previousHistoryCommand(self):
        if self.historyIndex > 0:
            self.historyIndex += -1
            self.eraseLine()
            self.line = self.history[self.historyIndex][:]
            self.index = len(self.line) 
            self.out.write("".join(self.line))
    
    def nextHistoryCommand(self):
        if self.historyIndex < len(self.history) - 1:
            self.historyIndex += 1
            self.eraseLine()
            self.line = self.history[self.historyIndex][:]
            self.index = len(self.line) 
            self.out.write("".join(self.line))

    def getCommand(self):
        done = False
        self.enableRaw()
        self.line = []
        while not done:
            char = sys.stdin.read(1)
            num = ord(char)
            #print num
            if num == 27: #Escape Character
                control = ord(sys.stdin.read(1))
                command = ord(sys.stdin.read(1))
                if command == 68:  #Left arrow
                    self.moveLeft()
                elif command == 67: #Right arrow
                    self.moveRight()
                elif command == 66: #Down arrow
                    self.nextHistoryCommand()
                elif command == 65: #Down arrow
                    self.previousHistoryCommand()
                else:
                    self.out.write(num)
            elif num == 1:   #Control-A
                self.moveToStart()
            elif num == 5:   #Control-E
                self.moveToEnd()
            elif num == 3:   #Control-C
                self.eraseLine()
            elif num == 2:
                self.moveLeft()                
            elif num == 6:
                self.moveRight()                
            elif num == 8 or num == 127:
                if self.index > 0:
                    self.eraseChar()
            elif num == 13 or num == 10:
                self.history.append(self.line)
                self.historyIndex = len(self.history)
                done = True
            elif num == 14:
                pass
            elif num == 16:
                self.previousHistoryCommand()
            else:
                if self.index == len(self.line):
                    self.appendChar(char)
                else:
                    self.insertChar(char)

        self.disableRaw()
        self.out.write("\n")
        return "".join(self.line)

cli = CommandLineInterface()

done = False
while not done:
    command = cli.getCommand()
    sys.stdout.write("Command: %s\n" % command)
    if command == "end":
        done = True



