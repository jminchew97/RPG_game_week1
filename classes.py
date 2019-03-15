import random as rnd
class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 10
    self.fullHp = 10
    self.inv = []
    self.lvl = 1
    self.isDeveloper = True
    self.coins = 0
    self.location = 'HOME'


class Monster:
    def __init__(self,lvl,name,hp):
        self.lvl = lvl
        self.name = name
        self.hp = hp
        self.fullHp = hp
    def coinDrop(self):
        return rnd.randint(0,self.lvl)