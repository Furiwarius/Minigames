import random

from sample import Sample

class Paladin (Sample):

    def __init__(self, name:str):
        super().__init__(name)

        self.holy_fury = 0
        self.holy_fury_max = 100

        self.regeneration = 2

        self.recharge = 3
        self.recharge_holyHealing_current = 0
        self.duration_holyHealing = 2
        self.duration_holyHealing_current = 0

        self.recharge_blindingLight_current = 0
        
        
        self.armor+=5
        self.hp+=20
        self.percent_hp = self.hp
        self.lack+=10


    def giveDamage(self):
        self.holyFight()
        return super().giveDamage()
    
    def getDamage(self, value: int):
        self.holyFight()
        super().getDamage(value)

    def holyFight(self):

        # священный бой

        if self.hp<self.percent_hp: self.hp+=self.regeneration
        else: self.hp=self.percent_hp
        if self.holy_fury<=self.holy_fury_max:
            self.holy_fury+=15
        else: self.holy_fury=self.holy_fury_max
        self.holyHealing()
        self.blindingLight()
        
        if self.holy_fury!=0 and self.holy_fury<=self.holy_fury_max: 
            self.armor+=self.holy_fury//10
            self.regeneration+=1



    def holyHealing (self):

        # святое исцеление
        
        if self.holy_fury>=40 and self.recharge_holyHealing_current==0:
            self.holy_fury-=40
            self.armor+=5
            self.regeneration+=3

            self.recharge_holyHealing_current+=self.recharge
            self.duration_holyHealing_current+=self.duration_holyHealing
        else:
            if self.recharge_blindingLight_current!=0: 
                self.recharge_holyHealing_current-=1
            if self.duration_holyHealing_current>0:
                self.duration_holyHealing_current-=1
                if self.duration_holyHealing_current==0:
                    self.armor-=5
                    self.regeneration-=3
    
    def blindingLight(self):

        # ослепление светом

        pass