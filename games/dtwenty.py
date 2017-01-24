import random


class DTwenty:


	def __init__(self, player={}):
		self.stats = {
			'strength': 8,
			'intelligence': 8,
			'dexterity': 8,
			'wisdom': 8,
			'charisma': 8,
			'constitution': 8
		}
		self.role = None
		self.level = 1
		self.exp = 0

	def roll(self, rolls, dice):
		r = []
		for x in range(rolls):
			roll = random.randint(1, dice)
			r.append(roll)

		return r

	def fight(self, player):
		enemy = self.enemy()
		while enemy['health'] is not 0:
			enemy['health'] -= 1
			print(enemy['health'])

	def enemy(self, level=1, difficulty=1):
		# enemy health calculated 10 + level * difficulty
		stats = {
			'health': 10,
			'class': None,
			'dmg': 1
		}
		return stats

	def request_ally(self, ally):
		# request the aid of an ally
		pass

	def get_player(self):
		# get player stats
		pass
