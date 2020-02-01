#!/usr/bin/env micropython
import time

# List of spin turn error values
data = []

# open log file
# logfile = open('log.txt','r')

# Capture some statistics
longest_time = 0
shortest_time = 99999999999
total_error = 0
max_value = -1
min_value = 1000

# Parse log file
with open('log_data.txt', 'r') as log:
    for line in log:
        elapsed, compass_point, target_angle = line.split(',')
        elapsed = float(elapsed)
        compass_point = int(compass_point)
        target_angle = int(target_angle)
        if elapsed > longest_time:
            longest_time = elapsed
        if elapsed <= shortest_time:
            shortest_time = elapsed
        # data.append((elapsed, compass_point, target_angle))
# for line in logfile:
#     data.append(int(line))
# print(data)

print("longest_time: {:.2f}s".format(longest_time))
print("shortest_time: {:.2f}s".format(shortest_time))

# for item in data:
#     total_error += item
#     if item > max_value:
#         max_value = item
#     if item < min_value:
#         min_value = item

print('total is {}'.format(total_error))
# number of data values
data_values = len(data)

# prints out statsistics
print('number of samples is {}'.format(data_values))
print('minimum value is {}'.format(min_value))
print('maximum value is {}'.format(max_value))

# Computes Average
# average = total_error/data_values
# print('Average is {} degrees'.format(round(average, 2)))

