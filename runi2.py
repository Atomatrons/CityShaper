#!/usr/bin/env micropython
import Robot
import My_block

def red_push_block_return():
    """ 
    This is the red block pushing mission and it scores 95 points. This is Kyan and Rushil's second mission.
    """
    Robot.gyro.compass_point = 0
    #Robot.tank_pair.on_for_rotations(50, 50, 4)
    #Robot.tank_pair.on_for_rotations(50, 50, -2.75)
    Robot.tank_pair.on_for_rotations(50, 50, 4.5)
    Robot.tank_pair.on_for_rotations(50, 50, -2.25)
    My_block.spin_turn(90)
    Robot.tank_pair.on_for_rotations(50, 50, -5)