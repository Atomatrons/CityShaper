#!/usr/bin/env micropython
import My_block
import Robot

# Red_blocks: Completes M-12 Design & Build, and M-13 Sustainability Upgrades.

# Programmed by Kyan


def push_red_blocks_and_return():
    """
    Completes M-12 Design & Build, and M-13 Sustainability Upgrades.
    """

    # Establishes the compass point the root is facing

    Robot.gyro.compass_point = 75

    # Drops off the blocks

    My_block.gyro_straight(50, 3.9)
    # Robot.tank_pair.on_for_rotations(50, 50, 3.9)

    My_block.gyro_straight(50, -1)
    #Robot.tank_pair.on_for_rotations(50, 50, -1)

    My_block.spin_turn(0)

    My_block.gyro_straight(50, 0.7)
    #Robot.tank_pair.on_for_rotations(50, 50, .7)

    My_block.spin_turn(58)

    My_block.gyro_straight(20, 1.29)
    #Robot.tank_pair.on_for_rotations(20, 20, 1.295)

    # Returns home
    My_block.gyro_straight(25, -1.5)
    #Robot.tank_pair.on_for_rotations(25, 25, -1.5)
    My_block.spin_turn(80)

    My_block.wall_square(90)
