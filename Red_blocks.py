#!/usr/bin/env micropython
import My_block
import Robot

# Red_blocks: Completes M-12 Design & Build, and M-13 Sustainability Upgrades.


def push_red_blocks_and_return():
    """
    Completes M-12 Design & Build, and M-13 Sustainability Upgrades.
    """

    # Establishes the compass point the root is facing

    Robot.gyro.compass_point = 75

    # Drops off the blocks

    Robot.tank_pair.on_for_rotations(50, 50, 3.9)

    Robot.tank_pair.on_for_rotations(50, 50, -1.5)

    # Returns home

    My_block.spin_turn(90)

    My_block.wall_square(100)
