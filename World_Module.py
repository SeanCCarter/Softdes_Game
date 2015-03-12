"""This Module creates the methods for creating, saving, and interacting with a World"""

import random
import pygame
from Block_Module import *
from Misc_Module import *
from pickle import dump, load

class World(object):

	def __init__(self, seed = 0, chunk_width = 11, chunk_height = 11):
		'''Creates the basic information about the world'''
		#Todo: use a seed to generate the world
		self.chunk_width = chunk_width
		self.chunk_height = chunk_height
		self.center_chunk = [0,0]
		self.chunk_list = []
		self.loaded_world = {}
		self.create_world()

	def get_displayed_world(self, player_position, dx_range, dy_range):
		'''Returns a list of lists of display objects for pygame, which will later be blitted to the screen'''
		self.load_world(player_position)
		#print 'get_displayed_world did something'
		return [[self.get_square(player_position, dx, dy).loadgraphic() for dx in xrange(dx_range[0], dx_range[1]+1)] for dy in xrange(dy_range[0], dy_range[1]+1)]
		
	def get_square(self, player_position, dx, dy):
		'''Returns the block dx distance and dy distance from the player's square'''

		position = relative_position(player_position, dx, dy, self.chunk_width, self.chunk_height)
		block_chunk = position[0] #the block where the chunk should be located
		x = position[1] #x location where the block should be located
		y = position[2] #y location where the block should be located

		#print 'get_square did something!'
		return self.loaded_world[block_chunk].get_block(x,y)

	def change_square(self, player_position, dx, dy, block):
		'''When the player mines or places blocks, this function is used to change the world's square to the new one'''

		position = relative_position(player_position, dx, dy, self.chunk_width, self.chunk_height)
		block_chunk = position[0] #the chunk where the block should be located
		x = position[1] #x location where the block should be located
		y = position[2] #y location where the block should be located

		self.loaded_world[block_chunk].change_block(x,y, block)


	def load_world(self, player_position):
		''' Checks the player position to see if the player is in the central chunk. If not, saves 
			the chunks which are out of range, and loads new ones.'''
		#Get the coordinates of the chunk the player is in
		player_chunkx = player_position[0][0]
		player_chunky = player_position[0][1]
		center_chunkx = self.center_chunk[0]
		center_chunky = self.center_chunk[1]

		#If the player has moved up, out of the center chunk
		if player_chunky > center_chunky:
			for x in xrange(center_chunkx-1, center_chunkx+2):
				self.loaded_world[(x, center_chunky-1)].save_data() #Saves the bottom three chunks
				del(self.loaded_world[(x, center_chunky-1)]) #deletes them
				self.loaded_world[(x, center_chunky+2)] = self.load_chunk(self.chunk_width, self.chunk_height, (x, center_chunky+2)) #Adds 3 new chunks on top
			self.center_chunk[1] += 1

		#If the player has moved down, out of the center chunk
		elif player_chunky < center_chunky:
			for x in xrange(center_chunkx-1, center_chunkx+2):
				self.loaded_world[(x, center_chunky+1)].save_data() #Saves the top three chunks
				del(self.loaded_world[(x, center_chunky+1)]) #delets them
				self.loaded_world[(x, center_chunky-2)] = self.load_chunk(self.chunk_width, self.chunk_height, (x, center_chunky-2)) #Adds 3 new chunks on bottom
			self.center_chunk[1] -= 1

		#If the player has moved right, out of the center chunk
		elif player_chunkx > center_chunkx:
			for y in xrange(center_chunky-1, center_chunky+2):
				self.loaded_world[(center_chunkx-1,y)].save_data() #Saves the left three chunks
				del self.loaded_world[(center_chunkx-1,y)] #deletes them
				self.loaded_world[(center_chunkx+2, y)] = self.load_chunk(self.chunk_width, self.chunk_height, (center_chunkx+2, y)) #Adds 3 chunks to the right
			self.center_chunk[0] += 1

		#If the player has moved left, out of the center chunk
		elif player_chunkx < center_chunkx:
			for y in xrange(center_chunky-1, center_chunky+2):
				self.loaded_world[(center_chunkx+1,y)].save_data() #Saves the rightmost three chunks
				del self.loaded_world[(center_chunkx+1,y)] #deletes them
				self.loaded_world[(center_chunkx-2, y)] = self.load_chunk(self.chunk_width, self.chunk_height, (center_chunkx-2, y)) #Adds 3 on left
			self.center_chunk[0] -= 1


	def create_world(self):
		'''creates a 3x3 dictionary of chunks'''
		for i in xrange(-1, 2):
			for j in xrange(-1, 2):
				self.chunk_list.append((i,j))
				self.loaded_world[(i,j)] = Chunk(self.chunk_width, self.chunk_height, (i,j))

	def load_chunk(self, x_size, y_size, location):
		if location in self.chunk_list: #Checks to see whether there is already a file for that chunk
			return Chunk(x_size, y_size, location, True)
		else:
			self.chunk_list.append(location)
			return Chunk(x_size, y_size, location)


class Chunk(object):
	'''A chunk is an x_size by y_size array of block values'''

	def __init__(self, x_size, y_size, location, loadable = False):
		#Self.
		#Self.location should be a tuple (x,y)
		self.location = location
		self.chunk = make_blank_world(x_size, y_size)
		self.chunk[random.randint(2, x_size-2)][random.randint(2, y_size-2)] = Water() #chooses a random place to be water
		if not loadable:
			#This is our algorithm for generating a chunk. It's semi-rendom, but not partucularly interesting. Mostly it stops trees from getting too
			#close together, and tries to group water if it can. Blank tiles act like water tiles.
			for i in range(x_size-1):
				for j in range(y_size-1):
					seed = random.random()
					if self.check_surroundings(i, j, 'water'):
						if seed >= 0.8:
							self.chunk[i][j] = Water()
						elif seed >= 0.6:
							self.chunk[i][j] = Tree()
						else:
							self.chunk[i][j] = Grass()
					elif not self.check_surroundings(i, j, 'tree'):
						if seed >= 0.5:
							self.chunk[i][j] = Tree()
						else:
							self.chunk[i][j] = Grass()
					else:
						self.chunk[i][j] = Grass()
			self.chunk = [row[:y_size+1] for row in self.chunk[:x_size+1]]
			self.save_data()
		else:
			filename = "./chunks/("+str(self.location[0])+","+str(self.location[1])+").txt"
			data_file = open(filename, "r")
			self.chunk = load(data_file)
			data_file.close()


	def save_data(self):
		filename = "./chunks/("+str(self.location[0])+","+str(self.location[1])+").txt"
		data_file = open(filename, "w")
		dump([row for row in self.chunk], data_file) #Saves itself as a list of lists
		data_file.close()


	def get_block(self,x,y):
		'''returns the block object at x, y'''
		return self.chunk[x][y]


	def change_block(self,x,y,block):
		'''replaces the block at x, y'''
		self.chunk[x][y] = block


	def check_surroundings(self,x_coord, y_coord, value):
		"""
		If the variable world has already been defined, it checks all x and y coords within one square (aka, checks the 8 surrounding squares) for a given value. If that value is present in 1 or more squares, returns True; else, False.
		"""
		for i in range(3):
			for j in range(3):
				examining = self.chunk[x_coord - 1 + i][y_coord - 1 + j]
				if examining.name == value:
					return True
		return False

#Not reallly functions for the class. Not really sure where to put it yet.
def make_blank_world(x_size, y_size):
	"""
	Creates an x-by-y list of lists blank objects.
	"""
	blank_array = [[Blank() for j in range(y_size)] for i in range(x_size)]
	return blank_array

