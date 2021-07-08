from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline 


die1 = Die(8)
die2 = Die(8)
results = []
num_rolls = 10_000_000
for x in range(num_rolls):
	results.append(die1.roll()+die2.roll())

frequencies = []
for i in range(2,die1.sides+die2.sides+1):
	frequencies.append(results.count(i))

x_values = list(range(2,die1.sides+die2.sides+1))
data = [Bar(x=x_values,y=frequencies)]


my_layout = Layout(
				title=f"Wynik {num_rolls} rzutów dwiema kostkami D8", 
				xaxis={'title':'Wynik','dtick':1},
				yaxis={'title':'Częstość wyniku'}
			)

offline.plot({'data':data, 'layout':my_layout},filename='d6_d10.html')