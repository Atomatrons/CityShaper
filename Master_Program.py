#!/usr/bin/env micropython

import My_block
import Robot
from runi2 import push_block_return
from runi import push_tan_blocks_and_return

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
                Robot.sound.speak("Run 3")
                push_tan_blocks_and_return()

    if Robot.button.right == True:
        for int in range(0, 1000):
            if Robot.button.enter == True:
                Robot.sound.speak("Run 4")
                push_block_return()
