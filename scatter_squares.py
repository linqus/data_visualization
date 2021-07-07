import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values, s=10, c=(0,0.8,0))
ax.set_title('Scatter plot')
ax.set_xlabel('Wartości',fontsize=14)
ax.set_ylabel('Kwadraty wartości',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=9)

ax.axis([0,1100,0,1100000])


plt.show()