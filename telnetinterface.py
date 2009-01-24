#!/usr/local/bin/python

import socket
import stackless
import sandman
import errno

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

class TelnetInterface():

    def __init__(self,channel):
        self.channel = channel
        self.channel.setblocking(0)
        self.task = stackless.tasklet(self.run)()
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
        while True:
            try:
                return self.channel.recv ( 128 )
            except socket.error, error:
                if error[0] == errno.ECONNRESET:
                    self.channel.close()
                    break
                if error[0] == errno.EPIPE:
                    self.channel.close()
                    break
                if error[0] != 35:
                    print error
            stackless.schedule()
    
    def run(self):
        while True:
            print ":", self.getCommandLine()


s = Server()
sleep = sandman.Sandman(0.001)

try:
    stackless.run()
except KeyboardInterrupt, e:
    print "KeyboardInterrupt", e
    s.close()



