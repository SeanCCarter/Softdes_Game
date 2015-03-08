"""
Creates & otherwise defines the Controller class and its pygame-related functions.
-Matt; Mar. '15

(The controller just maps a particular player to a particular set of keys/functions. This is chiefly of use for either custom names, or if multiple people play; hypothetically this could also be used to customize control schemes, though that's unlikely to happen in the duration of this particular project.)
"""

import pygame

class Controller():
	def __init__(self, dictionary, player):
		""" 
		Initiates the controller, with the dictionary mapping its keys to the corresponding functions.
		"""
		self.dictionary = dictionary
		self.player = player
		self.exit_flag = False

	def process_events(self):
		"""
		Pumps and checks events; changes key_pressed to its corresponding value.
		"""
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.exit_flag = True
				elif event.key in self.dictionary:
					function = self.dictionary[event.key]
					self.player.function()
