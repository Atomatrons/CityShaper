#!/usr/bin/env micropython

# Swingset: Completes M-07 Swing and M-08 Elevator

import Robot
import My_block
from time import sleep


def swingset_mission():
    """
    Completes M-07 Swing, and M-08 Elevator.
    """
    
    # Establishes the compass point the robot is facing
    
    Robot.gyro.compass_point = 90

    # Complete Swing and back away

    My_block.gyro_straight(50, 7.3)

    My_block.gyro_straight(30, -1)

    # Smush against wall
    
    My_block.spin_turn(0)
    My_block.wall_square(100)

    # Drive to elevator
    
    My_block.gyro_straight(30, 1.62)
    My_block.spin_turn(52)
    My_block.gyro_straight(30, 2.1)

    # qwhack elevator
    
    Robot.left_attachment.on_for_rotations(35, 1)
    sleep(1)
    Robot.tank_pair.on_for_rotations(50, 50, -2.5)

    # Return home

    My_block.spin_turn(90)
    My_block.gyro_straight(100, -8)
    My_block.wall_square(100)
