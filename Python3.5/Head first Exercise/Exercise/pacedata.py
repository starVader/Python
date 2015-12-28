row_data = {}

with open('PaceData.csv') as pace:
	column_headings = pace.readline().strip().split(',')
	column_headings.pop(0)	
	for each in pace:
		row = each.strip().split(',')
		row_label = row.pop(0)
		inner_data = {}
		for i in range(len(column_headings)):
			inner_data[row[i]] = column_headings 
		row_data[row_label] = inner_data 
num_cols = len(column_headings)
print(num_cols, end ='-> ')
print(column_headings)

num_2mi = len(row_data['2mi'])
print(num_2mi,end = '-> ')
print(row_data['2mi'])

num_marathon = len(row_data['Marathon'])
print(num_marathon,end = '-> ')
print(row_data['Marathon'])


