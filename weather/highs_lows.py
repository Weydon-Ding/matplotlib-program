import csv
from datetime import datetime

from matplotlib import pyplot as plt

def highs_lows(file_name):
	filename = file_name + '.csv'
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
	
		dates, highs, lows = [], [], []
		for row in reader:
			try:
				current_date = datetime.strptime(row[0],"%Y-%m-%d")
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(filename, current_date, 'missing data!')
			else:			
				dates.append(current_date)
				highs.append(high)
				lows.append(low)
		
	fig = plt.figure(dpi=128,figsize=(10,6))
	plt.plot(dates,highs,c='red',alpha=0.5)
	plt.plot(dates,lows,c='blue',alpha=0.5)
	plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

	title = "Daily high and low tempeatures - \n%s, CA" % file_name
	plt.title(title,fontsize=20)
	plt.xlabel('',fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature(F)",fontsize=16)
	plt.tick_params(axis='both',which='major',labelsize=16)

	plt.savefig(file_name + '.png',bbox_inches='tight')
	print(file_name + '.png saved')



filename_list = ['sitka_weather_07-2014', 'sitka_weather_2014', 
	'death_valley_2014']

for filename in filename_list:
	highs_lows(filename)
