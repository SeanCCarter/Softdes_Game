"""
Creates & otherwise defines the Controller class and its pygame-related functions.
-Matt; Mar. '15
"""

import pygame

class Controller():
	def __init__(self):
		self.key_pressed = False

	def process_events(self):
		"""
		Pumps and checks events; changes key_pressed to its corresponding value.
		"""
		pygame.event.pump()
		if pygame.key.get_pressed():
			self.key_pressed = 