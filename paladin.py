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

        self.recharge_blindingLight = 5
        self.recharge_blindingLight_current = time()
        self.duration_blindingLight = 3


        self.storage_holyFight=0
        
        self.speed-=10
        self.armor+=6
        self.hp+=20
        self.max_hp = self.hp
        self.lack+=10
    

    def info(self, damage_caused=0):
        print("_______________________________________________")
        result_string = super().info(damage_caused)
        +f"Святая ярость {self.holy_fury}\nБроня {self.armor}\nРегенерация {self.regeneration}\n"
        
        print(f"Святая ярость {self.holy_fury}")
        print(f"Броня {self.armor}")
        print(f"Регенерация {self.regeneration}")
        
        return result_string


    def giveDamage(self):
        self.holyFury()
        self.holyFight()
        self.holyHealing()
        blindingLight_damage = self.blindingLight()

        result_damage = super().giveDamage()
        if blindingLight_damage!=0: result_damage=blindingLight_damage
        self.info(result_damage)
        
        return result_damage
    
    
    def getDamage(self, value: int):
        self.holyFury()
        self.healthRecovery()
        self.holyHealing()
        self.holyFight()
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
                
        if self.holy_fury>=30 and time()-self.recharge_holyHealing_current>self.recharge:
            self.holy_fury-=30
            self.armor+=5
            self.regeneration+=3
            self.holy_healong=True

            self.recharge_holyHealing_current=time()
            self.duration_holyHealing_current=time()
                
    
    def blindingLight(self):
        # ослепление светом

        if self.holy_fury>=70 and time()-self.recharge_blindingLight_current>=self.recharge_blindingLight:
            self.holy_fury-=70
            duration = time()
            hp = self.hp
            lost_hp = 0
            while time()-duration<=self.duration_blindingLight:
                lost_hp += hp-self.hp
            else:
                if self.state_live==False:
                    self.state_live=True
                self.hp+=lost_hp
                self.recharge_blindingLight_current=time()
                return lost_hp
        else: return 0


    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()
