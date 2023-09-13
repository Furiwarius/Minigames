from sample import Sample
from random import randrange
from time import time
from collectionInfo import SaveInfo


class Warior(Sample):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.fury = 0
        self.max_fury =200

        self.recharge_furiousBlow = 3
        self.recharge_furiousBlow_current = time()

        self.armor+=6

        self.save_info = SaveInfo(self)
    

    def info(self, damage_caused=0):
        
        result_string = super().info(damage_caused)+f"Fury {self.fury}\n"
        self.save_info.run(result_string)

        return result_string        


    def giveDamage(self):
        if self.fury!=0: self.burst_damage+=(self.fury//20)/10
        result_damage = super().giveDamage()*self.furiousBlow()

        self.info(result_damage)        
        return result_damage


    def getDamage(self, value: int):
        super().getDamage(value)
        self.fury+=10
        self.throughDeath()


    def furiousBlow (self):
        # кровавый удар

        if self.fury>=40 and time()-self.recharge_furiousBlow_current>=self.recharge_furiousBlow:
            self.fury-=40
            self.recharge_furiousBlow_current=time()
            return randrange(2, 4)
        else: 
            self.fury+=20
            return 1
        

    def throughDeath (self):
        # сквозь смерть

        if self.fury>=80 and self.state_live==False:
            self.fury-=80
            self.state_live=True
            self.hp=10


    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()