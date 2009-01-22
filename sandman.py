
import stackless
import actor
import time


class Sandman(actor.Actor):

    def __init__(self,sleep=0.001):
        actor.Actor.__init__(self)
        self.sleep = sleep

    def run(self):
        """Slow down a bit, rest for a while"""
        while 1:
            time.sleep(self.sleep)
            stackless.schedule()


