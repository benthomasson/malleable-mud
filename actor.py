
import stackless

class Actor():

    messageHandler = { }

    def __init__(self):
        self.channel = stackless.channel()
        self.task = stackless.tasklet(self.run)()

    def run(self):
        while 1:
            self.processMessage(self.channel.receive())

    def processMessage(self,message):
        if self.messageHandler.has_key(message.name):
            apply(self.messageHandler[message.name],[self,message])
        else:
            print "Unknown message: %s" % message

    def __getstate__(self):
        dict = self.__dict__.copy()
        dict['channel'] = None
        dict['task'] = None
        return dict

    def __setstate__(self,dict):
        self.__dict__ = dict
        self.channel = stackless.channel()
        self.task = stackless.tasklet(self.run)()
        return
