import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, lows, highs = [], [],[]
	for row in reader:
		dates.append(datetime.strptime(row[2],"%Y-%m-%d"))
		highs.append(int( row[5] ))
		lows.append(int( row[6] ))

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates,highs,c='Red')
ax.plot(dates,lows,c='Blue')
ax.set_title('Dzienne temperatury w 2018 w Sitka')
ax.set_xlabel('',fontsize=14)
ax.set_ylabel('Temperatura (F)',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()
plt.show()