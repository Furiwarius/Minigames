import time

from sample import Sample

class Warlock(Sample):

    def __init__(self):
        super().__init__()

        self.vampirism = 3 
        self.armor-=3
        self.hp+=20
        self.max_hp = self.hp

        self.recharge_sphereDarkness = 4
        self.recharge_sphereDarkness_current = time.time()

        self.recharge_lifeSiphon = 5
        self.recharge_lifeSiphon_current = time.time()

    def giveDamage(self):
        if self.lifeSiphon():
            return self.lifeSiphon()+self.powerDarkness()
        elif self.sphereDarkness():
            return super().giveDamage()+self.sphereDarkness()+self.powerDarkness()
        else:
            return super().giveDamage()+self.powerDarkness()

    def getDamage(self, value):
        super().getDamage(value)        
        
        
    def sphereDarkness (self):
        
        if (time.time()-self.recharge_sphereDarkness_current)//1>=self.recharge_sphereDarkness:
            result_damage = 20
            self.hp-= self.hp*0.07
            self.recharge_sphereDarkness_current= time.time()
            return result_damage
        else: return 0


    def powerDarkness (self):

        count = ((self.max_hp-self.hp)/(self.max_hp*0.01))//5
        self.hp+=count*3+self.vampirism
        return count*3
        
        
    def lifeSiphon (self):
        if (time.time()-self.recharge_lifeSiphon_current)//1>=self.recharge_lifeSiphon and self.hp<=self.max_hp*0.5:
            result_damage = self.damage*self.burst_damage*2.5
            self.hp+=result_damage*0.35
            return result_damage  
        else: return 0  