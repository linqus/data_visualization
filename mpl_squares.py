import matplotlib.pyplot as plt

values = range(1,6)
squares = [x**2 for x in range(1,6)]

fig, ax = plt.subplots()

ax.plot(values,squares,linewidth=3)
ax.set_title("Kwadraty",fontsize=20)
ax.set_xlabel('Wartosć',fontsize=14)
ax.set_ylabel('Wartość do kwadratu',fontsize=14)
ax.tick_params(axis='both',width=3,labelsize=14)

plt.show()


