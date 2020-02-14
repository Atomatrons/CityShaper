# Shiva_Steering: Program that allows adaptation bewteen different wheel sizes

from ev3dev2.motor import MoveSteering
from ev3dev2.motor import MoveTank
from sys import stderr

factor_imp = open('../factor.txt', 'r')
factor = float(factor_imp.read())


class Shiva_MoveSteering(MoveSteering):
    def on_for_rotations(self, steering, speed, rotations, brake=True, block=True):
        adjusted_rotations = rotations*factor
        print("adjusted rotations {}".format(adjusted_rotations), stderr)
        return super().on_for_rotations(steering, speed, adjusted_rotations, brake=brake, block=block)
    
    def on(self, steering, speed, brake=True, block=True):
        return super().on(steering, speed)



class Shiva_MoveTank(MoveTank):
    def on_for_rotations(self, left_speed, right_speed, rotations, brake=True, block=True):
        return super().on_for_rotations(left_speed, right_speed, rotations*factor, brake=brake, block=block)
    
    def on(self, left_speed, right_speed, brake=True, block=True):
        return super().on(left_speed, right_speed)

