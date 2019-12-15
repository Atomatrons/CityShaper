from ev3dev2.sensor.lego import ColorSensor

# Defines the ShivaColor class


class ShivaColor (ColorSensor):
    """
    Returns true or false statements depending on wether the color sensor is seeing white or black
    """
    # Defines the black and white colorsensor RLI values
    WHITE = 85
    BLACK = 8

    # Defines a function that returns true or false if the color sensor sees black or not

    def is_at_black(self):
        """ returns a true or false statement if the desired color sensor is under or over the reflected light intensity of 7"""
        return self.reflected_light_intensity < self.BLACK

    # Defines a function that returns true or false if the color sensor sees white or not

    def is_at_white(self):
        """ returns a true or false statement if the desired color sensor is over or under the reflected light intensity of 80"""
        return self.reflected_light_intensity > self.WHITE
