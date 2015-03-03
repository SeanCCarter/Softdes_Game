class player(object):
	def __init__(self):
		self.inventory = {}
		self.hp = 5

	def add_to_inventory(self, item):
		if item in self.inventory:
			self.inventory[item] += 1
		else:
			self.inventory[item] = 1

	def remove_from_inventory(self, item):
		if item in self.inventory:
			self.inventory[item] -= 1
			if self.inventory[item] == 0:
				del self.inventory[item]
		else:
			print 'You tried to use something you don\'t have!'

matt = player()

matt.add_to_inventory('wood')
print matt.inventory['wood']

matt.add_to_inventory('wood')
print matt.inventory['wood']

matt.remove_from_inventory('wood')
print matt.inventory['wood']

matt.remove_from_inventory('wood')

matt.remove_from_inventory('wood')