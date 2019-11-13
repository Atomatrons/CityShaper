#!/usr/bin/env micropython

import Robot
import My_block

Robot.gyro.compass_point = 90
My_block.gyro_straight(60, 1)
My_block.gyro_straight(80, 2)
Robot.tank_pair.on_for_rotations(25,25,1)

