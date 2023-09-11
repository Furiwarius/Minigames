
from warior import Warior
from assassin import Assassin
from paladin import Paladin
import threading
from time import time


class SaveInfo (threading.Thread):
        
    def __init__(self, character):
        super().__init__()
        self.character = character
        if type(character)==Warior:
            self.infoWarior(self.character)
        elif type(character)==Paladin:
            self.infoPaladin(self.character)
        elif type(character)==Assassin:
            self.infoAssassin(self.character)

    
    def infoWarior(self, characher:Warior):
        self.hp = characher.hp
        self.fury = characher.fury
        self


    def infoPaladin(self, characher:Paladin):
        pass


    def infoAssassin(self, characher:Assassin):
        pass


    #def statusRecord(self):
    #    with open("hello.txt",self "w") as somefile:
    #        somefile.write("hello world")

