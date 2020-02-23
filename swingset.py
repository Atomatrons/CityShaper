#!/usr/bin/env micropython

# Swingset: Completes M-07 Swing and M-08 Elevator

import Robot
import My_block
from time import sleep

def swingset_mission():
    """
    Completes M-07 Swing, and M-08 Elevator.
    """
    
    Robot.right_attachment.on_for_seconds(50, 1)

    # Establishes the compass point the robot is facing
    
    Robot.gyro.compass_point = 90

    # Complete Swing and back away

    My_block.gyro_straight(40, 7.36)

    My_block.gyro_straight(30, -1)

    # Smush against wall
    
    My_block.spin_turn(0)
    My_block.wall_square(100)

    # Drive to elevator
    
    My_block.gyro_straight(35, 1.62)
    My_block.spin_turn(56)
    My_block.gyro_straight(35, 2.15)

    # qwhack elevator
    
    Robot.left_attachment.on_for_rotations(35, 1)
    sleep(0.5)
    Robot.tank_pair.on_for_rotations(55, 55, -1.05)
    Robot.left_attachment.on_for_rotations(-35, 0.95)


    # Do House Mission
    Robot.debug_print(Robot.gyro.compass_point)

    My_block.spin_turn(89)

    Robot.debug_print(Robot.gyro.compass_point)

    Robot.right_attachment.on_for_seconds(-50, 1.4)
    
    Robot.debug_print(Robot.gyro.compass_point)

    My_block.gyro_straight(30, 0.81)

    Robot.debug_print(Robot.gyro.compass_point)

    My_block.spin_turn(99)

    Robot.debug_print(Robot.gyro.compass_point)
    
    Robot.steer_pair.on_for_rotations(0, -20, 0.3)

    My_block.spin_turn(93)

    Robot.debug_print(Robot.gyro.compass_point)

    Robot.steer_pair.on_for_rotations(0, -20, 0.3) 

    My_block.spin_turn(86)

    
    # Go Home.


    My_block.gyro_straight(100, 6)
    My_block.wall_square(100)
    Robot.right_attachment.on_for_rotations(100, 2.2)
    sleep(0.4)
    My_block.spin_turn(0)