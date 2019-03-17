import random as rnd
class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 10
    self.fullHp = 10
    self.inv = []
    self.lvl = 1
    self.attk = 10
    self.speed = 10
    self.isDeveloper = True
    self.coins = 0
    self.location = 'HOME'


class Monster:
    def __init__(self,lvl,name,attk,speed,hp):
        self.lvl = lvl
        self.attk = attk
        self.name = name
        self.hp = hp
        self.speed = speed
        self.fullHp = hp
    def coinDrop(self):
        return rnd.randint(0,self.lvl)