"""
This Module contains all of the atributes and methods of the player
"""
import pygame
from World_Module import *

class Player(object):
	def __init__(self, chunk = (0,0), x = 0, y =0):
		self.inventory = {}
		self.max_hp = 5
		self.hp = 5
		self.position = [chunk, x, y]
		self.direction = 1
		self.avatar_up = pygame.image.load('graphics/up_avatar.png')
		self.avatar_right = pygame.image.load('graphics/right_avatar.png')
		self.avatar_down = pygame.image.load('graphics/down_avatar.png')
		self.avatar_left = pygame.image.load('graphics/left_avatar.png')
		self.direction_to_graphic = {0: self.avatar_up, 1: self.avatar_right, 2: self.avatar_down, 3: self.avatar_left}
		self.current_avatar = self.direction_to_graphic[self.direction]


	def __str__(self):
		return "("+str(self.position[0][0])+","+str(self.position[0][1])+")"+" "+str(self.position[1])+","+str(self.position[2])


##################################################################
#################### Change Player attributes ####################
##################################################################
	def turn_left(self, world):
		"""  Rotates character counter-clockwise.
			 The direction works like this:
			 0
		   3 + 1
		     2
		     It's just modular arithmetic. If you add 4, it stays the same.
		     """
		self.direction = (self.direction - 1)%4
		self.current_avatar = self.direction_to_graphic[self.direction]



	def turn_right(self, world):
		'''Rotates character clockwise'''
		self.direction = (self.direction + 1)%4
		self.current_avatar = self.direction_to_graphic[self.direction]


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


##################################################################
################### Interact with the World ######################
##################################################################
	def block_in_front(self, world):
		'''Returns the block object in front of the player'''
		return world.get_square(self.position, block_front_direction[self.direction][0],block_front_direction[self.direction][1])


	def block_behind(self, world):
		'''Returns the block object behind the player'''
		return world.get_square(self.position, -block_front_direction[self.direction][0], -block_front_direction[self.direction][1])


	def update_position(self, world, dx, dy):
		"""
		Sets the player's position to the block dx and dy from the player's current position.
		"""
		self.position = relative_position(self.position, dx, dy, world.chunk_width, world.chunk_height)


	def move_forward(self, world):
		if self.block_in_front(world).walkable:
			self.update_position(world, block_front_direction[self.direction][0],block_front_direction[self.direction][1])


	def move_backward(self, world):
		if self.block_behind(world).walkable:
			self.update_position(world, -block_front_direction[self.direction][0], -block_front_direction[self.direction][1])


	def mine(self, world):
		'''Removes whatever block is in front of the player, and replaces it with dirt'''
		if self.block_in_front(world).destructible:
			self.add_to_inventory(self.block_in_front(world).drop)
			world.change_square(self.position, block_front_direction[self.direction][0],block_front_direction[self.direction][1], Dirt())


	def place(self, world, item=Wood):
		'''Changes a block in the world to one that the player carries'''
		if item not in self.inventory:
			return False
		else:
			world.change_square(self.position, block_front_direction[self.direction][0],block_front_direction[self.direction][1], item())
			self.remove_from_inventory(item)


##################################################################
##################### Save and Load Data #########################
##################################################################
	def save_data(self):
		''' Player objects cannot be pickled, so this returns a list of all relavent data,
			to be loaded back into the player when the world is loaded
		'''
		return [self.position, self.direction, self.inventory, self.hp]


	def load_data(self, saved_data):
		'''Takes in the information from save_data, and resets the player attributes appropriately'''
		self.position = saved_data[0]
		self.direction = saved_data[1]
		self.inventory = saved_data[2]
		self.hp = saved_data[3]


#These directions encode the dx and dy from the player.
#In otherwords, whether to add a positive or negative to
#the x and y of the player position
block_front_direction = {}
block_front_direction[0] = (0,-1) #up
block_front_direction[1] = (1,0) #right
block_front_direction[2] = (0,1) #down
block_front_direction[3] = (-1,0) #left


