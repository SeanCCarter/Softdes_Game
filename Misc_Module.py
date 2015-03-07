"""This Module contains functions that I don't know where to put anywhere else, that are usable in all modules"""

def relative_position(position, dx, dy, xsize, ysize):
	'''Returns the block x distance and y distance from the player's square'''
	block_chunk = position[0] #the current chunk
	x = position[1]
	y = position[2]
	#Updates the player location based on dx and dy
	if x + dx < 0:
		block_chunk = (block_chunk[0]-1, block_chunk[1])
		x = xsize + dx + x 
	elif x + dx > (xsize-1):
		block_chunk = (block_chunk[0]+1, block_chunk[1])
		x = (dx + x)%xsize
	else:
		x = x + dx

	if y + dy < 0:
		block_chunk = (block_chunk[0], block_chunk[1]-1)
		y = ysize + dy + y 
	elif y + dy > (ysize-1):
		block_chunk = (block_chunk[0], block_chunk[1]+1)
		y = (dy + y)%ysize
	else:
		y = y + dy
		
	return [block_chunk, x, y]