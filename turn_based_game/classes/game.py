import random

class bcolors:
	HEADER = '\033[95m'
	DKBLUE = '\033[94m'
	DKGREEN = '\033[92m'
	WARNING = '\033[91m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Person:
	def __init__(self, hp, mp, atk, df, magic):
		self.maxhp = hp
		self.hp = hp
		self.maxmp = mp
		self.mp = mp
		self.atkl = atk - 10
		self.atkh = atk + 10
		self.df = df
		self.magic = magic 
		self.actions = ["Attack", "Magic"]

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)