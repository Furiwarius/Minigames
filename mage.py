from sample import Sample
from time import time
from random import randrange

class Mage(Sample):

    def __init__(self, name: str):
        super().__init__(name)
        
        self.mana=0
        self.max_mana=100
        
        self.recovery_mana=15
        self.recovery_time=1.5
        self.recovery_mana_current=time()

        self.recovery_fireBall=2
        self.recovery_fireBall_current=time()

        self.recovery_magicShield=4
        self.recovery_magicShield_current=time()
        self.duratoin_magicShield=3
        self.duratoin_magicShield_current=0
        self.magicShield_flag = False

        self.magicExplocion_count=0
        self.max_count=5
        self.stored_damage=0

        self.armor-=3
        self.damage-=2


    def info(self, damage_caused=0):
        print("_______________________________________________")
        result_string = super().info(damage_caused)
        +f"Заряды магического взрыва {self.magicExplocion_count}\nСохраненный урон {self.stored_damage}\nМана {self.mana}\n"
        
        print(f"Заряды магического взрыва {self.magicExplocion_count}")
        print(f"Сохраненный урон {self.stored_damage}")
        print(f"Мана {self.mana}")
        
        return result_string

        
    def giveDamage(self):
        self.recoveryMana()
        result_damage = self.magicExplocion()
        if result_damage!=0:
            return result_damage

        self.magicShield()

        result_damage=self.fireBall()
        if result_damage!=0:
            self.info(result_damage)
            return result_damage
        else:
            result_damage = super().giveDamage()
        self.info(result_damage)
        return result_damage


    def getDamage(self, value: int):
        self.recoveryMana()
        if self.magicShield_flag:
            back_damage = value*0.15
            self.stored_damage+=back_damage
            self.target.getDamage(back_damage)
            self.magicCountMax(back_damage)
        super().getDamage(value)
        

    def recoveryMana(self):
        #восстановление маны
        self.mana+=(time()-self.recovery_mana_current)/self.recovery_time*self.recovery_mana
        if self.mana>=self.max_mana: self.mana=self.max_mana
        

    def magicShield(self):
        #магический шит
        if time()-self.recovery_magicShield_current>=self.recovery_magicShield and self.mana>=30:
            self.recovery_magicShield_current=time()
            self.mana-=30
            self.magicShieldOn()
    

    def magicShieldOn(self):
        #включение магического щита
        if self.duratoin_magicShield==0:
            self.duratoin_magicShield=time()
            self.armor+=8
            self.magicShield_flag=True

            
    def magicShieldOf(self):
        #выключение магического щита
        if time()-self.duratoin_magicShield_current>=self.duratoin_magicShield:
            self.recovery_magicShield_current=0
            self.armor-=8
            self.magicShield_flag=False


    def fireBall(self):
        #огненный шар
        if time()-self.recovery_fireBall_current>=self.recovery_fireBall and self.mana>=25:
            self.mana-=25
            self.recovery_fireBall_current=time()
            result_damage = super().giveDamage()*(randrange(15, 21)/10)
            self.magicCountMax(result_damage)
            return result_damage
        else: return 0


    def magicCountMax(self, damage:int):
        # прибавка к зарядам магического взрыва
        if self.magicExplocion_count<self.max_count:
            self.magicExplocion_count+=1
            self.stored_damage+=damage
            

    def magicExplocion(self):
        #Магический взрыв
        if self.magicExplocion_count==self.max_count and self.mana>=60:
            self.mana-=60
            self.magicExplocion_count=0
            result_damage = self.stored_damage
            self.stored_damage=0
            return result_damage
        else: return 0