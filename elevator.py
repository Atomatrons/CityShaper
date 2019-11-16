#!/usr/bin/env micropython 
import Robot

import My_block

Robot.gyro.compass_point = 80
My_block.gyro_straight(75, 7.5)
Robot.left_attachment.on_for_rotations(100, 1)
My_block.spin_turn(93)
Robot.tank_pair.on_for_rotations(-100, -100, 11)
