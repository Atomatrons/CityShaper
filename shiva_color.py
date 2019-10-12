from ev3dev2.sensor.lego import ColorSensor


class shiva_color (ColorSensor):
    WHITE = 80
    BLACK = 9

    def is_at_black(self):
        """ returns a true or false statement if the desired color sensor is under or over the reflected light intensity of 7"""
        return self.reflected_light_intensity < self.BLACK

    def is_at_white(self):
        """ returns a true or false statement if the desired color sensor is over or under the reflected light intensity of 80"""
        return self.reflected_light_intensity > self.WHITE
