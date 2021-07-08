from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline 


results = []
die1 = Die()
die2 = Die()
die3 = Die()
num_rolls = 100_000
for x in range(num_rolls):
	results.append(die1.roll()+die2.roll()+die3.roll())

frequencies = []
max_rolls = die1.sides+die2.sides+die3.sides
for i in range(3,max_rolls+1):
	frequencies.append(results.count(i))

x_values = list(range(3,max_rolls+1))
data = [Bar(x=x_values,y=frequencies)]


my_layout = Layout(
				title=f"Wynik {num_rolls} rzutów trzema kostkami D6", 
				xaxis={'title':'Wynik','dtick':1},
				yaxis={'title':'Częstość wyniku'}
			)

offline.plot({'data':data, 'layout':my_layout},filename='d6_d6_d6.html')