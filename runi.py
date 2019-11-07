#!/usr/bin/env micropython

import Robot
"""
This is mission 12 and 13 and it scores 95 points. This is Kyan and Rushil's mission.
"""

def push_tan_blocks_and_return():
    """
    Pushes blocks to the red circle then returns to base.
    """
    #Robot.gyro.compass_point = 0
    Robot.tank_pair.on_for_rotations(50, 50, 2.9)
    Robot.tank_pair.on_for_rotations(50, 50, -1.5)
    Robot.tank_pair.on_for_rotations(100, 0, .5)
    Robot.tank_pair.on_for_rotations(50, 50, 3.5)
