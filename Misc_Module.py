"""This Module contains functions that I don't know where to put anywhere else, that are usable in all modules"""

def relative_position(position, dx, dy, xsize, ysize):
	''' Returns the position x distance and y distance from the player's square,
		in the form [chunk, x, y]

		dx and dy are the distance from the player in the x and y directions
		xsize and ysize are the width and height of each chunk in the world
	'''
	block_chunk = position[0] #the current chunk
	x = position[1]
	y = position[2]
	
	if x + dx < 0: #If the position is to the left of the current chunk
		block_chunk = (block_chunk[0]-1, block_chunk[1])
		x = xsize + dx + x #Doesn't work if you try dx > either size variable
	elif x + dx > (xsize-1): #If the position is to the right
		block_chunk = (block_chunk[0]+1, block_chunk[1])
		x = (dx + x)%xsize #Adding one to a position at the chunk boundry makes the position 0, in the next chunk
	else:
		x = x + dx

	if y + dy < 0: #Position in chunk below
		block_chunk = (block_chunk[0], block_chunk[1]-1)
		y = ysize + dy + y 
	elif y + dy > (ysize-1): #Position in chunk above
		block_chunk = (block_chunk[0], block_chunk[1]+1)
		y = (dy + y)%ysize
	else:
		y = y + dy
		
	return [block_chunk, x, y]

