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

<<<<<<< HEAD
    # go to swingset and release girl
    My_block.ramp_gyro_straight (10, 75, 7.26)
    # back off swingset 
    My_block.gyro_straight (50, -1)
=======
    # Complete Swing and back away

    My_block.ramp_gyro_straight(10, 80, 7.26)

    My_block.gyro_straight(30, -1)
>>>>>>> 28d792f5de7ba0c508e4e91bc82f03fda28e8c87

    # Smush against wall
    
    My_block.spin_turn(0)
    My_block.wall_square(100)

    # Drive to elevator
    
    My_block.gyro_straight(35, 1.62)
    My_block.spin_turn(52)
    My_block.gyro_straight(35, 2.1)

    # qwhack elevator
    
    Robot.left_attachment.on_for_rotations(35, 1)
    sleep(0.5)
    Robot.tank_pair.on_for_rotations(55, 55, -2.5)

    # Return home

    My_block.spin_turn(90)
    My_block.gyro_straight(100, -8)
    My_block.wall_square(100)
