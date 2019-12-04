#!/usr/bin/env micropython
import Robot
import My_block

Robot.gyro.compass_point = 0

My_block.gyro_straight(30, 5)

My_block.spin_turn(90)