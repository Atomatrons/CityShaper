#!/usr/bin/env micropython 
import Robot
#Imports the code from the file Robot which defines the which defines ports, and motors, compass points
import My_block
#Import a file that is called My_block which is like the feature in Mindstorms and defines gyro staight, spin turn, square to line 
Robot.gyro.compass_point = 81
#Says that right now that we are 81 degrees
My_block.spin_turn(62)
#Now we need to turn the Robot to 62 degrees
My_block.gyro_straight(75, 5)
My_block.gyro_straight(50, 3.1)
#The robot goes 8.1 rotations to get to the elevator mission model
Robot.left_attachment.on_for_rotations(100, 1)
#Swings the attachement to flip the elevator and complete the mission
My_block.gyro_straight(50, -2)
#Backs away from the mission model 
My_block.spin_turn(90)
My_block.gyro_straight(100, -10)
#Turns the robot and then backs up to home
