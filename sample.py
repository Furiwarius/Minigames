from random import randrange
from time import time
import threading
from getDamage import GetDamage
from giveDamage import GiveDamage


class Sample(threading.Thread, GetDamage, GiveDamage):

    def __init__(self, name = "unknown"):
        super().__init__()
        self.hp = 100
        self.armor = 6 # 1 == 2.5 %
        #self.lvl = 1
        self.damage = 15
        self.burst_damage = 1

        self.speed = 40          # на 10 speed 0,23 сек
        self.attack_current = 1.5  # 3 - максимальный кд на атаку

        self.lack = 10 # 10 %
        self.crete = 0.5

        self.state_live = True # 1-жив, 0-мертв
        self.state_move = 0 # 1-ходит, 0-не ходит

        self.target = None
        self.name = name

        self.group_enemy = None


    def __bool__ (self):
        return self.state_live
    
    
    def info(self, damage_caused=0):
        print(f"Здоровье {self.name} {self.hp}")
        if damage_caused!=0:
            print(f"Нанесенный урон {damage_caused}")


    def getDamage(self, value:int):
        result_damage = value - (value/100)*2.5*self.armor
        if result_damage<0: result_damage=0  
        self.hp = (self.hp-result_damage)//1
        if self.hp <= 0: self.state_live = False


    def giveDamage(self):
        result_damage = self.damage*self.burst_damage    
        if self.lack >= randrange(1, 100):
            result_damage += result_damage*self.crete
        return result_damage


    def enemyTarget (self):
        for enemy in self.group_enemy:
                if enemy: 
                    self.target = enemy
                    return
                #------------------------------------
                # ДОРАБОТАТЬ С УЧЕТОМ ПЕРЕДВИЖЕНИЯ
                #------------------------------------
        self.target = None
        
    
    def enemyGroupTarget(self, group_enemy:list):
        if self.group_enemy==None and self not in group_enemy:
            self.group_enemy = group_enemy
        self.enemyTarget()
        

    def attack (self):
        attack_speed = self.attack_current-self.speed/10*0.23
        time_start = time()
        while self.target.state_live and self.state_live:
            time_end = time()
            if time_end-time_start>=attack_speed:
                time_start = time()
                self.target.getDamage(self.giveDamage())
        else: self.target = None


    def run(self):
        while self.target!=None:
            self.attack()
            if self.state_live:
                self.enemyTarget()
        
        


        

    

