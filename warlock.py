from time import time
from collectionInfo import SaveInfo
from sample import Sample

class Warlock(Sample):

    def __init__(self):
        super().__init__()

        self.vampirism = 3 
        self.armor-=1
        self.hp+=20
        self.max_hp = self.hp

        self.recharge_sphereDarkness = 4
        self.recharge_sphereDarkness_current = time.time()

        self.recharge_lifeSiphon = 5
        self.recharge_lifeSiphon_current = time.time()

        self.save_info = SaveInfo(self)

    def info(self, damage_caused=0):
        class_str = f"Vampirism {self.vampirism}\n"
        result_string = super().info(damage_caused)+class_str
        self.save_info.run(result_string)
        
        return result_string
    

    def giveDamage(self):
        if self.lifeSiphon():
            result_damage=self.lifeSiphon()+self.powerDarkness()
        elif self.sphereDarkness():
            result_damage=super().giveDamage()+self.sphereDarkness()+self.powerDarkness()
        else:
            result_damage=super().giveDamage()+self.powerDarkness()
            
        self.info(result_damage)
        return result_damage

    def getDamage(self, value):
        super().getDamage(value)        
        
        
    def sphereDarkness (self):
        # Сфера тьмы
        if (time()-self.recharge_sphereDarkness_current)//1>=self.recharge_sphereDarkness:
            result_damage = 20
            self.hp-= self.hp*0.07
            self.recharge_sphereDarkness_current= time()
            return result_damage
        else: return 0


    def powerDarkness (self):
        # Сила тьмы
        count = ((self.max_hp-self.hp)/(self.max_hp*0.01))//5
        self.hp+=count*3+self.vampirism
        return count*3
        
        
    def lifeSiphon (self):
        # Высасывание жизни
        if (time()-self.recharge_lifeSiphon_current)//1>=self.recharge_lifeSiphon and self.hp<=self.max_hp*0.5:
            result_damage = self.damage*self.burst_damage*2.5
            self.hp+=result_damage*0.35
            self.recharge_lifeSiphon_current=time()
            return result_damage  
        else: return 0  

    
    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()