#!/usr/bin/env micropython

import My_block
import Robot


while True:
    if Robot.button.on_up and Robot.button.on_down:
        Robot.sound.speak("Run 1 commencing")
    if Robot.button.up:
        Robot.sound.speak("Run 2 commencing")
    if Robot.button.left:
        Robot.sound.speak("Run 3 commencing")
    if Robot.button.right:
        Robot.sound.speak("Run 4 commencing")