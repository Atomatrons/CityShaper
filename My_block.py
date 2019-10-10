from time import sleep
import Robot

# Defines the line square program


def line_square(left_wheel_speed=10, right_wheel_speed=10):
    """Checks when each color sensor reads a reflected light intensity value under 10.
        When a color sensor reads a value under 10, it stops the coresponding motor. Motor default speed is 10."""
    # Defines left and right wheel speed as integers
    left_wheel_speed = int(left_wheel_speed)
    right_wheel_speed = int(right_wheel_speed)

    # Turns on the motors
    Robot.left_wheel.on(left_wheel_speed)
    Robot.right_wheel.on(right_wheel_speed)

    # Esablishes varibles that tell the program if a motor is stopped
    is_left_stopped = False
    is_right_stopped = False

    # Checks the color sensor values to find black. When a color sensor finds black, it stops the corresponding motor.

    while True:
        is_left_stopped = False
        is_right_stopped = False
        if Robot.right_color.is_at_white():
            Robot.right_wheel.off(brake=True)
            is_right_stopped = True

        if Robot.left_color.is_at_white():
            Robot.left_wheel.off(brake=True)
            is_left_stopped = True

        if is_left_stopped and is_right_stopped == True:
            break
    Robot.left_wheel.on(-10)
    Robot.right_wheel.on(-10)
    while True:

        if Robot.right_color.is_at_black():
            Robot.right_wheel.off(brake=True)
            is_right_stopped = True

        if Robot.left_color.is_at_black():
            Robot.left_wheel.off(brake=True)
            is_left_stopped = True

        if is_left_stopped and is_right_stopped == True:
            break


# Defines the wall square program


def wall_square(speed=10):
    """Program that squares against a wall"""
    if speed < 0:
        speed = speed*(-1)
    Robot.steer_pair.on(0, speed)
    while True:
        if Robot.touch.is_pressed == True:
            Robot.sleep(0.3)
            Robot.steer_pair.off(brake=True)
            break



