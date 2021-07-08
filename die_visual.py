from die import Die

die = Die()
results = []
for x in range(1000):
	results.append(die.roll())

frequencies = []
for i in range(1,die.sides+1):
	frequencies.append(results.count(i))

print(frequencies)
