from abc import ABCMeta, abstractmethod

class GetDamage(metaclass=ABCMeta): 

    @abstractmethod 
    def getDamage(self, value:int):
       pass