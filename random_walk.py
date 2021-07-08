from random import choice


class RandomWalk:

	def __init__(self,num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self,steps=100):

		while len(self.x_values) < self.num_points:

			x_step = self.get_step()
			y_step = self.get_step()
			
			if x_step == 0 and y_step == 0:
				continue
			
			self.x_values.append(self.x_values[-1] + x_step)
			self.y_values.append(self.y_values[-1] + y_step)

	def get_step(self):
		x_direction = choice([1,-1])
		x_move = choice([0,1,2,3,4])
		return  x_move * x_direction 


