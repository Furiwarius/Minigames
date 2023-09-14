from warior import Warior
from paladin import Paladin
from assassin import Assassin
from shooter import Shooter
from mage import Mage
from sample import Sample

import bext
import generators as gen

from world import World
from population import Population


print("Сегодня с помощью основ ооп мы создадим 2 рандомные армии и завяжем между ними бой")


def duel2(): 

    war1 = Warior("Furiwarius")
    war2 = Assassin("KissasPissas")

    group_1  = Population("Group 1")
    group_1.addPerson(war1)

    group_2 = Population("Group 2")
    group_2.addPerson(war2)


    war1.enemyGroupTarget(group_2.getPopulation())
    war2.enemyGroupTarget(group_1.getPopulation())
        
    war1.start()
    war2.start() 
    while True:
        if war1.state_live and war2.state_live==False: 
            print(f"Furiwarius победил\n")
            break
        elif war2.state_live and war1.state_live==False: 
            print(f"KissasPissas победил\n")
            break


def duel3():
    new_world = World("my_World")
    for _ in range(2):
        new_world.addPopulation(gen.populationGenerator(3))

    return new_world
        
new_world = duel3()
new_world.war()

