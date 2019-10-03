from time import sleep
import Robot

#Defines the line square program

def line_square(left_wheel_speed = 10, right_wheel_speed = 10):

    left_wheel_speed = int(left_wheel_speed)
    right_wheel_speed = int(right_wheel_speed)

    #Turns on the motors
    Robot.left_wheel.on(left_wheel_speed)
    Robot.right_wheel.on(right_wheel_speed)

    #Esablishes varibles that tell the program if a motor is stopped
    stop_left= False
    stop_right= False

    """Checks when each color sensor reads a reflected light intensity value under 10.
    When a color sensor reads a value under 10, it stops the coresponding motor"""

    while True:
        if Robot.cl_right.reflected_light_intensity < 7:
            Robot.right_wheel.off(brake = True)
            stop_right = True
        
        if Robot.cl_left.reflected_light_intensity < 7:
            Robot.left_wheel.off(brake = True)
            stop_left = True
        
        if stop_left and stop_right == True:
            break


