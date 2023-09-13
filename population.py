# описание группы персонажей
# все объекты входящие в популяцию являются союзниками, а другие популяции врагами

from sample import Sample

class Population():

    def __init__(self, name="newPopulatoin"):

        self.name_population=name
        self.general_population = []
        self.enemy_list = []

    
    def __str__(self) -> str:
        return self.name_population


    def __bool__ (self):
        if len(self.general_population)>0: return True
        else: return False


    def addPerson(self, person:Sample):
        if self.general_population.count(person)==0:
            self.general_population.append(person)
            person.population=self


    def getPopulation(self):
        return self.general_population
    
    
    def examBelonging (self, person:Sample):
        # Проверка на принадлежность к данной группе

        if person in self.general_population: return True
        return False


    def getEnemy(self):
        return self.enemy_list
    
    
    def addEnemy(self, enemys:list):
        if enemys!=self.general_population and enemys not in self.general_population:
            
            for elem in enemys:
                self.enemy_list.append(elem)
            self.targetSetting()
            
    
    def targetSetting (self):
        for char in self.general_population:
            char.enemyGroupTarget(self.enemy_list)
