from warior import Warior
from paladin import Paladin
from assassin import Assassin
from shooter import Shooter
from mage import Mage
from population import Population
from random import randrange

# функции для генерации персонажей, популяций

consonants = "qwrtpsdfghjklzxcvbnm"

vowels = "eyuioa"

classList = (Warior, Paladin, Assassin, Shooter, Mage)

def nameGenerator():
    # генерация имени случайной длины
    name = ""
    name_length = randrange(5, 10)
    for i in range(name_length):
        if i==0 or i%2==0:
            name+=consonants[randrange(len(consonants))]
        else:
            name+=vowels[randrange(len(vowels))]
    return name


def randomCharacter():
    # генерация персонажа случайного класса
    character = classList[randrange(len(classList))]
    result_char = character(nameGenerator())
    return result_char


def populationGenerator(count=0):
    # генерация группы с заданным количеством персонажей внутри
    population_name = nameGenerator()+"Group"
    new_population = Population(population_name)

    if count!=0:
        for _ in range(count):
            new_population.addPerson(randomCharacter())
    return new_population