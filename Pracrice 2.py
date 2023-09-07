import random
import threading

from warior import Warior
from paladin import Paladin
from assassin import Assassin


print("Сегодня с помощью основ ооп мы создадим 2 рандомные армии и завяжем между ними бой")



#------------------------------------------------------------------------------------------

def duel():
    f_win = 0
    k_win = 0
    for i in range(1, 21):
                
        war1 = Warior("Furiwarius")
        war2 = Assassin("KissasPissas")
    
        war1.targetSelection(war2)
        war2.targetSelection(war1)
    
        war1.attack(war1.target)
        war2.attack(war2.target)
    
        print(f"Начинается бой {i}")
        while war1 and war2:
            pass
    
        if war1.state_live: f_win+=1
        else: k_win+=1
    else:
        print(f"Furiwarius победил {f_win}\nKissasPissas победила {k_win}")

def duel2():              
    war1 = Warior("Furiwarius")
    war2 = Assassin("KissasPissas")
    
    war1.targetSelection(war2)
    war2.targetSelection(war1)
    

    th = threading.Thread(target=war1.attack(war1.target))
    th2 = threading.Thread(target=war2.attack(war2.target))
    
    

    th.start()
    th2.start()    
    
    
    if war1.state_live: print(f"Furiwarius победил\n")
    else: print(f"KissasPissas победил\n")


#duel()
duel2()

        