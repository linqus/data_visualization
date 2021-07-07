import matplotlib.pyplot as plt

from random_walk import RandomWalk




while True:
	fig, ax = plt.subplots()
	rw = RandomWalk()
	rw.fill_walk()

	ax.scatter(rw.x_values,rw.y_values,s=7,c=range(1,5001),cmap=plt.cm.hot)

	plt.show()
	ending = input("Press 'n' to quit, any other key to continue")
	if ending == 'n':
		break