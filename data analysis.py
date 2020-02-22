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
total_secs = 0
total_deg = 0
max_value = -1
min_value = 1000
number_of_lines = 0

# Parse log file
with open('log_data.txt', 'r') as log:
    for line in log:
        # reads one line in the file and splits it into three values.
        elapsed, error, target_angle = line.split(',')
        # convert strings to numbers
        elapsed = float(elapsed)
        error = int(error)
        target_angle = int(target_angle)
        # set min and max.
        if elapsed > longest_time:
            longest_time = elapsed
        if elapsed <= shortest_time:
            shortest_time = elapsed
        total_error = error + total_error
        number_of_lines = number_of_lines + 1
        total_deg = total_deg + target_angle
        total_secs = elapsed + total_secs

average_error = total_error / number_of_lines
msecs_per_deg = (total_secs / total_deg) * 1000
print("longest_time: {:.2f}s".format(longest_time))
print("shortest_time: {:.2f}s".format(shortest_time))
print("average_error: {:.2f}deg".format(average_error))
print("total_secs: {:.2f}s".format(total_secs))
print("total_deg: {:.2f}deg".format(total_deg))
print("msecs_per_deg: {:.2f}msecs".format(msecs_per_deg))

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


