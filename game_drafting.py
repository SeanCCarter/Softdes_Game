"""
whoop whoop
orthogonal terraria here we goooooo

"""

import random
import sys
import pygame

class player:
	def __init__(self):
		self.inventory = []
		self.max_hp = 5
		self.hp = 5
		self.x = 3
		self.y = 3
		self.direction = 1


	def turn_left(self):
		"""  0
		   3 + 1
		     2
		     """
		self.direction = (self.direction - 1)%4


	def turn_right(self):
		self.direction = (self.direction + 1)%4


	def move_forward(self):
		if self.direction == 0:
			self.y += 1
		elif self.direction == 1:
			self.x += 1
		elif self.direction == 2:
			self.y += -1
		elif self.direction == 3:
			self.x += -1


class block:
	def __init__(self, block_id):
		"""
		creates an object with a given ID. Python doesn't exactly have a case structure, so... elifs?
		"""
		pass


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


test_var = 1

world = generate_world(12,12)

pygame.init()
SCREEN = pygame.display.set_mode((768,768))
font = pygame.font.SysFont("Arial",30)


exit_flag = False

matt = player()	

up_arrow = pygame.image.load('up_arrow.png')
right_arrow = pygame.image.load('right_arrow.png')
down_arrow = pygame.image.load('down_arrow.png')
left_arrow = pygame.image.load('left_arrow.png')
grass = pygame.image.load('grass.png')
tree = pygame.image.load('tree.png')

avatar_dict = {}
avatar_dict[0] = up_arrow
avatar_dict[1] = right_arrow
avatar_dict[2] = down_arrow
avatar_dict[3] = left_arrow

while not exit_flag:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit_flag = True
			elif event.key == pygame.K_UP:
				matt.move_forward()
			elif event.key == pygame.K_LEFT:
				matt.turn_left()
			elif event.key == pygame.K_RIGHT:
				matt.turn_right()
	label = font.render('(' + str(matt.x) + ', ' + str(matt.y) + ')',1,(0,0,0))
	SCREEN.fill((255,255,255))
	for i in range(len(world)):
		for j in range(len(world[0])):
			if world[i][j] == '.':
				SCREEN.blit(grass, (i*64, j*64))
			elif world[i][j] == 'T':
				SCREEN.blit(tree, (i*64, j*64))
			else:
				pass
	SCREEN.blit(avatar_dict[matt.direction], (matt.x*64, (768 -matt.y*64)))
	SCREEN.blit(label, (300,300))
	pygame.display.flip()
# while game_flag == True:
# 	print test_var
# 	test_var += 1
# 	if test_var >= 3:
# 		game_flag = False
# 	

# while game_flag == True: