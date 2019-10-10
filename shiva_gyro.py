from ev3dev2.sensor.lego import GyroSensor


class ShivaGyro(GyroSensor):


    def __init__(self, port):
        super.__init__(port)
        self.zero_point = 0
    
    @property
    def compass_point(self):
        return self.angle - self.zero_point

    @compass_point.setter
    def compass_point(self, current_heading):
        self.zero_point = self.angle - current_heading
        
