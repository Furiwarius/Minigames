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

            

            self.armor-=1
            self.damage-=3

            self.speed+=25


    def cripplingShot(self):
          pass

    def sharpEye(self):
          pass