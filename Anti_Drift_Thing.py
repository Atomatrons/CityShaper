#!/usr/bin/env micropython
import Robot
import My_block

def Anti_Drift_Thing():
    """
    Checks is gyro is drifting, if it is, do a manual reset
    """
    print("Gyro is check")

    old_angle = Robot.gyro.angle
    Robot.sleep(5)
    new_angle = Robot.gyro.angle

    while old_angle != new_angle:
        old_angle = Robot.gyro.angle
        Robot.sleep(2)
        new_angle = Robot.gyro.angle
        if old_angle == new_angle:
            print("Angle be good")
            Robot.sleep(1)
        else:
         print("Not good angle be")
        Robot.sleep(3)
    print("Angle be good")
    Robot.sleep(1)
