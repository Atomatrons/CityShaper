#!/usr/bin/env micropython

import Robot
import My_block

Robot.gyro.compass_point = 0

My_block.gyro_straight(30, 2)

My_block.spin_turn(39)

My_block.gyro_straight(30, 3)

Robot.right_attachment.on_for_rotations(-100, 5.1)

My_block.gyro_straight(10, 0.45)

Robot.right_attachment.on_for_rotations(100, 4.8)

My_block.gyro_straight(-5, 0.4)

My_block.spin_turn(180)

My_block.wall_square(-30)

My_block.gyro_straight(10, 0.15)

My_block.spin_turn(130)
