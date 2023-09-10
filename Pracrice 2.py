from warior import Warior
from paladin import Paladin
from assassin import Assassin
from sample import Sample

from population import Population


print("Сегодня с помощью основ ооп мы создадим 2 рандомные армии и завяжем между ними бой")



#------------------------------------------------------------------------------------------

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


duel2()

        