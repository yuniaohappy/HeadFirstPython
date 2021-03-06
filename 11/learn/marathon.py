from find_it import find_closest
from tm2secs2tm import time2secs, secs2time

def find_nearest_time(look_for,target_data):
    what = time2secs(look_for)
    where = [time2secs(t) for t in target_data]
    res = find_closest(what,where)
    return(secs2time(res))

row_data = {}
with open('PaceData.csv') as paces:
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)        
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[row[i]] = column_headings[i]
        row_data[row_label] = inner_dict

num_cols = len(column_headings)
print(num_cols,end=' -> ')
print(column_headings)

num_2mi = len(row_data['2mi'])
print(num_2mi,end = ' -> ')
print(row_data['2mi'])

num_Marathon = len(row_data['Marathon'])
print(num_Marathon,end = ' -> ')
print(row_data['Marathon'])
