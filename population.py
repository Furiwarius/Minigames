# описание группы персонажей
# все объекты входящие в популяцию являются союзниками, а другие популяции врагами

from sample import Sample

class Population():

    def __init__(self, name="newPopulatoin"):

        self.name_population=name
        self.general_population = []
        self.enemy_list = []

        self.my_world = None

    
    def __str__(self) -> str:
        return self.name_population


    def __bool__ (self):
        if len(self.general_population)>0: return True
        else: return False


    def addPerson(self, person:Sample):
        if person not in self.general_population:
            self.general_population.append(person)


    def setWorld(self, world):
        self.my_world = world
        self.searchEnemy()
        


    def getPopulation(self):
        return self.general_population
    
    
    def examBelonging (self, person:Sample):
        # Проверка на принадлежность к данной группе

        if person in self.general_population: return True
        return False


    def getEnemy(self):
        return self.enemy_list
    
    
    def searchEnemy(self):
        groups = self.my_world.getPopulations()
        for group in groups:
            if group != self:
                self.addEnemy(group.getPopulation())


    def addEnemy(self, enemys:list):          
            for elem in enemys:
                if elem not in self.enemy_list:
                    self.enemy_list.append(elem)            
    

    def targetSetting (self):
        for char in self.general_population:
            char.enemyGroupTarget()

