
import stackless

class Actor():

    messageHandler = { }

    def __init__(self):
        self.channel = stackless.channel()
        self.task = stackless.tasklet(self.run)()

    def run(self):
        while 1:
            message = self.channel.receive()
            if message.name != "UPDATE":
                self.processMessage(message)

    def processMessage(self,message):
        if self.messageHandler.has_key(message.name):
            apply(self.messageHandler[message.name],[self,message])
        else:
            print "%s: Unknown message: %s" % (repr(self),message)

    def waitForUpdate(self):
        while 1:
            message = self.channel.receive()
            if message.name == "UPDATE":
                break
            else:
                self.processMessage(self,message)

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


class TestableActor(Actor):

    def __init__(self):
        Actor.__init__(self)
        self.messages = []
        self.steps = 0

    def run(self):
        while 1:
            message = self.channel.receive()
            self.steps+=1
            if message.name != "UPDATE":
                self.processMessage(message)

    def processMessage(self,message):
        self.messages.append(message)
        if self.messageHandler.has_key(message.name):
            apply(self.messageHandler[message.name],[self,message])

        

    
