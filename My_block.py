from time import sleep
import Robot

# Defines the line square program


def line_square(left_wheel_speed=10, right_wheel_speed=10):
    """Checks when each color sensor reads a reflected light intensity value under 10.
        When a color sensor reads a value under 10, it stops the coresponding motor. Motor default speed is 10."""
    #Defines left and right wheel speed as integers
    left_wheel_speed = int(left_wheel_speed)
    right_wheel_speed = int(right_wheel_speed)

    # Turns on the motors
    Robot.left_wheel.on(left_wheel_speed)
    Robot.right_wheel.on(right_wheel_speed)

    # Esablishes varibles that tell the program if a motor is stopped
    is_left_stopped = False
    is_right_stopped = False

    while True:

        if Robot.color_right.reflected_light_intensity < 7:
            Robot.right_wheel.off(brake=True)
            is_right_stopped = True

        if Robot.color_left.reflected_light_intensity < 7:
            Robot.left_wheel.off(brake=True)
            is_left_stopped = True

        if is_left_stopped and is_right_stopped == True:
            break
