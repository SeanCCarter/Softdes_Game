"""This Module creates the methods for creating, saving, and interacting with a World"""

from Block_Module import *
from pickle import dump, load

class World(object):

	def __init__(self, seed, chunk_width = 11, chunk_height = 11):
		'''Creates the basic information about the world'''
		#Todo: use a seed to generate the world
		self.chunk_width = chunk_width
		self.chunk_height = chunk_height
		self.chunk_list = []
		self.loaded_world = {}
		self.create_world()

	def get_displayed_world(self, player_position, xsize, ysize):
		self.load_world(player_position)
		return [[self.get_square(player_position, dx, dy) for dx in xrange(-xsize/2, xsize/2+1)] for dy in xrange(-ysize/2, ysize/2+1)]]

	def get_square(self, player_position, dx, dy):
		'''Returns the block x distance and y distance from the player's square'''
		block_chunk = player_position[0] #the block where the chunk should be located
		x = player_position[1] #x location where the block should be located
		y = player_position[2] #y location where the block should be located

		#Updates the block location based on dx and dy
		if x + dx < 0:
			block_chunk[0] -= 1
			x = self.chunk_width + dx + x 
		elif x + dx > (self.chunk_width-1):
			block_chunk[0] += 1
			x = (dx + x)%self.chunk_width
		if y + dy < 0:
			block_chunk[1] -= 1
			y = self.chunk_height + dy + y 
		elif y + dy > (self.chunk_height-1):
			block_chunk[1] += 1
			y = (dy + y)%self.chunk_height

		return self.loaded_world[block_chunk].get_block(x,y)

	def change_square(self, player_position, dx, dy, block):
		'''When the player mines or places blocks, this function is used to change the world's square to the correct one'''
		block_chunk = player_position[0] #the block where the chunk should be located
		x = player_position[1] #x location where the block should be located
		y = player_position[2] #y location where the block should be located

		#Updates the block location based on dx and dy
		if x + dx < 0:
			block_chunk[0] -= 1
			x = self.chunk_width + dx + x 
		elif x + dx > (self.chunk_width-1):
			block_chunk[0] += 1
			x = (dx + x)%self.chunk_width
		if y + dy < 0:
			block_chunk[1] -= 1
			y = self.chunk_height + dy + y 
		elif y + dy > (self.chunk_height-1):
			block_chunk[1] += 1
			y = (dy + y)%self.chunk_height

		self.loaded_world[block_chunk].change_block(x,y, block)


	def load_world(self, player_position):
		''' Checks the player position to see if the player is in the central chunk. If not, saves 
			the chunks which are out of range, and loads new ones.'''
		#Get the coordinates of the chunk the player is in
		centerx = player_position[0][0]
		centery = player_position[0][1]

		#Player has moved up, out of current center chunk
		if (centerx, centery + 1) not in self.loaded_world:
			#Save all of the chunks behind you, and remove them from memory
			for i in xrange(centerx-1, centerx+2):
				self.loaded_world[(i, centery-2)].save_data()
				del self.loaded_world[(i, centery-2)]
				#Add the new row of chunks
				if (i, centery+1) in self.chunk_list:
					self.loaded_world[(i, centery+1)] = Chunk(self.chunk_width, self.chunk_height, (i, centery+1), True)
				else:
					self.loaded_world[(i, centery+1)] = Chunk(self.chunk_width, self.chunk_height, (i, centery+1))

		#Player has moved downwards, out of current chunk
		elif (centerx, centery - 1) not in self.loaded_world:
			#Save all of the chunks behind you, and remove them from memory
			for i in xrange(centerx-1, centerx+2):
				self.loaded_world[(i, centery+2)].save_data()
				del self.loaded_world[(i, centery+2)]
				#Add the new row of chunks
				if (i, centery-1) in self.chunk_list:
					self.loaded_world[(i, centery-1)] = Chunk(self.chunk_width, self.chunk_height, (i, centery-1), True)
				else:
					self.loaded_world[(i, centery-1)] = Chunk(self.chunk_width, self.chunk_height, (i, centery-1))

		#Player has moved to the right, out of current chunk
		elif (centerx + 1, centery) not in self.loaded_world:
			#Save all of the chunks behind you, and remove them from memory
			for j in xrange(centery-1, centery+2):
				self.loaded_world[(centerx-2, j)].save_data()
				del self.loaded_world[(centerx-2, j)]
				#Add the new row of chunks
				if (centerx+1, j) in self.chunk_list:
					self.loaded_world[(centerx+1, j)] = Chunk(self.chunk_width, self.chunk_height, (centerx+1, j), True)
				else:
					self.loaded_world[(centerx+1, j)] = Chunk(self.chunk_width, self.chunk_height, (centerx+1, j))

		#Player has moved to the left, out of current chunk
		elif (centerx - 1, centery) not in self.loaded_world:
			#Save all of the chunks behind you, and remove them from memory
			for j in xrange(centery-1, centery+2):
				self.loaded_world[(centerx+2, j)].save_data()
				del self.loaded_world[(centerx+2, j)]
				#Add the new row of chunks
				if (centerx-1, j) in self.chunk_list:
					self.loaded_world[(centerx-1, j)] = Chunk(self.chunk_width, self.chunk_height, (centerx-1, j), True)
				else:
					self.loaded_world[(centerx-1, j)] = Chunk(self.chunk_width, self.chunk_height, (centerx-1, j))


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
			self.save_data()
		else:
			filename = "./chunks/("+str(self.location[0])+str(self.location[1])+").txt"
			data_file = open(filename, "r")
			self.chunk = load(data_file)
			data_file.close()


	def save_data(self):
		filename = "("+str(self.location[0])+str(self.location[1])+").txt"
		data_file = open(filename, "w")
		dump(self.chunk)
		data_file.close()


	def get_block(x,y):
		return self.chunk[x][y]


	def change_block(x,y,block):
		self.chunk[x][y] = block


	#Not reallly functions for the class. Not really sure where to put it yet.
	def check_surroundings(self, x_coord, y_coord, value):
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

	def make_blank_world(self, x_size, y_size):
		"""
		Creates an x-by-y list of lists of zeroes.
		"""
		blank_array = [[block('grass','grass',False,False) for j in range(y_size + 1)] for i in range(x_size + 1)]
		return blank_array

