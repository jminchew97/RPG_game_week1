# change players ability to recieve 0xp from kill

# add descriptions for monsters

# read weapons from text file
# add ability to buy weapons from store
# add extra damage to npc from weapon

import time
import random
from classes import *
from load_obj import monsters, weapons
# developer functions


def allStats(p):
    print(p.hp)
    print(p.fullHp)
    print(p.inv)
    print(p.xp)
    print(p.fullXp)
    print(p.attk)
    print(p.speed)
    print(p.isDeveloper)
    print(p.coins)
    print(p.location)
    print(p.type)


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


def stats():
    inventoryString = 'BAG-[\\'
    for weapon in char.inv:
        inventoryString += ' {} \\'.format(weapon.name)
    inventoryString += ']'
    print(inventoryString)
    print('|{}| {}/{}HP | COINS:{} | ATTACK:{} | SPEED:{} | {}/{}xp'.format(char.name,char.hp, char.fullHp,
                                                                 char.coins, char.attk, char.speed, char.xp, char.fullXp))
    print('----' + char.location + '----')


def space():
    print('\n' * 100)


def cont():
    print('--Enter to continue--')
    input()


def decideFirstHit(p, m):
    pChance = rnd.randint(0, p.speed)
    mChance = rnd.randint(0, m.speed)
    while pChance == mChance:
        pChance = rnd.randint(0, p.speed)
        mChance = rnd.randint(0, m.speed)
    print('PlayerRoll:{} | MonsterRoll:{}'.format(pChance, mChance))
    if pChance > mChance:
        return 1
    elif mChance > pChance:
        return 2


def fightSequence(hitFirst, hitSecond):
    print(hitFirst.name + ' hits first.')
    cont()
    while True:
        space()
        print(
            '{} {}hp || {} {}hp'.format(
                hitFirst.name,
                hitFirst.hp,
                hitSecond.name,
                hitSecond.hp))
        hit = rnd.randint(0, hitFirst.attk)
        print(hitFirst.name + ' hits ' + str(hit))
        hitSecond.hp -= hit
        time.sleep(2)

        # Check if both opponents HP above 0
        if hitFirst.hp <= 0 or hitSecond.hp <= 0:
            print("{} - {}".format(hitFirst.hp, hitSecond.hp))
            break

        hit = rnd.randint(0, hitSecond.attk)
        print(hitSecond.name + ' hits ' + str(hit))
        hitFirst.hp -= hit
        time.sleep(2)

        # One oponent has below 0 HP
        if hitFirst.hp <= 0 or hitSecond.hp <= 0:
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
    # You hits first
    if decideFirstHit(p, m) == 1:
        fightSequence(p, m)
    # Monster hits first
    else:
        fightSequence(m, p)
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
# Create character object
char = Person('Player')

# Main loop
while True:
        # Intro to game
    print('---ZYTHON RPG---')
    char.name = input('Enter your name:')
    if char.name == '':
        char.name = 'Player'
    print('Welcome ' + char.name + '.')
    
    # Game loop
    while True:
        space()
        stats()
        print('Where would you like to go?')
        # Options
        print('| 0.Quit // 1.Sleep // 2.Dungeon // 3.Store // 4.Developer options | ')
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
            choice = input('buy or sell:')
            if choice == 'buy':
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
            
            cont()
        # developer shit
        elif choice == 4:
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
