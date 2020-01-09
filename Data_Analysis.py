#!/usr/bin/env micropython

import statistics

# List of spin turn error values
data = []

# open log file
logfile = open ('log_data.txt','r')
 
 # read file into 
for line in logfile:
    data.append(int(line))

# compute some statistics
total_error = 0
max_value = -1
min_value = 1000
for item in data:
    total_error += item
    if item > max_value:
        max_value = item
    if item < min_value:
        min_value = item

# number of data values
data_values = len(data)

# Computes Average
average = total_error/data_values

#Prints out Data Values
print("samples: {}, Min: {}, Max: {}, Avg:{}, Median: {}".format(data_values, min_value, max_value, average, statistics.median(data)))



