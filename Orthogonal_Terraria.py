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
from World_Module import *
from Player_Module import *
from Block_Module import *
from Controller_Module import *

def main():
	pygame.init()
	SCREEN = pygame.display.set_mode((64*19,64*15))
	font = pygame.font.SysFont("Arial",30)

	world = World(chunk_width = 10, chunk_height = 10)
	player1 = Player((0,0), 0, 0)
	player1_controller = Arrow_Controller(player1, world)

	while not player1_controller.exit_flag:
		player1_controller.process_events()
		# for event in pygame.event.get():
		# 	if event.type == pygame.KEYDOWN:
		# 		player1_controller.process_events()
		# label = font.render(str(player1),1,(0,0,0))
		SCREEN.fill((255,255,255))

		visible_world = world.get_displayed_world(player1.position, [-9,9], [-7,7])
		for i in range(len(visible_world)):
			for j in range(len(visible_world[0])):
				SCREEN.blit(visible_world[i][j], (j*64, i*64))
		SCREEN.blit(player1.current_avatar, (9*64, 7*64))
		# SCREEN.blit(label, (300,300))
		pygame.display.flip()
	pygame.quit()
	# sys.exit()


if __name__ == '__main__':
	main()
