#!/usr/bin/env micropython
import Robot


def push_block_return():
    """ 
    This is the tan block pushing mission and it scores 60 points. This is Kyan and Rushil's second mission.
    """
    #Robot.gyro.compass_point = 0
    #Robot.tank_pair.on_for_rotations(50, 50, 4)
    #Robot.tank_pair.on_for_rotations(50, 50, -2.75)
    Robot.tank_pair.on_for_rotations(50, 50, 4.5)
    Robot.tank_pair.on_for_rotations(50, 50, -2.25)
    Robot.tank_pair.on_for_rotations(0, 20, 3)
    Robot.tank_pair.on_for_rotations(50, 50, 5)