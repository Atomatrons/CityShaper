#!/usr/bin/env micropython

# Drone: Completes M-03 Inspection Drone.

import Robot
import My_block


def drone():
    """
    Completes M-03 Inspection Drone, plus the Innovative Architecture and Bat missions
    """

    # Establishes the compass point the robot is facing
    Robot.gyro.compass_point = 0

    # Moves the robot forward, turns, and pushes architecture to circle
    My_block.gyro_straight(35,1)
    My_block.spin_turn(44)
    My_block.gyro_straight(35, 1.6)

    # backs up
    My_block.gyro_straight(35,-1)

    # Picks up the drone
    My_block.gyro_straight(20, 0.58)
    Robot.right_attachment.on_for_rotations(-100, 4.9)

    # Drops off the drone on the post
    My_block.gyro_straight(10, 0.38)
    My_block.spin_turn(33)
    Robot.right_attachment.on_for_rotations(100, 2.3)

    # Returns home
    My_block.gyro_straight(-10, 0.8)
    My_block.wall_square(-100)
    Robot.right_attachment.on_for_seconds(40, 5)


drone()