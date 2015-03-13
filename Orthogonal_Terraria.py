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
		self.inventory_font = pygame.font.SysFont("Arial",20)
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
			self.render_inventory()
			pygame.display.flip()

	def render_inventory(self):
		'''Renders player inventory to the current gameinstance screen'''
		inventory = self.player.get_inventory()
		starting_location = (60, 60) #Top left corner of the inventory screen

		pygame.draw.rect(self.SCREEN, 
							 (255,0,255), #Draw purple back of inventory
							 (starting_location[0]-7,starting_location[1]-7,14+40*len(inventory),46), #Make the border 7 pixels
							 0) 
		if self.player.selected_inventory != None:
			pygame.draw.rect(self.SCREEN, 
							 (255,255,0), #Draw yellow square underneath selected inventory item
							 (starting_location[0]-3 + self.player.selected_inventory*40,starting_location[1]-3, 37 , 37), #Make border 3 pixels
							  0)
		for i, item in enumerate(inventory):
			graphic = item[0] #item to blit
			number = item[1] #how many of the item there are
			label = self.inventory_font.render(str(number),1,(0,0,0)) #Shows the player how many of an item they have
			self.SCREEN.blit(graphic, (starting_location[0] + 40*i, starting_location[1]))
			self.SCREEN.blit(label, (starting_location[0] + 40*i, starting_location[1]))

	def exit(self):
		'''Saves all data, and shuts down pygame'''
		worldfile = open('./chunks/' + self.worldname, 'w')
		dump([self.world, self.player.save_data()], worldfile)
		worldfile.close()
		pygame.quit()


def main():
	Game = Game_Instance(loadworld = True)
	Game.play()
	Game.exit()


if __name__ == '__main__':
	main()
