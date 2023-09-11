from abc import ABCMeta, abstractmethod

class GiveDamage(metaclass=ABCMeta): 

    @abstractmethod 
    def giveDamage(self):
       pass
