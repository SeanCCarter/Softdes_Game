''''This Module contains all of the atributes and methods of the player'''
import pygame
from World_Module import *

class Player(object):
	def __init__(self, chunk = (0,0), x = 0, y =0):
		self.inventory = {}
		self.max_hp = 5
		self.hp = 5
		self.position = [chunk, x, y]
		self.direction = 1

	def __str__(self):
		return "("+str(self.position[0][0])+","+str(self.position[0][1])+")"+" "+str(self.position[1])+","+str(self.position[2])


	def avatar(self):
		'''returns a pygame image based on current direction'''
		return avatar_dict[self.direction]


	def turn_left(self, world):
		"""  0
		   3 + 1
		     2
		     """
		self.direction = (self.direction - 1)%4


	def turn_right(self, world):
		self.direction = (self.direction + 1)%4


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
		if item in self.inventory:
			return True
		else:
			return False

	def block_in_front(self, world):
		return world.get_square(self.position, block_front_direction[self.direction][0],block_front_direction[self.direction][1])

	def block_behind(self, world):
		return world.get_square(self.position, -block_front_direction[self.direction][0], -block_front_direction[self.direction][1])

	def update_position(self, world, dx, dy):
		'''Returns the block x distance and y distance from the player's square'''
		block_chunk = self.position[0] #the current chunk
		x = self.position[1]
		y = self.position[2]
		#Updates the player location based on dx and dy
		if x + dx < 0:
			block_chunk = (block_chunk[0]-1, block_chunk[1])
			x = world.chunk_width + dx + x 
		elif x + dx > (world.chunk_width-1):
			block_chunk = (block_chunk[0]+1, block_chunk[1])
			x = (dx + x)%world.chunk_width
		if y + dy < 0:
			block_chunk = (block_chunk[0], block_chunk[1]-1)
			y = world.chunk_height + dy + y 
		elif y + dy > (world.chunk_height-1):
			block_chunk = (block_chunk[0], block_chunk[1]+1)
			y = (dy + y)%world.chunk_height

		self.position = [block_chunk, x, y]

	def move_forward(self, world):
		if self.block_in_front(world).walkable:
			self.update_position(world, block_front_direction[self.direction][0],block_front_direction[self.direction][1])

	def move_backward(self, world):
		if self.block_behind(world).walkable:
			self.update_position(world, -block_front_direction[self.direction][0], -block_front_direction[self.direction][1])

up_arrow = pygame.image.load('up_arrow.png')
right_arrow = pygame.image.load('right_arrow.png')
down_arrow = pygame.image.load('down_arrow.png')
left_arrow = pygame.image.load('left_arrow.png')

avatar_dict = {}
avatar_dict[0] = up_arrow
avatar_dict[1] = right_arrow
avatar_dict[2] = down_arrow
avatar_dict[3] = left_arrow
block_front_direction = {}
block_front_direction[0] = (0,1)
block_front_direction[1] = (1,0)
block_front_direction[2] = (0,-1)
block_front_direction[3] = (-1,0)