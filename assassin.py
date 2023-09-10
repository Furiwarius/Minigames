from random import randrange
from time import time

from sample import Sample

class Assassin(Sample):
    
    def __init__(self, name: str):
        super().__init__(name)
        
        self.evasion = 15 # уклонение
        self.beat_counter = 0 # счетчик серии ударов
        self.energy = 0
        self.energy_max = 100        

        self.armor-=3
        self.damage-=2
        self.crete+=0.25
        self.lack+=15 
        self.speed+=15

        self.recharge_deadlyPoison = 4
        self.recharge_deadlyPoison_current = time()
        self.deadlyPoison_flag = False
        self.deadlyPoison_duration = 3
        self.deadlyPoison_duration_current = time()

    
    def info(self, damage_caused=0):
        print("_______________________________________________")
        super().info(damage_caused)
        print(f"Счетчик ударов {self.beat_counter}")
        print(f"Энергия {self.energy}")


    def giveDamage(self):        
        self.energy+=25
        if self.energy>self.energy_max: 
            self.energy = self.energy_max

        if self.beat_counter==3 and self.energy>=60:
            result_damage = self.seriesBlows()
            #self.info(result_damage)
            return result_damage
        else:
            self.deadlyPoison()
            self.beat_counter+=1
            result_damage = super().giveDamage()+self.poison(self.target)
            #self.info(result_damage)
            return result_damage


    def getDamage(self, value: int):
        evasion = self.evasion+(self.lack+self.energy//10*3)*0.2
        if evasion<=randrange(1, 100):
            super().getDamage(value)


    def deadlyPoison (self):
        # Смертельный яд

        new_time = time()
        if self.deadlyPoison_flag==False:
            current = (new_time-self.recharge_deadlyPoison_current)//1
            if current>=self.recharge_deadlyPoison:
                self.energy-=40
                self.recharge_deadlyPoison_current=new_time
                self.deadlyPoison_flag=True
        elif new_time-self.deadlyPoison_duration_current>=self.deadlyPoison_duration:
            self.deadlyPoison_flag=False


    def poison (self, enemy: Sample):
        # дейтсвие яда

        if self.deadlyPoison_flag:
            return enemy.hp*0.05
        else: return 0
        

    def seriesBlows (self):
        # серия ударов

        self.energy-=60
        result_damage = 0
        for _ in range(3):
            result_damage+=super().giveDamage()
        self.beat_counter=0
        return result_damage
    
    
    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()
        
