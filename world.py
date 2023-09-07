# Для прописаня мира, то есть для 2 состояний - мир и война

from population import Population

class World():

    populations = []

    def addPopulation (self, group:Population):
        if self.populations.count(group)==0:
            self.populations.append(group)

    def war(self):
        pass

