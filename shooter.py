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
            self.duration_cripplingShotBaff = 2
            self.duration_cripplingShotBaff_current = 0
            self.crippled_speed = 0
            self.crippled_damage = 0
            

            self.recharge_sharpEye = 3
            self.recharge_sharpEye_current = time()
            

            self.armor-=3
            self.damage-=4

            self.speed+=25
            self.increase_speed_current=0
            self.increase_speed = 5


    def info(self, damage_caused=0):
        print("_______________________________________________")
        result_string = super().info(damage_caused)
        +f"Скорость {self.speed}\nЭнергия {self.passion}\n"
        
        print(f"Скорость {self.speed}")
        print(f"Энергия {self.passion}")
        
        return result_string


    def giveDamage(self):
        self.passion+=15
        self.cripplingShotBaffOf()
        sharpEye_damage = self.sharpEye()
        if self.sharpEye()!=0:
            self.info(sharpEye_damage)
            return sharpEye_damage
        else:
            result_damage = super().giveDamage()+self.cripplingShot()
            self.info(result_damage)
            return result_damage


    def getDamage(self, value:int):
        self.passion+=5
        super().getDamage(value)
    

    def cripplingShot(self):
        # калечащий выстрел
        if time()-self.recharge_cripplingShot_current>=self.recharge_cripplingShot and self.passion>=30:
            self.recharge_cripplingShot_current = time()
            self.passion-=30
            result_damage = 5+ self.target.hp*0.05
            self.cripplingShotBaffOn()
            return result_damage
        else: 
            return 0

    def cripplingShotBaffOn(self):
        #включение усиления от колечащего выстрела
        if self.duration_cripplingShotBaff_current==0:
            self.duration_cripplingShotBaff_current=time()
            self.burst_damage+=0.2
            self.crippled_speed=self.target.speed*0.2
            self.crippled_damage=self.target.damage*0.2
            
            self.target.speed-=self.crippled_speed
            self.target.damage-=self.crippled_damage
            

    def cripplingShotBaffOf(self):
        #выключение усиления от колечащего выстрела
        if time()-self.duration_cripplingShotBaff_current>=self.duration_cripplingShotBaff and self.duration_cripplingShotBaff_current!=0:
            self.duration_cripplingShotBaff_current=0
            self.burst_damage-=0.2
            self.target.speed+=self.crippled_speed
            self.target.damage+=self.crippled_damage
            

    def passionForShooting(self):
        # пассивная прибавка к скорости атаки от количества азарта(passion) 
        self.speed-=self.increase_speed_current
        self.increase_speed_current=(self.passion//10*self.increase_speed)
        self.speed+=self.increase_speed_current


    def increasedPerformanceDegradation(self, value=1):
        # при value=1 прибавляет характеристики, при -1 отнимает
        self.lack+=randrange(20, 50)*value
        self.crete+=randrange(1,5)*value

    
    def sharpEye(self):
        # Острый глаз
        if time()-self.recharge_sharpEye_current>=self.recharge_sharpEye and self.passion>=60:
            self.recharge_sharpEye_current=time()
            self.passion-=60
            self.increasedPerformanceDegradation(1)
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