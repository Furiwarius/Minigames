# Для прописаня мира, то есть для 2 состояний - мир и война

from population import Population

class World():

    def __init__ (self, name_world = "newWorld"):
        self.name = name_world
        self.populations = []


    def __str__ (self) -> str:
        return self.name
    

    def addPopulation (self, group:Population):
        if group not in self.populations:
            self.populations.append(group)
            group.setWorld(self)

    def synchronization(self):
        for group in self.populations:
            group.setWorld()



    def getPopulations (self):
        return self.populations


    def size(self):
        return len(self.populations)


    def war(self):
        for population in self.populations:
            population.start()


