#!/usr/bin/env micropython
import Robot
#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, -4)
Robot.tank_pair.on_for_rotations(50, 50, 4.5)