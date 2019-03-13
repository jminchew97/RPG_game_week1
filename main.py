

class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.inv = []
    self.coins = 0
    self.location = 'HOME'

def stats():
    print('---' + char.name + '/HP:' + str(char.hp) + '---')
    print('----' + char.location + '----')

def cont():
  print('Hit enter to continue.')
  input()
char = Person('Player')
#Main loop
while True:
    #Intro to game
    print('---ZYTHON RPG---')
    char.name = input('Enter your name:')
    print('Welcome ' + char.name + '.')
    
    #Game loop
    while True:
        stats()
        print('Where would you like to go?')  
        #Options
        print('| 0.Quit // 1.Sleep // 2.Dungeon // 3.Store // 4.Skills(maybe) | ')
        
        try:
          choice = int(input('CHOOSE:'))
          if choice == 1:
            #player goes to sleep and health becomes 100
            print('entered sleep')
          elif choice == 2:
            #Player goes to dungeon and shit
            print('entered dungeon')
          elif choice == 3:
            #Player goes to store and buys shit
            print('entered store')
          elif choice == 0:
            break
          else:
            print('Enter a valid number (0-4)')
            cont()
        except:
          print('ERROR:')
          print('Enter a number 0-4')
          cont()
        
    print('Until next time, {}.'.format(char.name))
    break