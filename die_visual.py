from die import Die

die = Die()
results = []
for x in range(1000):
	results.append(die.roll())

frequencies = []
for i in range(1,die.sides+1):
	frequencies.append(0)

for n in results:
	frequencies[n-1] += 1

print(frequencies)
