import random
from time import time

from sample import Sample

class Paladin (Sample):

    def __init__(self, name:str):
        super().__init__(name)

        self.holy_fury = 0
        self.holy_fury_max = 100

        self.regeneration = 5

        self.recharge = 3
        self.recharge_holyHealing_current = 0

        self.holy_healing = False
        self.duration_holyHealing = 2
        self.duration_holyHealing_current = 0

        self.recharge_blindingLight_current = 0

        self.storage_holyFight=0
        
        self.speed-=10
        self.armor+=6
        self.hp+=20
        self.max_hp = self.hp
        self.lack+=10
    

    def info(self, damage_caused=0):
        print("_______________________________________________")
        super().info(damage_caused)
        print(f"Святая ярость {self.holy_fury}")
        print(f"Броня {self.armor}")
        print(f"Регенерация {self.regeneration}")



    def giveDamage(self):
        self.holyFury()
        self.holyFight()
        self.holyHealing()
        self.blindingLight()
        
        result_damage = super().giveDamage()
        self.info(result_damage)
        
        return result_damage
    
    def getDamage(self, value: int):
        self.holyFury()
        self.holyHealing()
        super().getDamage(value)


    def holyFury(self):
        # накопление святой ярости
        if self.holy_fury<=self.holy_fury_max:
            self.holy_fury+=15
        else: self.holy_fury=self.holy_fury_max


    def healthRecovery(self):
        # Регенерация хп
        if self.hp<self.max_hp: self.hp+=self.regeneration
        else: self.hp=self.max_hp
        

    def holyFight(self):
        # священный бой
        
        self.armor-=self.storage_holyFight
        self.regeneration-=self.storage_holyFight
        if self.holy_fury!=0:
            self.storage_holyFigth=self.holy_fury//10
            self.armor+=self.storage_holyFight
            self.regeneration+=self.storage_holyFight


    def calculationDuration(self):
        if time()-self.duration_holyHealing_current>=self.duration_holyHealing: return True
        else: return False


    def holyHealing (self):
        # святое исцеление
        if self.holy_healing and self.calculationDuration():
                self.armor-=5
                self.regeneration-=3
                self.holy_healong=False
                
        if self.holy_fury>=40 and time()-self.recharge_holyHealing_current>self.recharge:
            self.holy_fury-=40
            self.armor+=5
            self.regeneration+=3
            self.holy_healong=True

            self.recharge_holyHealing_current=time()
            self.duration_holyHealing_current=time()
                
    
    def blindingLight(self):
        # ослепление светом

        pass


    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()
