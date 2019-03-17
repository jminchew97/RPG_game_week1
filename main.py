#add battles
#add dungeon
#create monster generator
#Add descriptions for monsters

import time
from classes import *
def sleep(hp):
  if hp <= 10:
    for x in range(10):
      print('zZ~'*x)
      time.sleep(3)
def stats():
    print('/-' + char.name + '/HP:' + str(char.hp) + ' - '+ 'Coins:'+str(char.coins) + '-/')
    print('----' + char.location + '----')
def space():
  print('\n' * 100)
def cont():
  print('--Enter to continue--')
  input()
def decideFirstHit(p,m):
  pChance = rnd.randint(0,p.speed)
  mChance = rnd.randint(0,m.speed)
  while pChance == mChance:
    pChance = rnd.randint(0,p.speed)
    mChance = rnd.randint(0,m.speed)
  print('PlayerRoll:{} | MonsterRoll:{}'.format(pChance,mChance))
  if pChance > mChance:
    return 1
  elif mChance > pChance:
    return 2
def fightSequence(hitFirst,hitSecond):
  

  print(hitFirst.name + ' hits first.')
  cont()
  while True:
    space()
    print('{} {}hp || {} {}hp'.format(hitFirst.name,hitFirst.hp,hitSecond.name,hitSecond.hp))
    hit = rnd.randint(0,hitFirst.attk)
    print(hitFirst.name + ' hits ' + str(hit) )
    hitSecond.hp -= hit
    time.sleep(1)
    
    #Check if both opponents HP above 0
    if hitFirst.hp <= 0 or hitSecond.hp <= 0:
      print("{} - {}".format(hitFirst.hp,hitSecond.hp))
      break

    hit = rnd.randint(0,hitSecond.attk)
    print(hitSecond.name + ' hits ' + str(hit) )
    hitFirst.hp -= hit
    time.sleep(1)

    #Check if both opponents HP above 0
    if hitFirst.hp <= 0 or hitSecond.hp <= 0:
      print("{} - {}".format(hitFirst.hp,hitSecond.hp))
      break
    
#Fight function p = player m=monster
def fight(p,m):
  space()
  print('You enter a fight with ' + m.name + '.')
  space()
  print("{} {}/{}hp --- {} {}/{}hp".format(p.name,p.hp,p.fullHp,m.name,m.hp,m.fullHp))

  #You hits first
  if decideFirstHit(p,m) == 1:
    fightSequence(p,m)
      
  #Monster hits first
  else:
    fightSequence(m,p)

  #Set hp to 0 if below
  if p.hp <= 0:
    p.hp = 0
    print('You lost to ' + m.name)
    cont()
    
  elif m.hp <= 0:
    coins = m.coinDrop()
    print('You killed ' + m.name + ' and recieved ' + str(coins) + ' coins' )
    p.coins += coins
    cont()

#Create character object
char = Person('Player')

#Main loop
while True:
    #Intro to game
    print('---ZYTHON RPG---')
    char.name = input('Enter your name:')
    print('Welcome ' + char.name + '.')
    
    #Game loop
    while True:

      space()
      stats()
      print('Where would you like to go?')  
      #Options
      print('| 0.Quit // 1.Sleep // 2.Dungeon // 3.Store // 4.Fight | ')
      
      
      choice = int(input('CHOOSE:'))
      if choice == 1:

        #player goes to sleep and health becomes 100
        if char.isDeveloper != True:
          if char.hp <= 100:
            print('You close your eyes and lie down...')
            time.sleep(2)
        char.hp = char.fullHp

      elif choice == 2:
        #Player goes to dungeon and shit
        print('entered dungeon')

      elif choice == 3:
        #Player goes to store and buys shit
        print('entered store')
      elif choice == 4:
        #Create monster
        monst = Monster(10,'BoogaLooga',1,5,10)
        
        #Fight sequence
        fight(char,monst)
        cont()


      elif choice == 10:
        char.isDeveloper = True
        print('Entered developer mode')
        cont()

      elif choice == 0:
        break

      else:
        print('Enter a valid number (0-4)')
        cont()
    
        
    print('Until next time, {}.'.format(char.name))
    break