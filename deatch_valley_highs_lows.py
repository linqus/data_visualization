import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as file:
	reader = csv.reader(file)
	header_row = next(reader)


	dates, highs, lows = [],[],[]
	for row in reader:
		date = datetime.strptime(row[2],"%Y-%m-%d")
		try:
			 high = int(row[4])
			 low = int(row[5])
		except ValueError:
			print(f'Brak wartości dla daty: {row[2]}')
		else: 
			dates.append(date)
			highs.append(high)
			lows.append(low)
fig,ax = plt.subplots(figsize=(13,6))

ax.set_title('Najwyższe i najniższe dzienne temperatury w 2018r w Dolinie Śmierci',fontsize=18)
ax.set_xlabel('Daty',fontsize=16)
ax.set_ylabel('Temperatura (F)',fontsize=16)
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)

ax.fill_between(dates,highs,lows,facecolor='orange',alpha=0.8)


fig.autofmt_xdate()
plt.show()