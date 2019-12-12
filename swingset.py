#!/usr/bin/env micropython

import Robot
import My_block
from time import sleep

Robot.gyro.compass_point = 90
"""
Robot.steer_pair.on_for_rotations(0, 10, 1, False)
Robot.steer_pair.on_for_rotations(0, 20, 1, False)
Robot.steer_pair.on_for_rotations(0, 30, 1, False)
Robot.steer_pair.on_for_rotations(0, 40, 1, False)
Robot.steer_pair.on_for_rotations(0, 50, 0.5, False)
"""
# go to swingset and release girl
My_block.gyro_straight(50, 7.2)

# back off swingset  
My_block.gyro_straight (30, -1)

# smush against wall
My_block.spin_turn(0)
My_block.wall_square(30)

# drive to elevator
My_block.gyro_straight(30, 1.62)
My_block.spin_turn(52)
My_block.gyro_straight(30, 2)

# qwhack elevator
Robot.left_attachment.on_for_rotations(35, 1)
sleep(2)
Robot.tank_pair.on_for_rotations(50, 50, -2.75)
My_block.spin_turn(85)
My_block.gyro_straight(50, -8)
My_block.wall_square(30)