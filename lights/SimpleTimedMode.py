import board
import neopixel
from .SimpleMode import SimpleMode

class SimpleTimedMode(SimpleMode):
    def __init__(self, numLights, colorOn, colorOff, delayOff=5):
        super().__init__(numLights, colorOn, colorOff)
        self.delayOff = delayOff

    def processEvent(self, event):
        message, deltatime = event
        if (deltatime > self.delayOff):
            self.pixels.fill((0,0,0))
            self.nextLight = 0
            self.prevLight = 0
        SimpleMode.processEvent(self, event)
