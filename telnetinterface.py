#!/usr/local/bin/python

import socket
import stackless
import sandman
import errno
import interface

class Server():

    def __init__(self):
        self.socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.socket.bind ( ( 'localhost', 8080 ) )
        self.socket.listen ( 1 )
        self.socket.setblocking(0)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.task = stackless.tasklet(self.run)()

    def run(self):
        while True:
            try:
                channel, details = self.socket.accept()
                print 'We have opened a connection with', details
                TelnetInterface(channel)
            except socket.error, error:
                if error[0] != 35:
                    print error
                stackless.schedule()
                
    def close(self):
        self.socket.close()

class TelnetInterface(interface.Interface):

    def __init__(self,channel):
        interface.Interface.__init__(self,None)
        self.channel = channel
        self.channel.setblocking(0)
        self.line = ""
    
    def getCommandLine(self):
        while 1:
            stackless.schedule()
            commandline, newline, self.line = self.line.partition('\n')
            if newline:
                return commandline
            else:
                self.line = commandline
                self.line += self.readSocket()

    def readSocket(self):
        while 1:
            try:
                return self.channel.recv ( 128 )
            except socket.error, error:
                if error[0] == errno.ECONNRESET:
                    self.channel.close()
                    self.open = False
                    break
                if error[0] == errno.EPIPE:
                    self.channel.close()
                    self.open = False
                    break
                if error[0] != 35:
                    print "Error:", error
            stackless.schedule()

    def write(self,text):
        try:
            self.channel.send(text)
        except socket.error, error:
            if error[0] != 35:
                print error
    
    def display(self,text):
        self.write("\n")
        self.write(text)
        self.write("\n")

    def exit(self):
        self.write("Goodbye\n")
        self.channel.close()
        self.open = False

TelnetInterface.commands = {
             '?'         : interface.Interface.help,
             'help'      : interface.Interface.help,
             'color'     : interface.Interface.color,
             'nocolor'   : interface.Interface.nocolor, 
             'exit'      : TelnetInterface.exit, 
             'quit'      : TelnetInterface.exit, }

