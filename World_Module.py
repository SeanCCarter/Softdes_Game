"""This Module creates the methods for creating, saving, and interacting with a World"""

from Block_Module import *
from pickle import dump, load

class World(object):

	def __init__(self, seed, chunk_width = 20, chunk_height = 20):
		'''Creates the basic information about the world'''
		#Todo: use a seed to generate the world
		self.chunk_width = chunk_width
		self.chunk_height = chunk_height
		self.chunk_list = []
		self.loaded_world = {}
		self.create_world()

	def load_world(self, center_chunkx, center_chunky):

	def create_world(self):
		'''creates a 3x3 series of chunks'''
		for i in xrange(-3, 4):
			for j in xrange(-3, 4):
				self.chunk_list.append((i,j))
				self.loaded_world[(i,j)] = Chunk(self.chunk_width, self.chunk_height, (i,j))


class Chunk(object):
	'''A chunk is an x_size by y_size array of block values'''

	def __init__(self, x_size, y_size, location, load = False):
		#Self.location should be a tuple (x,y), although it isn't used yet.
		self.location = location
		chunk = make_blank_world(x_size, y_size)
		if not load:
			for i in range(x_size):
				for j in range(y_size):
					seed = random.random()
					if check_surroundings(i, j, 'water'):
						if seed >= 0.8:
							chunk[i][j] = water()
						elif seed >= 0.6:
							chunk[i][j] = tree()
						else:
							chunk[i][j] = grass()
					elif not check_surroundings(i, j, 'tree'):
						if seed >= 0.5:
							chunk[i][j] = tree()
						else:
							chunk[i][j] = grass()
					else:
						chunk[i][j] = grass()
			self.chunk = [row[:y_size+1] for row in chunk[:x_size+1]]
		else:
			filename = "("+str(self.location[0])+str(self.location[1])+").txt"
			data_file = open(filename, "r")
			self.chunk = load(data_file)
			data_file.close()


	def save_data(self):
		filename = "("+str(self.location[0])+str(self.location[1])+").txt"
		data_file = open(filename, "w")
		dump(self.chunk)
		data_file.close()


	#Not reallly functions for the class. Not really sure where to put it yet.
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

	def make_blank_world(x_size, y_size):
		"""
		Creates an x-by-y list of lists of zeroes.
		"""
		blank_array = [[block('grass','grass',False,False) for j in range(y_size + 1)] for i in range(x_size + 1)]
		return blank_array

