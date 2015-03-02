"""
Testing whether a variable can be mapped to a function in a dictionary. 
"""


import random, sys

game_flag = True

class player:
	def __init__(self):
		self.inventory = []
		self.max_hp = 5
		self.hp = 5
		self.x = 0
		self.y = 0
		self.direction = 0


	def turn_left(self):
		"""  0
		   3 + 1
		     2
		     """
		self.direction = (self.direction - 1)%4


	def turn_right(self):
		self.direction = (self.direction + 1)%4


	def move_forward(self):
		if self.direction == 0:
			self.y += 1
		elif self.direction == 1:
			self.x += 1
		elif self.direction == 2:
			self.y -= 1
		elif self.direction == 3:
			self.x -= 1


def add_one(num):
	return num+1



test_function_dict = {}
test_function_dict['up'] = add_one
delta = test_function_dict['up'](1)
print delta
