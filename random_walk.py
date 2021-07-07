from random import choice


class RandomWalk:

	def __init__(self,num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self,steps=100):

		while len(self.x_values) < self.num_points:
			x_direction = choice([1,-1])
			x_step = choice([0,1,2,3,4])

			y_direction = choice([1,-1])
			y_step = choice([0,1,2,3,4])
			
			if x_step == 0 and y_step == 0:
				continue

			x_move = x_step * x_direction 
			x = self.x_values[-1] + x_move
			
			y_move = y_step * y_direction
			y = self.y_values[-1] + y_move

			self.x_values.append(x)
			self.y_values.append(y)
