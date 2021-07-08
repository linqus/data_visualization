from die import Die

die = Die()
results = []
for x in range(100):
	results.append(die.roll())

print(results)