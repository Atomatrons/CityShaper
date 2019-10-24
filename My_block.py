# My_block.py - Utility programs for use in runs
from time import sleep
import Robot


# Defines the line square program


def line_square(left_wheel_speed=10, right_wheel_speed=10):
    """
    Checks when each color sensor reads a reflected light intensity value
    under 10.  When a color sensor reads a value under 10, it stops the
    coresponding motor. Motor default speed is 10.
    """

    # Turns on the motors
    Robot.left_wheel.on(left_wheel_speed)
    Robot.right_wheel.on(right_wheel_speed)

    # Esablishes varibles that tell the program if a motor is stopped
    left_is_on = True
    right_is_on = True

    # Checks the color sensor values to find black. When a color sensor finds black, it stops the corresponding motor.

    while left_is_on and right_is_on:

        if Robot.right_color.is_at_white():
            Robot.right_wheel.off(brake=True)
            right_is_on = False

        if Robot.left_color.is_at_white():
            Robot.left_wheel.off(brake=True)
            left_is_on = False

    Robot.sleep(0.1)

    Robot.left_wheel.on(left_wheel_speed/4)
    Robot.right_wheel.on(right_wheel_speed/4)

    right_is_on = True
    left_is_on = True

    while left_is_on and right_is_on:

        if Robot.right_color.is_at_black():
            Robot.right_wheel.off(brake=True)
            right_is_on = False

        if Robot.left_color.is_at_black():
            Robot.left_wheel.off(brake=True)
            left_is_on = False


# Defines the wall square program


def wall_square(speed=10):
    """
    Program that squares against a wall
    """
    if speed > 0:
        speed = speed*(-1)
    Robot.steer_pair.on(0, speed)
    while True:
        if Robot.touch.is_pressed == True:
            Robot.sleep(0.2)
            Robot.steer_pair.off(brake=True)
            break


# Defines the SpinTurn program

def SpinTurn(target_angle):
    """
    Turns the robot untill the gyro reads the target angle compass point
    """
    # Turns on the motors
    if target_angle > Robot.gyro.compass_point:
        Robot.tank_pair.on(25, -25)
    else:
        Robot.tank_pair.on(-25, 25)

    # Checks if the gyro compass point angle equals target_angle
    if target_angle > Robot.gyro.compass_point:
        while target_angle > Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle < Robot.gyro.compass_point:
            while target_angle < Robot.gyro.compass_point:
                Robot.tank_pair.on(-2, 2)
    # Checks if the gyro compass point angle equals target_angle
    else:
        while target_angle < Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle > Robot.gyro.compass_point:
            while target_angle > Robot.gyro.compass_point:
                Robot.tank_pair.on(2, -2)

#Defines the gyro_straight program
def gyro_straight(speed, rotations):
    """
    Makes the robot go straight using the gyro.
    """
    #Sets the degree value the robot will try to stick to
    true_north = Robot.gyro.angle
    
    # checks if the robot should go backward or not
    if rotations*speed < 0:
        if rotations > 0:
            target_rotations = Robot.left_wheel.rotations - rotations
        else:
            target_rotations = Robot.left_wheel.rotations + rotations

        while Robot.left_wheel.rotations > target_rotations:
            Robot.steer_pair.on(true_north-Robot.gyro.angle, -speed)
            



    else:
        if rotations < 0:
            target_rotations = Robot.left_wheel.rotations - rotations
        
        else:
            target_rotations = Robot.left_wheel.rotations + rotations
    
        while Robot.left_wheel.rotations < target_rotations:
            Robot.steer_pair.on(true_north-Robot.gyro.angle, speed)   
    Robot.steer_pair.off(brake = True)