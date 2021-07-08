from random import randint 
class Die:
	def __init__(self,sides=6):
		self.sides = sides

	def roll(self):
		return randint(1,self.sides)


if __name__ == '__main__':
	die = Die(12)
	print(f"Rzucam kostką {die.sides}-ścienną: {die.roll()}")