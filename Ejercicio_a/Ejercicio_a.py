class NewYork:
    def __init__(self, EdificioA, EdificioB):
        self.EdificioA = EdificioA
        self.EdificioB = EdificioB

class LosAngeles:
    def __init__(self, EdificioC):
        self.EdificioC = EdificioC

class YooHoo:
    def __init__(self, Martin, Salim, Xing):
        self.Martin = Martin
        self.Salim = Salim
        self.Xing = Xing

class NewYork:
    def __del__(self):
        print("NewYork is destroyed")
