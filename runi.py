#!/usr/bin/env micropython
import Robot
"""This is mission 12 and 13 and it scores 95 points. This is Kyan and Rushil's mission.
"""

#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, 4.5)
Robot.tank_pair.on_for_rotations(50, 50, -2.25)
Robot.tank_pair.on_for_rotations(0, 100, 3)
Robot.tank_pair.on_for_rotations(50, 50, 5)