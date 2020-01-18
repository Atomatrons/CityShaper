#!/usr/bin/env micropython

import Robot
import My_block

def proportional_turn(target_angle):
    '''
    proportional_turn goes from the compass point it's pointing at to the target angle with a slowly decreasing speed.  
    '''
    current_angle = Robot.gyro.compass_point

    # clockwise
    while current_angle < target_angle:
        speed = abs(target_angle - current_angle)
        if speed < 5:
            speed = 5
        Robot.tank_pair.on(speed, -speed)
        if current_angle >= target_angle:
            return
        
    # counterclockwise
    while current_angle > target_angle:
        speed = abs(target_angle - current_angle)
        if speed < 5:
            speed = 5
        Robot.tank_pair.on(-speed, speed)