from classes import *
import math
# Syntax to create monsters
# name,attk,speed,hp
monsters = list()
# Read the text file with monsters
names = open('monsterNames.txt', 'r').readlines()

for monster in names:
	if monster == 'name    attk|speed|hp\n':
		continue
	# Separate all attributes of current monster
	properties = monster.split(' ')

	name = properties[0]
	attack = int(properties[1])
	speed = int(properties[2])
	hp = int(properties[3])
	singleMonster = Monster(name, attack,  speed, hp)
	monsters.append(singleMonster)
