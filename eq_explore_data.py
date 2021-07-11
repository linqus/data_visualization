import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as file:
	all_eq_data = json.load(file)

readable_filename = 'data/readable_eq_data.json'
with open(readable_filename,"w") as file:
	json.dump(all_eq_data,file,indent=4)