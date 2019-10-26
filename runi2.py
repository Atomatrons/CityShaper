#!/usr/bin/env micropython
import Robot
""" This is the tan block pushing mission and it scores 60 points. This is Kyan and Rushil's second mission.
"""

#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, 3)
Robot.tank_pair.on_for_rotations(50, 50, -2.75)