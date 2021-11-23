import board
import neopixel
from .SimpleMode import SimpleMode

class SimpleTimedMode(SimpleMode):
    def __init__(self, numLights, colorOn, colorOff, delayOff=5):
        super()
        self.numLights = numLights
        self.on = colorOn
        self.off = colorOff
        self.delayOff = delayOff
        self.pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))

    def processEvent(self, event):
        message, deltatime = event
        if (deltatime > self.delayOff):
            self.pixels.fill((0,0,0))
        SimpleMode.processEvent(self, event)
