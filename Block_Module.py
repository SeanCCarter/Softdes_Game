'''This Module defines what a block is, and the different types of blocks'''

class block(object):
	def __init__(self, name, block_type, walkable=True, destructible=False, drop=[]):
		"""
		creates an object with a given ID. Python doesn't exactly have a case structure, so... elifs?
		"""
		self.name = name
		self.graphic = pygame.image.load('{0}.png'.format(block_type))
		self.walkable = walkable
		self.destructible = destructible
		self.drop = drop