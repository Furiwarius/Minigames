from sample import Sample
from time import time
from random import randrange


class Shooter(Sample):

    def __init__(self, name: str):
            super().__init__(name)

            self.passion = 0
            self.max_passion = 100

            self.recharge_cripplingShot = 4
            self.recharge_cripplingShot_current = time()

            self.recharge_sharpEye = 5
            self.recharge_sharpEye_current = time()
            

            self.armor-=3
            self.damage-=4

            self.speed+=25

    def giveDamage(self):
        result_damage = self.sharpEye()
        if self.sharpEye()!=0: return result_damage
        else:
            pass
            #ДОПИСАТЬ 
    

    def cripplingShot(self):
        
        pass


    def increasedPerformanceDegradation(self, value=1):
        self.lack+=randrange(20, 50)*value
        self.crete+=randrange(1,4)*value

    
    def sharpEye(self):
        # Острый глаз
        if time()-self.recharge_sharpEye_current>=self.recharge_sharpEye and self.passion>=60:
            self.recharge_sharpEye_current=time()
            self.passion-=60
            self.increasedPerformanceDegradation()
            result_damage = super().giveDamage()
            self.increasedPerformanceDegradation(-1)
            return result_damage
        else: return 0


    def enemyGroupTarget(self, group_enemy:list):
        super().enemyGroupTarget(group_enemy)


    def attack (self):
        super().attack()


    def run(self):
        super().run()