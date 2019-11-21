#!/usr/bin/env micropython 
import Robot

import My_block

Robot.gyro.compass_point = 80
My_block.spin_turn(62)
My_block.gyro_straight(75, 8)
Robot.left_attachment.on_for_rotations(100, 1)
My_block.gyro_straight(50, -2)
My_block.spin_turn(90)
My_block.gyro_straight(100, -10)
