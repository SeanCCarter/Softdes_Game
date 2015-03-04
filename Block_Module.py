'''
This Module defines what a block is, and the different types of blocks.
'''

import pygame


class block(object):
	def __init__(self, name, graphic, walkable=True, destructible=False, drop=[]):
		"""
		creates an object with a given name, graphic, etc. Python doesn't exactly have a case structure, so... elifs?
		"""
		self.name = name
		self.graphic = pygame.image.load(os.path.join(graphic))
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop


class tree(block):
	def __init__(self):
		block.__init__(self, 'tree', 'tree.png', False, True, wood)


class water(block):
	def __init__(self):
		block.__init__(self,'water', 'water.png', False, False)


class grass(block):
	def __init__(self):
		block.__init__(self,'grass', 'grass.png', True, False)


class dirt(block):
	def __init__(self):
		block.__init__(self,'dirt', 'dirt.png', True, False)


class wood(block):
	def __init__(self):
		block.__init__(self,'wood', 'wood.png', False, True, wood)


class blank(block):
	def __init__(self):
		block.__init__(self, 'blank', 'water.png', False, False)
