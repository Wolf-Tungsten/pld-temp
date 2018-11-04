from pynq.overlays.base import BaseOverlay
from pynq.lib.arduino import Arduino_IO
base = BaseOverlay("base.bit")
class PynqIO(object):
    def __init__(self):
        self.__light_pin = Arduino_IO(base.ARDUINO, 0, 'out')
        self.__switch = base.switches[0]
        self.__rgbled = base.rgbleds[4]
    def turn_on_light(self):
        self.__light_pin.write(1)
    def turn_off_light(self):
        self.__light_pin.write(0)
    def read_switch(self):
        return False if self.__switch.read() == 0 else True
    def set_alarm(self):
        base.rgbleds[4].write(4)
        base.rgbleds[5].write(4)
    def clear_alarm(self):
        base.rgbleds[4].write(4)
        base.rgbleds[5].write(4)