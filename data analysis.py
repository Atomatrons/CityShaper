#!/usr/bin/env micropython
import time
import statistics

# Capture some statistics
longest_time = 0
shortest_time = 99999999999
total_secs = 0
max_speed = -1
min_speed = 10000

total_error = 0
max_error = -1
min_error = 10000

total_deg = 0
number_of_lines = 0

error_list = []                 # list of degrees each turn is off from target
mseconds_per_degree_list = []   # list of milliseconds per degree for turn

# Parse log file
with open('log_data_BB.txt', 'r') as log:
    for line in log:
        # reads one line in the file and splits it into three values.
        elapsed, degrees_turned, error = line.split(',')
        # convert strings to numbers
        elapsed = float(elapsed)
        degrees_turned = int(degrees_turned)
        if degrees_turned == 0:
            degrees_turned = 1
        error = int(error)
        speed = (elapsed / degrees_turned) * 1000

        # set min and max times
        if elapsed > longest_time:
            longest_time = elapsed
        if elapsed < shortest_time:
            shortest_time = elapsed

        # set min and max speed
        if speed > max_speed:
            max_speed = speed
        if speed < min_speed:
            min_speed = speed

        # set min and max errors
        if error > max_error:
            max_error = error
        if error < min_error:
            min_error = error

        # update totals
        total_error = error + total_error
        number_of_lines = number_of_lines + 1
        total_deg = total_deg + degrees_turned
        total_secs = elapsed + total_secs

        # append to lists
        error_list.append(error)
        mseconds_per_degree_list.append(speed)

# compute timing stats
msecs_per_deg = (total_secs / total_deg) * 1000
print("total_secs: {:.2f}s".format(total_secs))
print("total_deg: {}deg".format(total_deg))
print("msecs_per_deg: {:.2f}msecs".format(msecs_per_deg))

# compute error stats
average_error = total_error / number_of_lines
print('total error is {}'.format(total_error))

# Print out statistics
print("samples: {}".format(number_of_lines))
print("Min Error: {}, Max Error: {}, Avg Error: {}, Median Error: {}".format(min_error, max_error, average_error, statistics.median(error_list)))
print("Min duration: {:.2f}, Max duration: {:.2f}, Avg duration: {:.2f}".format(shortest_time, longest_time, total_secs / number_of_lines))
print("Min speed: {:.2f}, Max speed: {:.2f}, Avg speed: {:.2f}, Median speed: {:.2f}".format(min_speed, max_speed, msecs_per_deg, statistics.median(mseconds_per_degree_list)))

