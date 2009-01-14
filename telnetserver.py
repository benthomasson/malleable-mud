#!/usr/bin/python

import socket
mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
mySocket.bind ( ( 'localhost', 8080 ) )
mySocket.listen ( 1 )
try:
    while True:
        channel, details = mySocket.accept()
        print 'We have opened a connection with', details
        try:
            while True:
                print channel.recv ( 100 )
                channel.send ( 'Green-eyed monster.' )
        except socket.error, error:
            channel.close()
        finally:
            channel.close()
finally:
    mySocket.close()

