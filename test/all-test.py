#!/usr/local/bin/python

import unittest
import stackless
import game.test.test
import game.test.testactor
import game.test.testscheduler

modules = [ game.test.test, game.test.testactor, game.test.testscheduler ]

suite = unittest.TestSuite()

for module in modules:
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))

unittest.TextTestRunner(verbosity=2).run(suite)

