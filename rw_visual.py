import matplotlib.pyplot as plt

from random_walk import RandomWalk




while True:
	fig, ax = plt.subplots(figsize=(10,8))
	rw = RandomWalk(5_000)
	rw.fill_walk()

	ax.scatter(rw.x_values,rw.y_values,s=15,edgecolors='none',c=range(rw.num_points),cmap=plt.cm.plasma)
	ax.scatter(rw.x_values[0],rw.y_values[0],s=100,c='green',edgecolors='none')
	ax.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='red',edgecolors='none')

	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()
	ending = input("Press 'n' to quit, any other key to continue")
	if ending == 'n':
		break