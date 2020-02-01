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
        speed = target_angle - current_angle
        if speed > 40:
            speed = 40
        if speed < 5:
            speed = 5
        Robot.debug_print("CW current_angle: {}, target_angle: {}, speed: {}".format(current_angle, target_angle, speed))
        Robot.tank_pair.on(speed, -speed)
        current_angle = Robot.gyro.compass_point
        if current_angle >= target_angle:
            return
        
    # counterclockwise
    while current_angle > target_angle:
        speed = abs(target_angle - current_angle)
        if speed > 40:
            speed = 40
        if speed < 5:
            speed = 5
        Robot.debug_print("CCW current_angle: {}, target_angle: {}, speed: {}".format(current_angle, target_angle, speed))
        Robot.tank_pair.on(-speed, speed)
        current_angle = Robot.gyro.compass_point

Robot.gyro.compass_point = 0
proportional_turn(180)
Robot.debug_print("Final Heading: {}".format(Robot.gyro.compass_point))
proportional_turn(-180)
Robot.debug_print("Final Heading: {}".format(Robot.gyro.compass_point))
