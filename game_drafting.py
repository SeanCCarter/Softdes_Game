"""
whoop whoop
orthogonal terraria here we goooooo

"""

import random
import sys
import pygame


class Block(object):
	def __init__(self, name, graphic, walkable=True, destructible=False, drop=[]):
		"""
		creates an object with a given name, graphic, etc. Python doesn't exactly have a case structure, so... elifs?
		"""
		self.name = name
		self.graphic = pygame.image.load('graphics/' +graphic)
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop




class Tree(Block):
	def __init__(self):
		super(Tree, self).__init__('tree', 'tree.png', False, True, Wood)


class Water(Block):
	def __init__(self):
		super(Water, self).__init__('water', 'water.png', False, False)


class Grass(Block):
	def __init__(self):
		super(Grass, self).__init__('grass', 'grass.png', True, False)


class Dirt(Block):
	def __init__(self):
		super(Dirt, self).__init__('dirt', 'dirt.png', True, False)


class Wood(Block):
	def __init__(self):
		super(Wood, self).__init__('wood', 'wood.png', False, True, Wood)


class Blank(Block):
	def __init__(self):
		super(Blank, self).__init__('blank', 'water.png', False, False)




class player(object):
	def __init__(self):
		self.inventory = {}
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
			if world[self.x][self.y-1].walkable:
				self.y -= 1
		elif self.direction == 1:
			if world[self.x+1][self.y].walkable:
				self.x += 1
		elif self.direction == 2:
			if world[self.x][self.y+1].walkable:
				self.y += 1
		elif self.direction == 3:
			if world[self.x-1][self.y].walkable:
				self.x -= 1


	def move_backward(self):
		if self.direction == 0:
			if world[self.x][self.y+1].walkable:
				self.y += 1
		elif self.direction == 1:
			if world[self.x-1][self.y].walkable:
				self.x -= 1
		elif self.direction == 2:
			if world[self.x][self.y-1].walkable:
				self.y -= 1
		elif self.direction == 3:
			if world[self.x+1][self.y].walkable:
				self.x += 1


	def add_to_inventory(self, item):
		"""
		Adds item to the dictionary.
		"""
		if item in self.inventory:
			self.inventory[item] += 1
		else:
			self.inventory[item] = 1


	def remove_from_inventory(self, item):
		"""
		Decrements item's value in the dictionary, then removes it entirely if the value is zero.
		"""
		if item in self.inventory:
			self.inventory[item] -= 1
			if self.inventory[item] == 0:
				del self.inventory[item]


	def check_inventory(self, item):
		return item in self.inventory


	def mine(self):
		if self.direction == 0:
			if world[self.x][self.y-1].destructible:
				self.add_to_inventory(world[self.x][self.y-1].drop)
				world[self.x][self.y-1] = Dirt()
		elif self.direction == 1:
			if world[self.x+1][self.y].destructible:
				self.add_to_inventory(world[self.x+1][self.y].drop)
				world[self.x+1][self.y] = Dirt()
		elif self.direction == 2:
			if world[self.x][self.y+1].destructible:
				self.add_to_inventory(world[self.x][self.y+1].drop)
				world[self.x][self.y+1] = Dirt()
		elif self.direction == 3:
			if world[self.x-1][self.y].destructible:
				self.add_to_inventory(world[self.x-1][self.y].drop)
				world[self.x-1][self.y] = Dirt()


	def place(self, item):
		if not item in self.inventory:
			return False
		else:
			if self.direction == 0:
				if world[self.x][self.y-1].walkable:
					world[self.x][self.y-1] = item()
					self.remove_from_inventory(item)
			elif self.direction == 1:
				if world[self.x+1][self.y].walkable:
					world[self.x+1][self.y] = item()
					self.remove_from_inventory(item)
			elif self.direction == 2:
				if world[self.x][self.y+1].walkable:
					world[self.x][self.y+1] = item()
					self.remove_from_inventory(item)
			elif self.direction == 3:
				if world[self.x-1][self.y].walkable:
					world[self.x-1][self.y] = item()
					self.remove_from_inventory(item)


def generate_world(x_size, y_size):
	"""
	Generates an x-by-y world pseudorandomly; represents it as a list of x lists of y length; [i,j].
	"""

	def make_blank_world():
		"""
		Creates an x-by-y list of lists of zeroes.
		"""
		blank_array = [[Blank() for j in range(y_size + 1)] for i in range(x_size + 1)]
		return blank_array


	def check_surroundings(x_coord, y_coord, value):
		"""
		If the variable world has already been defined, it checks all x and y coords within one square (aka, checks the 8 surrounding squares) for a given value. If that value is present in 1 or more squares, returns True; else, False.
		"""
		for i in range(3):
			for j in range(3):
				examining = world[x_coord - 1 + i][y_coord - 1 + j]
				if examining.name == value:
					return True
				else:
					pass
		return False


	world = make_blank_world()

	world[random.randint(2, x_size-2)][random.randint(2, y_size-2)] = Water()

	for i in range(x_size):
		for j in range(y_size):
			seed = random.random()
			if check_surroundings(i, j, 'water'):
				if seed >= 0.5:
					world[i][j] = Water()
				elif seed >= 0.4:
					world[i][j] = Tree()
				else:
					world[i][j] = Grass()
			elif not check_surroundings(i, j, 'tree'):
				if seed >= 0.5:
					world[i][j] = Tree()
				else:
					world[i][j] = Grass()
			else:
				world[i][j] = Grass()
	return [row[:y_size+1] for row in world[:x_size+1]]





if __name__== '__main__':

	pygame.init()

	world = generate_world(12,12)

	SCREEN = pygame.display.set_mode((768,768))
	font = pygame.font.SysFont("Arial",30)


	exit_flag = False

	matt = player()	

	up_arrow = pygame.image.load('up_arrow.png')
	right_arrow = pygame.image.load('right_arrow.png')
	down_arrow = pygame.image.load('down_arrow.png')
	left_arrow = pygame.image.load('left_arrow.png')

	avatar_dict = {}
	avatar_dict[0] = up_arrow
	avatar_dict[1] = right_arrow
	avatar_dict[2] = down_arrow
	avatar_dict[3] = left_arrow


	key_to_function_dict = {pygame.K_UP: matt.move_forward, pygame.K_LEFT: matt.turn_left, pygame.K_RIGHT: matt.turn_right, pygame.K_DOWN: matt.move_backward, pygame.K_SPACE: matt.mine}


	while not exit_flag:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_flag = True
				if event.key in key_to_function_dict:
					key_to_function_dict[event.key]()
				if event.key == pygame.K_LSHIFT:
					matt.place(Wood)
		label = font.render('(' + str(matt.x) + ', ' + str(matt.y) + ')',1,(0,0,0))
		SCREEN.fill((255,255,255))
		for i in range(len(world)):
			for j in range(len(world[0])):
				SCREEN.blit(world[i][j].graphic, (i*64, j*64))
		SCREEN.blit(avatar_dict[matt.direction], (matt.x*64, matt.y*64))
		SCREEN.blit(label, (300,300))
		pygame.display.flip()


# while not exit_flag:
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				exit_flag = True
# 			elif event.key == pygame.K_UP:
# 				matt.move_forward()
# 			elif event.key == pygame.K_LEFT:
# 				matt.turn_left()
# 			elif event.key == pygame.K_RIGHT:
# 				matt.turn_right()
# 	label = font.render('(' + str(matt.x) + ', ' + str(matt.y) + ')',1,(0,0,0))
# 	SCREEN.fill((255,255,255))
# 	for i in range(len(world)):
# 		for j in range(len(world[0])):
# 			if world[i][j] == '.':
# 				SCREEN.blit(grass, (i*64, j*64))
# 			elif world[i][j] == 'T':
# 				SCREEN.blit(tree, (i*64, j*64))
# 			else:
# 				pass
# 	SCREEN.blit(avatar_dict[matt.direction], (matt.x*64, (768 -matt.y*64)))
# 	SCREEN.blit(label, (300,300))
# 	pygame.display.flip()