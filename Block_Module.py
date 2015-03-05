"""
This module creates the object type Block, and several subfunctions which 
generate specific varieties of the Block class.
"""

import pygame


class Block(object):
	def __init__(self, name, graphic, walkable=True, destructible=False, drop=[]):
		"""
		Defines the Block objecct type.
		"""
		self.name = name
		self.graphic = pygame.image.load(graphic)
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop





"""
These functions return a distinct block with specific parameters.
"""

def Tree():
	return Block('tree', 'tree.png', False, True, Wood)

def Water():
	return Block('water', 'water.png', False, False)

def Grass():
	return Block('grass', 'grass.png', True, False)

def Dirt():
	return Block('dirt', 'dirt.png', True, False)

def Wood():
	return Block('wood', 'wood.png', False, True, Wood)

def Blank():
	return Block('blank', 'water.png', False, False)



pygame.init()
SCREEN = pygame.display.set_mode((768,768))

test_tree = Tree()
print test_tree.graphic
exit_flag = False

while not exit_flag:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit_flag = True
		for i in range(12):
			for j in range(12):
				SCREEN.blit(test_tree.graphic, (64*i, 64*j))