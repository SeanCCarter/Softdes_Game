'''This is the code that actually runs the modules for orthoganal terarria
	-Sean
'''

"""
whoop whoop
orthogonal terraria here we goooooo
	-Mat
"""

import random
import sys
import pygame
from World_Module import *
from Player_Module import *
from Block_Module import *


def main():
	pygame.init()
	SCREEN = pygame.display.set_mode((64*11,64*11))
	font = pygame.font.SysFont("Arial",30)

	world = World(chunk_width = 11, chunk_height = 11)
	player = Player((0,0), 0, 0)
	key_to_function_dict = {pygame.K_UP: player.move_forward, pygame.K_LEFT: player.turn_left, pygame.K_RIGHT: player.turn_right, pygame.K_DOWN: player.move_backward}
	
	exit_flag = False
	while not exit_flag:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_flag = True
				if event.key in key_to_function_dict:
					key_to_function_dict[event.key](world)
				if event.key == pygame.K_LSHIFT:
					matt.place(wood)

		label = font.render(str(player),1,(0,0,0))
		SCREEN.fill((255,255,255))

		visible_world = world.get_displayed_world(player.position, 11, 11)
		for i in range(len(visible_world)):
			for j in range(len(visible_world)):
				SCREEN.blit(visible_world[i][j], (i*64, j*64))
		SCREEN.blit(player.avatar(), (6*64, 6*64))
		SCREEN.blit(label, (300,300))
		pygame.display.flip()


if __name__ == '__main__':
	main()