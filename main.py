#add battles
#add dungeon
#create monster generator
#Add descriptions for monsters
#Add speed as a property to increase chance of striking first

import time
from classes import *
def sleep(hp):
  if hp <= 10:
    for x in range(10):
      print('zZ~'*x)
      time.sleep(3)
def stats():
    print('---' + char.name + '/HP:' + str(char.hp) + '---')
    print('----' + char.location + '----')
def space():
  print('\n' * 100)
def cont():
  print('--Enter to continue--')
  input()

#Fight function p = player m=monster
def fight(p,m):
  space()
  print('You enter a fight with ' + m.name + '.')
  #Dice roll on who goes first
  roll = rnd.randint(0,1)

  while m.hp and p.hp != 0:
    space()
    print("{} {}/{}hp --- {} {}/{}hp".format(p.name,p.hp,p.fullHp,m.name,m.hp,m.fullHp))
    
    
    hit = rnd.randint(0,m.lvl)
    print(p.name + ' hits ' + str(hit) )
    m.hp -= hit
    cont()
    hit = rnd.randint(0,p.lvl)
    print(m.name + ' hits ' + str(hit) )
    m.hp -= hit
    cont()
    #Set hp to 0 if below
    if p.hp <= 0:
      p.hp = 0
      print('You lost to ' + m.name)
      cont()
      break
    elif m.hp <= 0:
      coins = m.coinDrop()
      print('You killed ' + m.name + ' and recieved ' + str(coins) + ' coins' )
      p.coins += coins
      cont()

      break


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
            sleep(char.hp)
        char.sleep = 100

      elif choice == 2:
        #Player goes to dungeon and shit
        print('entered dungeon')

      elif choice == 3:
        #Player goes to store and buys shit
        print('entered store')
      elif choice == 4:
        monst = Monster(10,'BoogaLooga',10)
        
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