# описание группы персонажей
# все объекты входящие в популяцию являются союзниками, а другие популяции врагами

from sample import Sample

class Population():

    def __init__(self, name="newPopulatoin"):
        self.name_population=name
        
        self.__general_population__ = []
        self.__alive__ = []
        self.__dead__ = []

    
    def __str__(self) -> str:
        return self.name_population


    def __bool__ (self):
        if len(self.__general_population__)>0: return True
        else: return False


    def addPerson(self, person:Sample):
        if self.__general_population__.count(person)==0:
            self.__general_population__.append(person)
            if person: self.__alive__.append(person)
            else: self.__dead__.append(person)


    def setAlive(self, person:Sample):
        # Переносит из мертвых к живым
        
        if person in self.__general_population__ and person in self.__dead__:
            self.__alive__.append(person)
            self.__dead__.remove(person)
            

    def setDead(self, person: Sample):
        # переносит из живых к мертвым

        if person in self.__general_population__ and person in self.__alive__:
            self.__dead__.append(person)
            self.__alive__.remove(person)


    def getPopulation(self):
        return self.__general_population__
    

    def getAlive(self):
        return self.__alive__
    

    def getDead(self):
        return self.__dead__
    

    def examBelonging (self, person:Sample):
        # Проверка на принадлежность к данной группе

        if person in self.__general_population__: return True
        return False
    

    def examAlive (self, person:Sample):
        # Проверка на принадлежность к живым данной группы

        if person in self.__alive__: return True  
        return False
    

    def examDead (self, person:Sample):
        # Проверка на принадлежность к мертвым данной группы

        if person in self.__dead__: return True
        return False
    

    def delitePerson(self, person:Sample):
        # Удаление персонажа

        if person in self.__general_population__:
            self.__general_population__.remove(person)
            if person: self.__alive__.remove(person)
            else: self.__dead__.remove(person)
