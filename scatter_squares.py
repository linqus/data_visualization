import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values, s=200)
ax.set_title('Scatter plot')
ax.set_xlabel('Wartości',fontsize=14)
ax.set_ylabel('Kwadraty wartości',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=14)

plt.show()