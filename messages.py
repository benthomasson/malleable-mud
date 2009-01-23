
class Message():
    
    def __init__(self,name):
        self.name = name

class Update(Message):

    def __init__(self):
        Message.__init__(self,"UPDATE")

update = Update()

class Die(Message):

    def __init__(self):
        Message.__init__(self,"DIE")

die = Die()


class Speech(Message):
    
    def __init__(self,srcId,srcName,text):
        Message.__init__(self,"SPEECH")
        self.srcId = srcId
        self.srcName = srcName
        self.text = text

