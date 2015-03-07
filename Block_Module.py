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
		self.graphic = graphic
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop

	def __str__(self):
		return self.name

	def loadgraphic(self):
		return pygame.image.load('graphics/' + self.graphic)



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