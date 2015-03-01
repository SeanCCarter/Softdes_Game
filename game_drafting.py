"""
whoop whoop
orthogonal terraria here we goooooo

"""

import pygame as pg

pg.init()

game_flag = True

class player:
	def __init__(self):
		self.inventory = []
		self.max_hp = 5
		self.hp = 5

class block:
	def __init__(self, block_id):
		"""
		creates an object with a given ID. Python doesn't exactly have a case structure, so... elifs?
		"""
		pass

turn_count = 1

matt = player()

while game_flag == True:
	pass