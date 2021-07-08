import matplotlib.pyplot as plt

from random_walk import RandomWalk




while True:
	fig, ax = plt.subplots()
	rw = RandomWalk()
	rw.fill_walk()

	ax.scatter(rw.x_values,rw.y_values,s=15,edgecolors='none',c=range(1,5001),cmap=plt.cm.hot)
	ax.scatter(rw.x_values[0],rw.y_values[0],s=100,c='green',edgecolors='none')
	ax.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='red',edgecolors='none')

	plt.show()
	ending = input("Press 'n' to quit, any other key to continue")
	if ending == 'n':
		break