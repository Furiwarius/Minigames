# Для прописаня мира, то есть для 2 состояний - мир и война

from population import Population

class World():

    def __init__ (self, name_world = "newWorld"):
        self.name = name_world
        self.__populations__ = []


    def __str__ (self) -> str:
        return self.name
    

    def addPopulation (self, group:Population):
        if self.__populations__.count(group)==0:
            self.__populations__.append(group)
        if len(self.__populations__)>1:
            for popul in self.__populations__:
                group.addEnemy(popul.getPopulation())
                popul.addEnemy(group.getPopulation())


    def getPopulations (self):
        return self.__populations__


    def size(self):
        return len(self.__populations__)


    def war(self):
        pass


