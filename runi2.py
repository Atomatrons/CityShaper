#!/usr/bin/env micropython
import Robot
#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, -2.75)
Robot.tank_pair.on_for_rotations(50, 50, 3)