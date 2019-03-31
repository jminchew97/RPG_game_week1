

# add save / load

# ---Things to add in future---
# add speed dynamic to fighting


# things I learned
# -functions functions functions

'''

-can now wield weapons


'''

import pickle
import time
import random
from classes import *
from load_obj import monsters, weapons
# developer functions


def isWield(char):
    if char.wield != False:
        return char.wield.bonus
    else:
        return False

def wield():
    if char.wield != False:
        print('Wielding: {}'.format(char.wield.name))
    else:
        print('Wielding: Nothing')
def sleep(char):
    if char.hp < char.fullHp:
        for x in range(char.fullHp - char.hp):
            print('zZ~' * x)
            time.sleep(3)
    else:
        print('Your HP is full.')


def death():
    time.sleep(1)
    print('You get very sleep...')
    time.sleep(2)
    print('A bright light appears and takes you away.')
    time.sleep(4)

def inventory():
    count = 0
    inventoryString = 'BAG~[\\'
    for weapon in char.inv:
        inventoryString += '{}.{}\\'.format(count,weapon.name)
        count += 1
    inventoryString += ']'
    print(inventoryString)
    count += 1

def stats():
    wield()
    inventory()
    print('|{}| {}/{}HP | COINS:{} | ATTACK:{} | SPEED:{} | {}/{}xp'.format(char.name,char.hp, char.fullHp,
                                                                 char.coins, char.attk, char.speed, char.xp, char.fullXp))
    print('-'*10)
    print('')
    

def space():
    print('\n' * 100)


def cont():
    print('--Enter to continue--')
    input()

def fightSequence(char, monst):
    print(char.name + ' hits first.')
    cont()
    while True:
        space()
        print(
            '{} {}hp || {} {}hp'.format(
                char.name,
                char.hp,
                monst.name,
                monst.hp))
        hit = rnd.randint(0, char.attk)
        
        # has weapon
        if isWield(char):
            hit += char.wield.bonus
            print('{} hits a {} with a {}'.format(char.name,hit,
                                                         char.wield.name))
        else:
            # does not have weapon
            print(char.name + ' hits ' + str(hit))
    
        monst.hp -= hit
        time.sleep(2)

        # check HP
        if char.hp <= 0 or monst.hp <= 0:
            break

        # monsters turn to hit
        hit = rnd.randint(0, monst.attk)
        print(monst.name + ' hits ' + str(hit))
        char.hp -= hit
        time.sleep(2)
        # One oponent has below 0 HP
        if monst.hp <= 0 or char.hp <= 0:
            break

def checkIfLevelUp(player, gainXp):
    # easy use variables
    leftOver = 0
    # add xp
    player.xp += gainXp
    print('You gained {} xp!'.format(gainXp))
    cont()

    # player levels up
    if player.xp >= player.fullXp:
        # check if theres extra xp
        leftOver = player.xp - player.fullXp
        # reset xp
        player.xp = leftOver
        # increase attack
        player.attk += 1
        # increase speed
        player.speed += 1
        # increase hp level
        player.fullXp += (player.fullXp * .5)
        player.fullXp = round(player.fullXp)
        # give player full heal
        player.hp = player.fullHp
        print('***Congrats you leveled up your attack to level {} *** '.format(player.attk))

# Fight function p = player m = monster


def fight(p, m):
    space()
    print('You enter a fight with ' + m.name + '.')
    cont()
    print("{} {}/{}hp --- {} {}/{}hp".format(p.name,
                                             p.hp, p.fullHp, m.name, m.hp, m.fullHp))
    
    fightSequence(p, m)
    
    # You lose
    if p.hp <= 0:
        p.hp = 0
        print('You lost to ' + m.name)
        cont()
    # You win
    elif m.hp <= 0:
        # Get coins
        coins = m.coinDrop()
        print(
            'You killed ' +
            m.name +
            ' and recieved ' +
            str(coins) +
            ' coins')
        p.coins += coins

        # Level up function
        checkIfLevelUp(p, m.attk * random.randint(1, m.attk))
        cont()
    m.hp = m.fullHp

def saveGame():
    pickle_out = open("data.pickle","wb")
    pickle.dump(char, pickle_out)
    pickle_out.close()
    print('--SAVED GAME--')
    cont()
# Create character object
char = Person('Player')

# auto wield weapon for developer purposes
#char.inv.append(weapons[2])
space()

# Main loop
print('---ZYTHON RPG---')
print('1.New Game / 2.Load Game')
choice = input('Choose:')
if choice == '1':
    char.name = input('Enter your name:')
    if char.name == '':
        char.name = 'Player'
    print('Welcome ' + char.name + '.')
elif choice == '2':

    char = pickle.load( open( 'data.pickle', "rb" ) )
    print('--LOADED GAME--')
    print('Welcome back {}'.format(char.name))

while True:    
    try:
            # Intro to game
        

        
        # new player

        # Game loop
        while True:
            space()
            stats()
            print('Where would you like to go?')
            # Options
            print('| 0.Quit // 1.Sleep // 2.Dungeon // 3.Store // 4.Equipt Weapon // 5.SAVE 10.Developer options //| ')
            choice = int(input('CHOOSE:'))
            
            if choice == 1:

                # player goes to sleep and health becomes 100
                if char.hp <= char.fullHp:
                    print('You close your eyes and lie down...')
                    Zs = ''
                    for x in range(char.fullHp - char.hp):
                        space()
                        Zs += 'z'
                        print(Zs)
                        time.sleep(.5)
                        space()
                        Zs += 'Z'
                        print(Zs)
                        time.sleep(.5)

                char.hp = char.fullHp

            # Dungeon
            elif choice == 2:
                # Player goes to dungeon and shit
                print('entered dungeon')
                cont()
                while True:
                    # exit dungeon player is dead
                    if char.hp <= 0:
                        death()
                        break

                    stats()
                    count = 1
                    # print out monsters in monster_file
                    for x in range(len(monsters)):
                        currentMonster = monsters[x]
                        print(
                            'NPC#:{}\n{}\nlevel:{}\n'.format(
                                count,
                                currentMonster.name,
                                currentMonster.attk))
                        count += 1

                    # User input
                    answer = int(
                        input('Choose a monster to fight: {}-{}:'.format(1, len(monsters))))

                    if answer > 0 and answer <= len(monsters):
                        fight(char, monsters[answer - 1])
                    elif answer == 0:
                        print('Come back to the dungeon soon...')
                        break
                        cont()
                    else:
                        # Input error
                        print('Error')

            elif choice == 3:
                # Player goes to store and buys stuff
                print('entered store')
                print('Would you like to buy or sell?')
                choice = input('1.buy or 2.sell:')
                if choice == '1':
                    print('Heres what I got...')
                    cont()
                    space()
                    print('Weapon list')
                    print('* ' * 15)
                    print('Your attack is currently level {}'.format(char.attk))
                    print('* ' * 15)
                    count = 0
                    for weapon in weapons:
                        print('{}. {} - attackBonus:{} | price:{} | level {} attk needed'.format(
                            count, weapon.name, weapon.bonus, weapon.price, weapon.level))
                        print('-' * 10)
                        count += 1
                    choice = int(input())
                    if choice <= len(weapons) - 1 and choice >= 0:
                        buyWep = weapons[choice]
                        if char.attk >= buyWep.level and char.coins >= buyWep.price:
                                
                            print('So you want to buy {} for {}?'.format(buyWep.name,buyWep.price))
                            choice = input('y or n')
                            if choice == 'y':
                                char.inv.append(buyWep)
                                char.coins -= buyWep.price
                                print('***Added {} to inventory***'.format(buyWep.name))
                                
                            elif choice == 'n':
                                print('Make up your mind kid.')
                        else:
                            print('You need at least level {} to buy a {}.'.format(buyWep.level,buyWep.name))
                # sell items
                elif choice == '2':
                    print('What do you wanna sell me?')
                    inventory()
                    choice = int(input('Choose item:'))
                    if choice >= 0 and choice <= len(char.inv) - 1:
                        weaponChoice = char.inv[choice]
                        sellPrice = round(weaponChoice.price / 2)
                        print('So you want to sell {} for {}'.format(weaponChoice.name,
                                                                        sellPrice))
                        inp = input('y or n:')
                        if inp == 'y':
                            
                            print('***You sold {} for {} coins***'.format(weaponChoice.name,
                                                                            sellPrice))
                            char.coins += sellPrice 
                            if char.inv[choice].wield == True:
                                char.wield = False                                           
                            del char.inv[choice]

                        elif inp == 'n':
                            print('My mistake')
                    cont()       
                cont()
            # wielding
            elif choice == 4:
                inventory()
                print('1.Equipt 2.Unequipt')
                choice = input('Choose Action:')
                # make sure character is not holding weapon 
                if choice == '1' and char.wield == False:
                    inventory()
                    print('What weapon would you like to wield?')
                    choice = int(input('Wield weapon:'))
                    if choice >= 0 and choice <= len(char.inv)-1:
                        char.inv[choice].wield = True
                        char.wield = char.inv[choice]
                        
                        char.bonus = char.wield.bonus
                        print('You are now holding a {}.'.format(char.wield.name))
                elif choice == '2':
                    if char.wield != False:
                        print('Unwield {}?'.format(char.name))
                        choice = input('y or n')
                        if choice == 'y':
                            char.wield.wield = False
                            char.wield = False
                        else:
                            print('You are not wielding a weapon...')
                cont()
            elif choice == 5:
                saveGame()
                
            elif choice == 10:
                while True:
                    print('1.set level | 2.set coins')
                    inp = input('option:')
                    if inp == '1':
                        inp = input('Enter level')
                        char.attk = int(inp)
                        print('Your attack is now {}'.format(char.attk))
                    elif inp == '2':
                        coins = int(input('Insert coin amount.'))
                        char.coins += coins
                        print('added {} coins'.format(coins))
                    elif inp == '0':
                        break
            elif choice == 0:
                break
            else:
                print('Enter a valid number (0-4)')
                cont()

        # Save game
        print('Until next time, {}.'.format(char.name))

        break
    except:
        print('That is not a valid option.')
        cont()
