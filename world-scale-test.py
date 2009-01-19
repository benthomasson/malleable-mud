#!/usr/bin/python

import world
import model
import time
import os

try:
    os.remove('test-world.db')
except Exception, error:
    print error

start = time.time()

testworld = world.World('test-world')

load = time.time()
print "Load: ", load - start

for i in range(100000):
    testworld.storeObject(model.Character('X' + repr(i)));

store = time.time()
print "Store: ", store - load

testworld.close()

end = time.time()
print "Close: ", end - store


testworld = world.World('test-world')

reload = time.time()
print "Reload: ", reload - end

for i in range(100000):
    try:
        testworld.getObject(repr(i))
    except Exception, error:
        print error

store = time.time()
print "Get: ", store - load

testworld.close()

end = time.time()
print "Close: ", end - store

