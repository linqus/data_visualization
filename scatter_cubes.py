import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values,s=5,c=y_values,cmap=plt.cm.hsv)
ax.axis( (0,6001,0,1000_0000_000_00) )
ax.set_title('Sześciany')
ax.set_xlabel('wartości')
ax.set_ylabel('sześciany wartości')
ax.tick_params(axis='x',labelsize=20)


plt.savefig('szesciany.png',bbox_inches='tight')