import random as rnd
class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 10
    self.fullHp = 10
    self.inv = []
    self.xp = 0
    self.fullXp = 10
    self.attk = 5
    self.wield = False
    self.type = 'character'
    self.speed = 10
    self.coins = 0

class Monster:
    def __init__(self,name,attk,speed,hp):
        self.attk = attk
        self.name = name
        self.hp = hp
        self.weapon = 0
        self.speed = speed
        self.fullHp = hp
        self.type = 'monster'
    def coinDrop(self):
        return rnd.randint(0,self.attk)
class Weapon:
    def __init__(self,name,attackBonus,levelNeeded,price):
        self.name = name
        self.bonus = attackBonus
        self.level = levelNeeded
        self.wield = False
        self.price = price