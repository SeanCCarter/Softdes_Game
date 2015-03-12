'''This is the code that actually runs the modules for orthogonal terraria
	-Sean
'''

"""
whoop whoop
orthogonal terraria here we goooooo
	-Mat
"""

import random
# import sys
import pygame
from pickle import dump, load
from World_Module import *
from Player_Module import *
from Block_Module import *
from Controller_Module import *

class Game_Instance(object):

	def __init__(self, worldname = 'world.txt', loadworld = False, worldsize = [19,15]):
		''' 
			Splits off all of the things that were in the main code associated with setting up the program.
			If you want to load a world, you set loadworld to true. To overwrite, set it to false.
		'''
		pygame.init()
		self.SCREEN = pygame.display.set_mode((64*worldsize[0],64*worldsize[1]))
		self.font = pygame.font.SysFont("Arial",30)
		self.worldname = worldname
		self.displayx = worldsize[0]/2 #width of the world on each side of the player
		self.displayy = worldsize[1]/2 #height of the world on each side of the player

		if loadworld == True:
			worldfile = open('./chunks/' + self.worldname, 'r')
			[self.world, player_attributes] = load(worldfile) #The player position is important, so it should be stored as well
			self.player = Player()
			self.player.load_data(player_attributes)
			self.player_controller = Arrow_Controller(self.player, self.world)
			worldfile.close()
		else:
			self.world = World(chunk_width = 12, chunk_height = 12)
			self.player = Player()
			self.player_controller = Arrow_Controller(self.player, self.world)


	def play(self):
		'''Runs the gameloop, using the things given in the setup'''
		while not self.player_controller.exit_flag:
			self.player_controller.process_events() #figures out what happens in the world
			label = self.font.render(str(self.player),1,(0,0,0)) #Renders the players position, for navigation
			self.SCREEN.fill((255,255,255))

			#This grabs the world around the player, and then renders the current screen
			visible_world = self.world.get_displayed_world(self.player.position, [-self.displayx,self.displayx], [-self.displayy,self.displayy])
			for i in range(len(visible_world)):
				for j in range(len(visible_world[0])):
					self.SCREEN.blit(visible_world[i][j], (j*64, i*64))
			self.SCREEN.blit(self.player.current_avatar, (self.displayx*64, self.displayy*64)) #Puts the player in the center of the screen
			self.SCREEN.blit(label, (300,300))
			pygame.display.flip()

	def exit(self):
		'''Saves all data, and shuts down pygame'''
		worldfile = open('./chunks/' + self.worldname, 'w')
		dump([self.world, self.player.save_data()], worldfile)
		worldfile.close()
		pygame.quit()

# def main():
# 	pygame.init()
# 	SCREEN = pygame.display.set_mode((64*19,64*15))
# 	font = pygame.font.SysFont("Arial",30)

# 	world = World(chunk_width = 10, chunk_height = 10)
# 	player1 = Player((0,0), 0, 0)
# 	player1_controller = Arrow_Controller(player1, world)

# 	while not player1_controller.exit_flag:
# 		player1_controller.process_events()
# 		# for event in pygame.event.get():
# 		# 	if event.type == pygame.KEYDOWN:
# 		# 		player1_controller.process_events()
# 		label = font.render(str(player1),1,(0,0,0))
# 		SCREEN.fill((255,255,255))

# 		visible_world = world.get_displayed_world(player1.position, [-9,9], [-7,7])
# 		for i in range(len(visible_world)):
# 			for j in range(len(visible_world[0])):
# 				SCREEN.blit(visible_world[i][j], (j*64, i*64))
# 		SCREEN.blit(player1.current_avatar, (9*64, 7*64))
# 		SCREEN.blit(label, (300,300))
# 		pygame.display.flip()
# 	pygame.quit()
# 	# sys.exit()

def main():
	Game = Game_Instance(loadworld = True)
	Game.play()
	Game.exit()


if __name__ == '__main__':
	main()
