#!/usr/bin/env micropython

import Robot
import My_block
from time import sleep

def swingset_mission(): 
    """
    Does the swing set mission and the elevator mission
    """
    Robot.gyro.compass_point = 90

    # go to swingset and release girl
    My_block.ramp_gyro_straight (10, 75, 7.26)
    # back off swingset 
    My_block.gyro_straight (50, -1)

    # smush against wall
    My_block.spin_turn(0)
    My_block.wall_square(30)

    # drive to elevator
    My_block.gyro_straight(30, 1.62)
    My_block.spin_turn(52)
    My_block.gyro_straight(50, 2.1)

    # qwhack elevator
    Robot.left_attachment.on_for_rotations(35, 1)
    sleep(0.2)
    Robot.tank_pair.on_for_rotations(50, 50, -2.75)
    My_block.spin_turn(90)
    My_block.gyro_straight(100, -8)
    My_block.wall_square(30)
