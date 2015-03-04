'''This Module defines what a block is, and the different types of blocks'''
import pygame

class block(object):
	def __init__(self, name, block_type, walkable=True, destructible=False, drop=[]):
		"""
		creates an object with a given ID. Python doesn't exactly have a case structure, so... elifs?
		"""
		self.name = name
		self.graphic_name = '{0}.png'.format(block_type)
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop

	def display_object(self):
		return pygame.image.load(self.graphic_name)

class tree(block):
	def __init__(self):
		block.__init__(self,'tree','tree',False,True,tree)


class water(block):
	def __init__(self):
		block.__init__(self,'water', 'water', False, False)


class grass(block):
	def __init__(self):
		block.__init__(self,'grass', 'grass', True, False)


class dirt(block):
	def __init__(self):
		block.__init__(self,'dirt', 'dirt', True, False)