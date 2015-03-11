"""
This module creates the object type Block, and several subfunctions which 
generate specific varieties of the Block class.
"""

import pygame


class Block(object):
	'''Hold all the data about '''
	graphics_names = ['tree.png', 'water.png', 'grass.png', 'dirt.png', 'wood.png', 'water.png']
	Graphics = {item: pygame.image.load('graphics/' + item) for item in graphics_names}
	def __init__(self, name, graphic, walkable=True, destructible=False, drop=None):
		"""
		Defines the Block objecct type.
		"""
		self.name = name
		self.graphic = graphic #Filename for the block's image
		self.walkable = walkable #Whether the player can move on top of the block
		self.destructible = destructible #Whether or not a block can be mined
		self.drop = drop #What is added to the player inventory if the block is mines

	def __str__(self):
		return self.name

	def loadgraphic(self):
		'''loads the pygame image that is supposed to represent a block'''
		return Block.Graphics[self.graphic]



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