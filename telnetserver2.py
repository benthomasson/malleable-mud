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
        
    def run(self):
        while True:
            try:
                print self.channel.recv ( 128 )
                self.channel.send ( 'Green-eyed monster.' )
            except socket.error, error:
                if error[0] == errno.ECONNRESET:
                    break
                if error[0] == errno.EPIPE:
                    break
                if error[0] != 35:
                    print error
            stackless.schedule()

s = Server()
sleep = sandman.Sandman(1)

try:
    stackless.run()
except KeyboardInterrupt, e:
    print "KeyboardInterrupt", e
    s.close()



