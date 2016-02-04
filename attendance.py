import csv
def read_sheet(csv_name, search_val):
	attendance_hash = {}
	with open(csv_name) as csvfile:
		namereader = csv.reader(csvfile, delimiter=',')
		idx = 0
		for row in namereader:
			if idx>0:
				# date and timestamp
				vals = row[1].split()
				#find and splice to get only the date
				space = row[0].find(' ')
				date = row[0][:space]
				# first
				# last
				# if at least 2 vals, add meeting to hash
				if(len(vals)==2):
					this_key = str(vals[0]) + '_' + str(vals[1])
					if this_key not in attendance_hash:
						attendance_hash[this_key] = []
					if str(date) not in attendance_hash[this_key]:
						attendance_hash[this_key].append(str(date))
			idx+=1
	#length of array at hash key will be number of meetings attended
	print(len(attendance_hash[search_val]))

def eventcounter(csv_name, search_val):
	attendance_hash = {}
	with open(csv_name) as csvfile:
		namereader = csv.reader(csvfile, delimiter=',')
		idx = 0
		for row in namereader:
			if idx>0:
				# date and timestamp
				vals = row[1].split()
				#find and splice to get only the date
				space = row[0].find(' ')
				date = row[0][:space]
				#professional
				print(row)
				hours_events = {}
				#professional
				#if row[2]=='':
					#hours_events['profesh'] = []
				if row[2]!='':
					pro_hours = get_hours(row[2])
					hours_events['profesh'] = pro_hours
				#philanthropy
				#if row[2]=='':
					#hours_events['phil'] = []
				if row[3]!='':
					phil_hours = get_hours(row[3])
					hours_events['phil'] = phil_hours
				#brotherhood
				#if row[4]=='':
					#hours_events['bro'] = []
				if row[4]!='':
					bro_hours = get_hours(row[4])
					hours_events['bro'] = bro_hours
				#skip one row
				#rush
				#if row[6]=='':
					#hours_events['rush'] = []
				if row[6]!='':
					rush_hours = get_hours(row[6])
					hours_events['rush'] = rush_hours
				# first
				# last
				# if at least 2 vals, add meeting to hash
				if(len(vals)==2):
					this_key = str(vals[0]) + '_' + str(vals[1])
					print("key")
					print(this_key)
					if this_key not in attendance_hash:
						attendance_hash[this_key] = hours_events
					else:
						#for dic in attendance_hash[this_key]:
						attendance_hash[this_key] = add_dicts(attendance_hash, hours_events)
						#attendance_hash[this_key].append(hours_events)
			idx+=1
	#length of array at hash key will be number of meetings attended
	print(attendance_hash[search_val])

def get_hours(hours_str):
	time_vals = []
	times = hours_str.split(':')
	times = [int(x) for x in times]
	return times
def add_dicts(main_dic, added_dict):
	new_dict = added_dict.copy()
	main_dic = main_dic.update(new_dict)
	return main_dic


read_sheet('attendance.csv', 'Wilson_Ngai')
eventcounter('event.csv', 'Logan_Crull')
