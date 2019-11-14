#!/usr/bin/env micropython

import My_block
import Robot

# Checks if certain buttons are being pressed
while True:
    if Robot.button.up == True:
        for int in range(0, 1000):
            if Robot.button.enter == True:
                Robot.sound.speak("Run 1 would be running")

    if Robot.button.down == True:
        for int in range(0, 1000):
            if Robot.button.enter == True:
                Robot.sound.speak("Run 2 would be running")

    if Robot.button.left == True:
        for int in range(0, 1000):
            if Robot.button.enter == True:
                Robot.sound.speak("Run 3 would be running")

    if Robot.button.right == True:
        for int in range(0, 1000):
            if Robot.button.enter == True:
                Robot.sound.speak("Run 4 would be running")
