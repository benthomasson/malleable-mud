
class Message():
    
    def __init__(self,name):
        self.name = name

class Update(Message):

    def __init__(self):
        Message.__init__(self,"UPDATE")

class Die(Message):

    def __init__(self):
        Message.__init__(self,"DIE")


