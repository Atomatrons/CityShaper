#!/usr/bin/env micropython

import My_block
import Robot
"""
This is mission 12 and 13 and it scores 95 points. This is Kyan and Rushil's mission.
"""

def push_tan_blocks_and_return():
    """
    Pushes blocks to the red circle then returns to base.
    """
    Robot.gyro.compass_point = 75
    Robot.tank_pair.on_for_rotations(50, 50, 2.9)
    Robot.tank_pair.on_for_rotations(50, 50, -1.5)
    My_block.spin_turn(90)
    Robot.tank_pair.on_for_rotations(50, 50, 5)
