'''The functions here are made to provide some qualitative tests of the modules made for the final function.'''

import random
import sys
import pygame
from World_Module import *
from Player_Module import *
from Block_Module import *
from Misc_Module import *

def test_chunk():
	chunk = Chunk(11,11, (0,0))
	for item in chunk.chunk:
		for block in item:
			print block



def display_chunk():
	pygame.init()
	SCREEN = pygame.display.set_mode((64*12,64*12))
	font = pygame.font.SysFont("Arial",30)
	chunk = Chunk(11,11, (0,0))

	for item in chunk.chunk:
		for block in item:
			print block

	exit_flag = False
	while not exit_flag:

		visible_world = [[block.loadgraphic() for block in row] for row in chunk.chunk]

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_flag = True

		for i in range(len(visible_world)):
			for j in range(len(visible_world[0])):
				SCREEN.blit(visible_world[i][j], (i*64, j*64))

		pygame.display.flip()

def position_tester():
	position = [(0,0), 0, 0]
	pygame.init()
	SCREEN = pygame.display.set_mode((64*11,64*11))
	font = pygame.font.SysFont("Arial",30)
	chunk = Chunk(11,11, (0,0))

	exit_flag = False
	while not exit_flag:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_flag = True

				elif event.key == pygame.K_UP:
					position = relative_position(position, 0, 1, 9, 13)
					print position
				elif event.key == pygame.K_DOWN:
					position = relative_position(position, 0, -1, 9, 13)
					print position
				elif event.key == pygame.K_RIGHT:
					position = relative_position(position, 1, 0, 9, 13)
					print position
				elif event.key == pygame.K_LEFT:
					position = relative_position(position, -1, 0, 9, 13)
					print position

		visible_world = [[block.loadgraphic() for block in row] for row in chunk.chunk]
		for i in range(len(visible_world)):
			for j in range(len(visible_world[0])):
				SCREEN.blit(visible_world[i][j], (i*64, j*64))

		pygame.display.flip()



position_tester()
