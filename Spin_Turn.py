#!/usr/bin/env micropython
from shiva_gyro import ShivaGyro
import Robot
from sys import stderr

gyro = ShivaGyro(Robot.INPUT_2)


def spin_turn(target_angle, on=False):
    turn_left = True
    gyro = ShivaGyro(Robot.INPUT_2)
    if not on:
        if target_angle > gyro.compass_point:
            Robot.left_wheel.on(30)
            Robot.right_wheel.on(-30)
        else:
            Robot.left_wheel.on(-30)
            Robot.right_wheel.on(30)
        return spin_turn(target_angle, on=True)

    if target_angle > gyro.compass_point:
        while target_angle > gyro.compass_point:
            pass
        Robot.left_wheel.off(brake=True)
        Robot.right_wheel.off(brake=True)
        return
    else:
        while target_angle > gyro.compass_point:
            pass
        Robot.left_wheel.off(brake=True)
        Robot.right_wheel.off(brake=True)
        return
