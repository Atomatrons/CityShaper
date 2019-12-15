#!/usr/bin/env micropython

import Robot
import My_block

def drone():
    Robot.gyro.compass_point = 0

    My_block.gyro_straight(30, 1.85)

    My_block.spin_turn(40)

    My_block.gyro_straight(30, 2.2)

    My_block.line_square(10, 10)

    My_block.gyro_straight(20, 0.5)

    Robot.right_attachment.on_for_rotations(-100, 5.1)

    My_block.gyro_straight(10, 0.3)

    My_block.spin_turn(30)

    Robot.right_attachment.on_for_rotations(100, 2.3)

    My_block.gyro_straight(-10, 1)
