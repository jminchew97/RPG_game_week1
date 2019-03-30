import random as rnd
class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 10
    self.fullHp = 10
    self.inv = []
    self.xp = 0
    self.fullXp = 10
    self.attk = 10
    self.speed = 10
    self.isDeveloper = False
    self.coins = 0
    self.location = 'HOME'
    self.type = 'char'

class Monster:
    def __init__(self,name,attk,speed,hp):
        self.attk = attk
        self.name = name
        self.hp = hp
        self.speed = speed
        self.fullHp = hp
        self.char = 'monster'
    def coinDrop(self):
        return rnd.randint(0,self.attk)