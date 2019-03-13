

class Person:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.inv = []
    self.location = 'HOME'

def stats():
    print('---' + char.name + '/HP:' + str(char.hp) + '---')
    print('----' + char.location + '----')

char = Person('Player')
#Main loop
while True:
    print('---ZYTHON RPG---')
    char.name = input('Enter your name:')
    print('Welcome ' + char.name + '.')
    
    #Game loop
    while True:
        stats()


    break