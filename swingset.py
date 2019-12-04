#!/usr/bin/env micropython

import Robot
import My_block

Robot.gyro.compass_point = 90
"""
Robot.steer_pair.on_for_rotations(0, 10, 1, False)
Robot.steer_pair.on_for_rotations(0, 20, 1, False)
Robot.steer_pair.on_for_rotations(0, 30, 1, False)
Robot.steer_pair.on_for_rotations(0, 40, 1, False)
Robot.steer_pair.on_for_rotations(0, 50, 1, False)
"""
My_block.gyro_straight(50, 7)

# Robot.t*--ank_pair.on_for_rotations(25,25,1)

Robot.steer_pair.on_for_rotations(0,50,-2)

My_block.gyro_straight(80,-8)
