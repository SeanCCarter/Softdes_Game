"""
whoop whoop
orthogonal terraria here we goooooo

"""

import pygame
import random
import sys
import math

pygame.init()

game_flag = True

class player:
	def __init__(self):
		self.inventory = []
		self.max_hp = 5
		self.hp = 5

class block:
	def __init__(self, block_id):
		"""
		creates an object with a given ID. Python doesn't exactly have a case structure, so... elifs?
		"""
		pass

turn_count = 1

matt = player()

def generate_world(x_size, y_size):
	"""
	Generates an x-by-y world pseudorandomly; represents it as a list of x lists of y length; [i,j].
	"""

	def make_blank_world():
		"""
		Creates an x-by-y list of lists of zeroes.
		"""
		blank_array = [[0 for j in range(y_size + 1)] for i in range(x_size + 1)]
		return blank_array


	def check_surroundings(x_coord, y_coord, value):
		"""
		If the variable world has already been defined, it checks all x and y coords within one square (aka, checks the 8 surrounding squares) for a given value. If that value is present in 1 or more squares, returns True; else, False.
		"""
		for i in range(3):
			for j in range(3):
				if world[x_coord - 1 + i][y_coord - 1 + j] == value:
					return True
				else:
					pass
		return False

	world = make_blank_world()

	for i in range(x_size):
		for j in range(y_size):
			seed = random.random()
			if not check_surroundings(i, j, 'T'):
				if seed >= 0.5:
					world[i][j] = 'T'
				else:
					world[i][j] = '.'
			else:
				world[i][j] = '.'
	return [row[:y_size] for row in world[:x_size]]



if __name__ == '__main__':

	test_var = 1

	test_world = generate_world(12,12)

	for i in range(len(test_world)):
		print ' '.join(test_world[i])
	# while game_flag == True:
	# 	print test_var
	# 	test_var += 1
	# 	if test_var >= 3:
	# 		game_flag = False
	# 	